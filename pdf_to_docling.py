import sys
import os
from docling.document_converter import DocumentConverter

def convert_pdf_to_markdown(pdf_path, output_dir="output"):
    """
    使用 IBM Docling 将 PDF 转换为 Markdown。
    Docling 能够更好地处理文档结构（如标题、列表、表格等）。
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # 初始化 DocumentConverter
    converter = DocumentConverter()
    
    print(f"正在使用 Docling 解析: {pdf_path}...")
    
    try:
        # 执行转换
        result = converter.convert(pdf_path)
        
        # 导出为 Markdown
        markdown_content = result.document.export_to_markdown()
        
        # 解析文件名
        base_name = os.path.splitext(os.path.basename(pdf_path))[0]
        output_filename = os.path.join(output_dir, f"{base_name}_docling.md")
        
        # 写入文件
        with open(output_filename, "w", encoding="utf-8") as f:
            f.write(markdown_content)
            
        print(f"成功将 PDF 转换为 Markdown: {output_filename}")
        
    except Exception as e:
        print(f"解析过程中出现错误: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("用法: python pdf_to_docling.py <pdf_文件路径> [输出目录]")
        sys.exit(1)

    input_pdf_path = sys.argv[1]
    output_directory = sys.argv[2] if len(sys.argv) > 2 else "output"

    convert_pdf_to_markdown(input_pdf_path, output_directory)
