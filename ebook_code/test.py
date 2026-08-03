


from utils import *
import asyncio
import edge_tts


from pathlib import Path

# 1. Define the original file path
file_path = Path("document.txt")

# 2. Generate the new path with the updated suffix
new_path = file_path.with_suffix(".pdf")


print(new_path)
sys.exit()

# 3. Rename the file on the actual hard drive
if file_path.exists():
    file_path.rename(new_path)
    print(f"Renamed to: {new_path}")

"""
file = "french_revolution.txt"
len_portion = 55000


text = read_txt(file)
word_list = text.split()
len_text = len(text)
print(len_text)
print(len(word_list))

print(len_text/len(word_list))
#print(word_list)


#sys.exit()

parts = math.ceil(len_text/len_portion)
print(parts)

VOICE = "en-US-AndrewNeural"

for a in range(0,parts):
    portion = text[a*len_portion:(a+1)*len_portion]
    output_file = file.replace(".txt","")+"_part"+str(a+1)+".mp3"
    print(output_file)
    async def generate_tts():
        # Initialize the communicate object
        communicate = edge_tts.Communicate(portion, VOICE)
        # Save the generated speech to an MP3 file
        await communicate.save(output_file)
        print(f"Audio successfully saved to {output_file}")
    # Run the async function
    asyncio.run(generate_tts())
    #os.startfile(output_file)

"""