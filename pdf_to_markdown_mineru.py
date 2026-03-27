import os
import sys
from magic_pdf.pdf_parse_union_core_v2 import PDFParser

def pdf_to_markdown_mineru(pdf_path, output_dir="output_markdown"):
    """
    Converts a PDF file to Markdown format using MinerU (magic-pdf).

    Args:
        pdf_path (str): The path to the input PDF file.
        output_dir (str): The directory where the output Markdown will be saved.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    try:
        parser = PDFParser()
        parser.parse(pdf_path, output_dir)
        print(f"PDF '{pdf_path}' processed with MinerU. Output saved to '{output_dir}'")
    except Exception as e:
        print(f"Error processing PDF with MinerU: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python pdf_to_markdown_mineru.py <path_to_pdf_file> [output_directory]")
        sys.exit(1)

    input_pdf_path = sys.argv[1]
    output_directory = sys.argv[2] if len(sys.argv) > 2 else "output_markdown"

    pdf_to_markdown_mineru(input_pdf_path, output_directory)