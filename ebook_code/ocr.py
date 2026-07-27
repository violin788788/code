import easyocr

# Initialize the reader with desired languages (e.g., 'en' for English)
reader = easyocr.Reader(['en'])

# Extract text from an image
results = reader.readtext('shib.png')

# Print only the detected text strings
for detection in results:
    bounding_box = detection[0]
    text = detection[1]
    confidence = detection[2]
    print(f"Found text: {text} (Confidence: {confidence:.2f})")