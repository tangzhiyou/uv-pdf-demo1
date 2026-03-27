# PDF 转换示例

这个项目演示了两种不同的 PDF 文本转换方法：

## 1. 使用 PyMuPDF (Fitz)
这是一个快速且轻量级的方式，用于从 PDF 中提取纯文本。

**特点：**
- 速度极快。
- 依赖少。
- 适合简单的文本提取。

**用法：**
```bash
python pdf_to_text.py <pdf_path> [output_dir]
```

## 2. 使用 IBM Docling
这是一个更高级的文档转换工具，能够处理复杂的文档结构（如表格、多列布局、重排等），并生成结构良好的 Markdown。

**特点：**
- **结构保持：** 能够识别标题、列表和表格。
- **多格式导出：** 支持 Markdown 和 JSON。
- **AI 驱动：** 使用深度学习模型理解页面布局。
- **适合 RAG：** 生成的 Markdown 非常适合 LLM 处理。

**用法：**
```bash
python pdf_to_docling.py <pdf_path> [output_dir]
```

### 安装依赖
如果使用 `uv`，可以运行：
```bash
uv sync
```
或者使用 `pip`：
```bash
pip install docling pymupdf
```

*注意：Docling 依赖较多（包括 PyTorch），首次安装可能需要一点时间。*
