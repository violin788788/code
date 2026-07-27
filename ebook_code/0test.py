import pyttsx3

# Create TTS engine
engine = pyttsx3.init()

# Set speech rate
engine.setProperty("rate", 150)

# Set volume (0.0 to 1.0)
engine.setProperty("volume", 1.0)

# Choose a voice (optional)
voices = engine.getProperty("voices")

for i, voice in enumerate(voices):
    print(i, voice.name)

# Pick a voice
engine.setProperty("voice", voices[0].id)

# Speak text
text = "Hello, this is a text to speech example using Python."

engine.say(text)

# Wait until speech finishes
engine.runAndWait()