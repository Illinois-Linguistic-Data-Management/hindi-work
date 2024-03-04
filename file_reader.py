
import docx # must be python-docx for use with python 3

GARBAGE = ['', ',', '………………………………….', '………………………………………………………..', '……………………………………………………………………………………..',
           '………………………………………………………………………………………………………………………………………', 'Red Ridding Hood']

def load_data(filename):
    doc = docx.Document(filename)
    content = []
    for para in doc.paragraphs:
        content.append(para.text)
    return content

def process_data(data):
    cleaned_data = [datum for datum in data if datum not in GARBAGE]
    data_dict = {}
    # for i in range(0, len(cleaned_data), 2):
    #     data_dict[cleaned_data[i]] = cleaned_data[i+1]
    return cleaned_data

def get_text(file_name):
    return process_data(load_data(file_name))

if __name__ == "__main__":
    results = process_data(load_data("Red Ridding Hood Vandana.docx"))
    first = results.pop(1)
    results[1] = first + " " + results[1] # the first story is in two paragraphs
    results_dict = {}
    for i in range(len(results)): # populate dictionary with speaker names as keys, transcripts as values
        if i % 2 == 0:
            print(results[i])
            results_dict[results[i]] = ""
        else:
            results_dict[results[i-1]] = results[i]
    for i, key in enumerate((results_dict)):
        name = "_".join(key.lower().split())
        output = open((f"romanized_transcripts/{'0' if i < 9 else ''}{i+1}_{name}.txt"), "w")

        output.write(results_dict[key])

        output.close()
    print(len(results))
