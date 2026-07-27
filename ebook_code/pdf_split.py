
import os
import sys
from pypdf import PdfReader, PdfWriter
pdf_file_name = "cheka_fixed"
file = pdf_file_name
if ".pdf" not in pdf_file_name:
    file = pdf_file_name + ".pdf"
size_in_bytes = os.path.getsize(file)
size_in_mb = size_in_bytes / (1024 * 1024)
print(f"File size: {size_in_mb:.2f} MB")
max_mb = 50
if size_in_mb < max_mb:
    print("under 50mb")
    sys.exit()
new_files = int(size_in_mb / max_mb) + 1
print("new_files", new_files)
reader = PdfReader(file)
num_pages = len(reader.pages)
pages_per_file = int(num_pages / new_files) + 1
print(f"Total pages: {num_pages}")
print("pages_per_file", pages_per_file)
base_name = os.path.splitext(file)[0]
for a in range(new_files):
    writer = PdfWriter()
    start_page = a * pages_per_file
    end_page = min(start_page + pages_per_file, num_pages)
    for page_num in range(start_page, end_page):
        writer.add_page(reader.pages[page_num])
    output_file = f"{base_name}_part{a+1}.pdf"
    with open(output_file, "wb") as f:
        writer.write(f)
    print(f"Created {output_file} ({end_page-start_page} pages)")
print("Done.")