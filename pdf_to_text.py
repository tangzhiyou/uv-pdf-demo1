import fitz  # PyMuPDF
import os
import sys

def pdf_to_text(pdf_path, output_dir="output"):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    try:
        document = fitz.open(pdf_path)
    except fitz.FileNotFoundError:
        print(f"Error: PDF file not found at {pdf_path}")
        return
    except Exception as e:
        print(f"Error opening PDF: {e}")
        return

    print(f"Processing {document.page_count} pages from {pdf_path}...")

    for page_num in range(document.page_count):
        page = document.load_page(page_num)
        text = page.get_text("text")

        output_filename = os.path.join(output_dir, f"page_{page_num + 1}.txt")
        with open(output_filename, "w", encoding="utf-8") as f:
            f.write(text)
        print(f"Page {page_num + 1} extracted to {output_filename}")

    document.close()
    print("PDF processing complete.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python pdf_to_text.py <path_to_pdf_file> [output_directory]")
        sys.exit(1)

    input_pdf_path = sys.argv[1]
    output_directory = sys.argv[2] if len(sys.argv) > 2 else "output"

    pdf_to_text(input_pdf_path, output_directory)