from pdf2image import convert_from_path

# Convert all 200 pages directly to JPEG
convert_from_path('document.pdf', output_folder='extracted_images', fmt='jpeg')
