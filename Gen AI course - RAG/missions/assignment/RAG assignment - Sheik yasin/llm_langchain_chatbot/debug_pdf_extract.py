from pdf_processor import load_all_pdfs

texts = load_all_pdfs()

print("\n Total pages extracted:", len(texts))
print("\nFirst 1000 characters of PDF:")
print(texts[0][:1000])