import fitz # PyMuPDF

def create_sample_pdf(filename="sample.pdf"):
    doc = fitz.open()  # new PDF
    page = doc.new_page()  # new page
    page.insert_text((72, 72), "This is page 1.", fontsize=12)

    page = doc.new_page()
    page.insert_text((72, 72), "This is page 2, with some more text.", fontsize=12)

    page = doc.new_page()
    page.insert_text((72, 72), "And this is the final page, page 3.", fontsize=12)

    doc.save(filename)
    doc.close()
    print(f"Created sample PDF: {filename}")

if __name__ == "__main__":
    create_sample_pdf("sample.pdf")
