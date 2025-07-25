
fitz is a prefix of name, meaning "son of", in memory of one of the early developers.
`pip install pymupdf`. PyMuPDF: python, minimal/micro (fast),PDF.


# PyMuPDF PDF编辑功能讲解 (Claude Sonnet 4)

## 编辑思路

PyMuPDF的PDF编辑遵循以下基本思路：
1. **加载文档** → **定位页面** → **执行操作** → **保存文档**
2. 所有编辑操作都是对Document对象和其Page对象进行的
3. 编辑后需要保存才能持久化更改## 核心编辑思路总结

**1. 文档结构操作**
- **页面管理**：增删改页面，复制移动页面
- **文档合并**：多个PDF合并为一个
- **文档分割**：一个PDF拆分为多个

**2. 内容编辑**
- **文本操作**：添加文本、文本框，搜索替换
- **图形绘制**：矩形、圆形、线条等基本图形
- **图片处理**：插入图片、提取图片

**3. 增强功能**
- **注释系统**：高亮、文本注释、形状注释
- **水印处理**：文字水印、图片水印
- **格式控制**：字体、颜色、对齐方式

## 编辑流程要点

1. **坐标系统**：PDF使用点坐标系（左下角为原点），但PyMuPDF使用左上角为原点
2. **颜色表示**：RGB值范围0-1，如`(1, 0, 0)`表示红色
3. **资源管理**：编辑后必须调用`save()`保存，`close()`释放资源
4. **批量操作**：可以遍历所有页面进行批量编辑

这样你就可以根据需要选择相应的编辑功能，从简单的文本添加到复杂的文档重构都能实现。