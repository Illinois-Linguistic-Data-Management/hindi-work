from openai import OpenAI
import platform
import os

client = OpenAI(api_key="") # this must be valid in order to actually run this script!!

if platform.system() == "Windows":
    BACKSLASH = "\\"
else:
    BACKSLASH = "/"
    
# the directory containing files to analyze
INPUT_DIR = f"corrected_romanized_transcripts{BACKSLASH}"
OUTPUT_DIR = f"indicized_transcripts{BACKSLASH}"

FILENAMES = os.listdir(INPUT_DIR)


messages = [ {"role": "system", "content": "You have been asked to transliterate romanized Hindi text into Devanagari"}, None]

for name in FILENAMES:
    if not name.startswith("."):
        file = open(f"{INPUT_DIR}{name}")
        new_text = file.read()
        file.close()

        messages[1] = {"role": "user", "content": new_text}
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages)
        reply = completion.choices[0].message
        print(reply)
        output = open(f"{OUTPUT_DIR}{name}_indicized.txt", "w")
        output.write(reply.content)
        output.close()

# from openai import OpenAI

# example from openAI
# completion = client.chat.completions.create(
#   model="gpt-3.5-turbo",
#   messages=[
#     {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
#     {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
#   ]
# )

print(completion.choices[0].message)





