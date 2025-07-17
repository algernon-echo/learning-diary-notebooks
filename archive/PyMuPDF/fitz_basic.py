# Claude Sonnet 4

# PyMuPDF Document对象的主要属性和方法示例

import fitz

# 打开PDF文件后得到的mypdf对象结构
def explore_pdf_document(pdf_path):
    mypdf = fitz.open(pdf_path)
    
    print("=== Document对象主要属性 ===")
    print(f"页面总数: {mypdf.page_count}")
    print(f"文件名: {mypdf.name}")
    print(f"是否需要密码: {mypdf.needs_pass}")
    print(f"是否已加密: {mypdf.is_encrypted}")
    print(f"PDF版本: {mypdf.pdf_version()}")
    
    print("\n=== 元数据信息 ===")
    metadata = mypdf.metadata
    for key, value in metadata.items():
        print(f"{key}: {value}")
    
    print("\n=== 文档大纲/书签 ===")
    outline = mypdf.get_toc()  # 获取目录/书签
    for item in outline[:5]:  # 只显示前5个
        print(f"层级{item[0]}: {item[1]} (页码: {item[2]})")
    
    print("\n=== 页面对象示例 (第一页) ===")
    if mypdf.page_count > 0:
        first_page = mypdf[0]  # 获取第一页
        print(f"页面尺寸: {first_page.rect}")
        print(f"页面旋转角度: {first_page.rotation}")
        print(f"媒体框: {first_page.mediabox}")
        print(f"裁剪框: {first_page.cropbox}")
    
    # 关闭文档
    mypdf.close()

# Document对象的常用方法和属性结构图
"""
fitz.Document对象 (mypdf)
├── 基本属性
│   ├── page_count          # 页面总数
│   ├── name               # 文件路径/名称
│   ├── is_closed          # 是否已关闭
│   ├── needs_pass         # 是否需要密码
│   └── is_encrypted       # 是否加密
│
├── 元数据方法
│   ├── metadata           # 文档元数据字典
│   ├── pdf_version()      # PDF版本
│   └── get_toc()          # 获取目录/书签
│
├── 页面访问
│   ├── [页码]             # 通过索引访问页面
│   ├── load_page(n)       # 加载指定页面
│   └── pages()            # 页面迭代器
│
├── 文本提取
│   ├── get_page_text(n)   # 获取指定页面文本
│   └── scrub()            # 清理敏感信息
│
├── 文档操作
│   ├── save()             # 保存文档
│   ├── insert_pdf()       # 插入其他PDF
│   ├── delete_page()      # 删除页面
│   └── close()            # 关闭文档
│
└── 页面对象 (page = mypdf[n])
    ├── rect               # 页面矩形区域
    ├── rotation           # 旋转角度
    ├── mediabox           # 媒体框
    ├── cropbox            # 裁剪框
    ├── get_text()         # 提取文本
    ├── get_images()       # 获取图片
    ├── search_for()       # 搜索文本
    └── get_links()        # 获取链接
"""

# 改进版的文本提取函数
def extract_text_from_pdf_improved(pdf_path):
    """
    改进版PDF文本提取函数，添加了错误处理和更多选项
    """
    try:
        mypdf = fitz.open(pdf_path)
        all_text = ""
        
        print(f"正在处理PDF: {mypdf.name}")
        print(f"总页数: {mypdf.page_count}")
        
        for page_num in range(mypdf.page_count):
            page = mypdf[page_num]
            
            # 多种文本提取方式
            # text = page.get_text("text")      # 纯文本
            # text = page.get_text("html")      # HTML格式
            # text = page.get_text("dict")      # 字典格式（包含字体信息）
            # text = page.get_text("json")      # JSON格式
            text = page.get_text("text")
            
            if text.strip():  # 只添加非空文本
                all_text += f"\n--- 第 {page_num + 1} 页 ---\n"
                all_text += text
                all_text += "\n"
            
            print(f"已处理页面: {page_num + 1}/{mypdf.page_count}")
        
        mypdf.close()  # 重要：关闭文档释放资源
        return all_text
        
    except Exception as e:
        print(f"处理PDF时出错: {e}")
        return ""

# 使用示例
if __name__ == "__main__":
    pdf_file = "example.pdf"  # 替换为实际PDF文件路径
    
    # 基础用法
    text_content = extract_text_from_pdf_improved(pdf_file)
    
    # 保存提取的文本到文件
    with open("extracted_text.txt", "w", encoding="utf-8") as f:
        f.write(text_content)