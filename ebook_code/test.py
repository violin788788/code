from PIL import Image
import pytesseract

# Load your image
img = Image.open('your_image.png')

# Extract text
extracted_text = pytesseract.image_to_string(img)

print(extracted_text)