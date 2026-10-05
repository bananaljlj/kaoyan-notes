import fitz  # PyMuPDF

pdf_path = "c:/lessons/考研数学/线代/线代基础12.pdf"
doc = fitz.open(pdf_path)

print(f"总页数: {len(doc)}")
print("=" * 80)

for page_num in range(len(doc)):
    page = doc[page_num]
    text = page.get_text("text")
    print(f"\n{'='*40} 第 {page_num+1} 页 {'='*40}")
    print(text)

doc.close()
