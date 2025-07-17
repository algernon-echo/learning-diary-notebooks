# (Claude Sonnet 4)

import fitz
import os

# ===== 1. 页面操作 =====
def page_operations(pdf_path, output_path):
    """页面增删改操作"""
    doc = fitz.open(pdf_path)
    
    # 删除页面
    doc.delete_page(0)  # 删除第一页
    doc.delete_pages([2, 4, 6])  # 删除多个页面
    
    # 插入空白页
    new_page = doc.new_page(width=595, height=842)  # A4尺寸
    
    # 复制页面
    doc.copy_page(0, 5)  # 将第0页复制到第5页位置
    
    # 移动页面
    doc.move_page(2, 0)  # 将第2页移动到第0页位置
    
    doc.save(output_path)
    doc.close()

# ===== 2. 文本编辑 =====
def text_operations(pdf_path, output_path):
    """文本添加和编辑"""
    doc = fitz.open(pdf_path)
    page = doc[0]  # 获取第一页
    
    # 添加文本
    point = fitz.Point(100, 100)  # 文本位置
    page.insert_text(
        point,
        "这是添加的文本",
        fontsize=12,
        color=(0, 0, 1),  # RGB颜色，蓝色
        fontname="china-s"  # 中文字体
    )
    
    # 添加多行文本
    text_rect = fitz.Rect(50, 200, 400, 300)  # 文本区域
    page.insert_textbox(
        text_rect,
        "这是一个文本框\n支持多行文本\n可以自动换行",
        fontsize=10,
        align=fitz.TEXT_ALIGN_CENTER
    )
    
    # 搜索并替换文本（需要重新绘制）
    text_instances = page.search_for("原文本")
    for inst in text_instances:
        # 用白色矩形覆盖原文本
        page.draw_rect(inst, color=(1, 1, 1), fill=(1, 1, 1))
        # 添加新文本
        page.insert_text(inst.tl, "新文本", fontsize=12)
    
    doc.save(output_path)
    doc.close()

# ===== 3. 图形和注释 =====
def graphics_operations(pdf_path, output_path):
    """添加图形和注释"""
    doc = fitz.open(pdf_path)
    page = doc[0]
    
    # 绘制矩形
    rect = fitz.Rect(100, 100, 200, 150)
    page.draw_rect(rect, color=(1, 0, 0), width=2)  # 红色边框
    
    # 绘制填充矩形
    page.draw_rect(rect, color=(0, 1, 0), fill=(0, 1, 0, 0.3))  # 半透明绿色填充
    
    # 绘制圆形
    center = fitz.Point(300, 200)
    page.draw_circle(center, 30, color=(0, 0, 1), width=3)
    
    # 绘制线条
    start_point = fitz.Point(50, 50)
    end_point = fitz.Point(150, 100)
    page.draw_line(start_point, end_point, color=(1, 0, 1), width=2)
    
    # 添加注释
    highlight_rect = fitz.Rect(100, 300, 300, 320)
    annot = page.add_highlight_annot(highlight_rect)
    annot.set_colors(stroke=(1, 1, 0))  # 黄色高亮
    annot.update()
    
    # 添加文本注释
    point = fitz.Point(400, 400)
    text_annot = page.add_text_annot(point, "这是一个注释")
    text_annot.set_info(title="作者", content="注释内容详细说明")
    text_annot.update()
    
    doc.save(output_path)
    doc.close()

# ===== 4. 图片操作 =====
def image_operations(pdf_path, output_path, image_path):
    """插入和处理图片"""
    doc = fitz.open(pdf_path)
    page = doc[0]
    
    # 插入图片
    img_rect = fitz.Rect(50, 50, 250, 200)  # 图片位置和大小
    page.insert_image(img_rect, filename=image_path)
    
    # 或者从字节数据插入图片
    with open(image_path, "rb") as f:
        img_data = f.read()
    page.insert_image(img_rect, stream=img_data)
    
    # 提取页面中的图片
    img_list = page.get_images()
    for i, img in enumerate(img_list):
        xref = img[0]  # 图片引用号
        pix = fitz.Pixmap(doc, xref)
        if pix.n - pix.alpha < 4:  # 确保是RGB或灰度图
            pix.save(f"extracted_image_{i}.png")
        pix = None
    
    doc.save(output_path)
    doc.close()

# ===== 5. PDF合并和分割 =====
def merge_split_operations():
    """PDF合并和分割"""
    
    # 合并PDF
    def merge_pdfs(pdf_list, output_path):
        merged_doc = fitz.open()
        for pdf_path in pdf_list:
            doc = fitz.open(pdf_path)
            merged_doc.insert_pdf(doc)  # 插入整个PDF
            doc.close()
        merged_doc.save(output_path)
        merged_doc.close()
    
    # 分割PDF
    def split_pdf(pdf_path, output_dir):
        doc = fitz.open(pdf_path)
        for i in range(doc.page_count):
            new_doc = fitz.open()
            new_doc.insert_pdf(doc, from_page=i, to_page=i)
            new_doc.save(f"{output_dir}/page_{i+1}.pdf")
            new_doc.close()
        doc.close()
    
    # 提取特定页面
    def extract_pages(pdf_path, pages, output_path):
        doc = fitz.open(pdf_path)
        new_doc = fitz.open()
        for page_num in pages:
            new_doc.insert_pdf(doc, from_page=page_num, to_page=page_num)
        new_doc.save(output_path)
        new_doc.close()
        doc.close()

# ===== 6. 水印和背景 =====
def watermark_operations(pdf_path, output_path):
    """添加水印和背景"""
    doc = fitz.open(pdf_path)
    
    for page_num in range(doc.page_count):
        page = doc[page_num]
        
        # 文字水印
        page_rect = page.rect
        center = page_rect.center
        
        # 旋转文字水印
        text_rect = fitz.Rect(center.x - 100, center.y - 20, 
                             center.x + 100, center.y + 20)
        
        # 设置透明度和旋转
        page.insert_textbox(
            text_rect,
            "机密文档",
            fontsize=36,
            color=(0.8, 0.8, 0.8),  # 浅灰色
            align=fitz.TEXT_ALIGN_CENTER,
            rotate=45  # 旋转45度
        )
        
        # 图片水印
        # watermark_rect = fitz.Rect(page_rect.width - 150, 20, 
        #                           page_rect.width - 20, 100)
        # page.insert_image(watermark_rect, filename="watermark.png")
    
    doc.save(output_path)
    doc.close()

# ===== 7. 完整编辑示例 =====
def comprehensive_edit_example():
    """综合编辑示例"""
    # 创建新PDF
    doc = fitz.open()
    
    # 添加第一页
    page1 = doc.new_page()
    
    # 添加标题
    title_rect = fitz.Rect(50, 50, 550, 100)
    page1.insert_textbox(
        title_rect,
        "PDF编辑示例文档",
        fontsize=24,
        align=fitz.TEXT_ALIGN_CENTER,
        color=(0, 0, 0.8)
    )
    
    # 添加内容
    content_rect = fitz.Rect(50, 120, 550, 400)
    content = """
    这是使用PyMuPDF创建的示例PDF文档。
    
    主要功能包括：
    • 文本编辑和格式化
    • 图形绘制
    • 图片插入
    • 注释添加
    • 页面管理
    """
    
    page1.insert_textbox(
        content_rect,
        content,
        fontsize=12,
        align=fitz.TEXT_ALIGN_LEFT
    )
    
    # 添加分隔线
    page1.draw_line(
        fitz.Point(50, 450),
        fitz.Point(550, 450),
        color=(0.5, 0.5, 0.5),
        width=1
    )
    
    # 添加页脚
    footer_rect = fitz.Rect(50, 780, 550, 800)
    page1.insert_textbox(
        footer_rect,
        "第 1 页 - PyMuPDF编辑示例",
        fontsize=10,
        align=fitz.TEXT_ALIGN_CENTER,
        color=(0.6, 0.6, 0.6)
    )
    
    # 保存文档
    doc.save("comprehensive_example.pdf")
    doc.close()
    print("综合示例PDF已创建：comprehensive_example.pdf")

# 使用示例
if __name__ == "__main__":
    # 运行综合示例
    comprehensive_edit_example()
    
    # 其他操作示例（需要提供实际的PDF文件路径）
    # page_operations("input.pdf", "output_pages.pdf")
    # text_operations("input.pdf", "output_text.pdf")
    # graphics_operations("input.pdf", "output_graphics.pdf")