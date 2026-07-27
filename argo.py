from argotranslate import ArgoTranslate

# Initialize ArgoTranslate
translator = ArgoTranslate()

# Example: Translate English to French
source_text = "Hello, how are you?"
source_lang = 'en'  # Source language (English)
target_lang = 'fr'  # Target language (French)

# Translate
translated_text = translator.translate(source_text, source_lang, target_lang)

print("Translated Text:", translated_text)
