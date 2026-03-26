from pypdf import PdfReader

# ================================
# 1. Load the PDF
# ================================
pdf_path = "kaustubh_resume.pdf"   # Change this to your PDF file name

reader = PdfReader(pdf_path)

# ================================
# 2. Count pages
# ================================
num_pages = len(reader.pages)
print(f"📄 Total Pages: {num_pages}")

# ================================
# 3. Extract text from each page
# ================================
full_text = ""

for i, page in enumerate(reader.pages):
    text = page.extract_text()
    print(f"\n--- Page {i+1} ---")
    
    if text:
        print(text[:1000])   # print first 500 characters for preview
        full_text += text + "\n"
    else:
        print("No text found on this page.")

# ================================
# 4. Save extracted text to file
# ================================
with open("extracted_text.txt", "w", encoding="utf-8") as file:
    file.write(full_text)

print("\n✅ Full PDF text extracted and saved to extracted_text.txt")

print(f"\n📝 Total extracted characters: {len(full_text)}")