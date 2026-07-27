import asyncio
import edge_tts

async def speak():
    with open("myfile.txt", "r", encoding="utf-8") as f:
        text = f.read()

    communicate = edge_tts.Communicate(text, "en-US-AriaNeural")

    async for chunk in communicate.stream():
        if chunk["type"] == "audio":
            # play audio chunk here
            pass

asyncio.run(speak())