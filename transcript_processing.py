import platform
import os

if platform.system() == "Windows":
    BACKSLASH = "\\"
else:
    BACKSLASH = "/"
    
# the directory containing files to analyze
INPUT_DIR = f"romanized_transcripts{BACKSLASH}"

FILENAMES = os.listdir(INPUT_DIR)

texts = {}
ik_counts = {}

# extract texts from files and index them by speaker
for file_name in FILENAMES:
    # macOS compatibility
    if not file_name.startswith("."):
        # use the filename as a key instead
        file_prefix = file_name.split(".")[0] #
        file = open(f"{INPUT_DIR}{file_name}")
        new_text = file.read()
        texts[file_prefix] = new_text
        file.close()

for key_name in texts:
    current_text = texts[key_name]
    current_words = current_text.split()
    new_text = ""

    ik_counts[key_name] = 0

    for word in current_words:
        if word == "Ik":
            new_text += "Ek"
            ik_counts[key_name] += 1
        elif word == "ik":
            new_text += "ek"
            ik_counts[key_name] += 1
        else:
            new_text += word 
        new_text += " "

    new_text = new_text.strip()

    output = open(f"corrected_romanized_transcripts{BACKSLASH}{key_name}.txt", "w")
    output.write(new_text)
    output.close()

output = open(f"correction_records{BACKSLASH}ik_counts.txt", "w")
for key_name in ik_counts:
    output.write(f"{key_name}:{ik_counts[key_name]}\n")
output.close()


