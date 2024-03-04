import platform
import os
import stanza

#stanza.download('hi')
nlp = stanza.Pipeline('hi') # initialize English neural pipeline

#doc = nlp("इराक के विदेश मंत्री ने अमरीका के उस प्रस्ताव का मजाक उड़ाया है , जिसमें अमरीका ने संयुक्त राष्ट्र के प्रतिबंधों को इराकी नागरिकों के लिए कम हानिकारक बनाने के लिए कहा है ।") # run annotation over a sentence

#doc = nlp("एक गाँव में एक लड़की रहती थी। उसकी दादी ने उसके लिए एक लाल कोट बनाया था। तबसे उसका नाम 'रेड रिडिंग हुड' बन गया। एक दिन रेड रिडिंग हुड की माँ ने उसको खाना दिया और बोला कि अपनी दादी के घर चले जाओ। दादी का घर जंगल के उस पार था। जब वह जंगल से जा रही थी, उसको एक भेड़िये ने देखा। और उसको पकड़ने लगा पर वहाँ एक लकड़हारा आकर, लकड़खारे ने भेड़िये को भगा दिया। भेड़िया दूसरी तरफ से जाकर उसकी दादी के घर चला गया और अंदर जाकर उसकी दादी को खा लिया और दादी की जगह मंजे पे लेट गया। जब रेड रिडिंग हुड आई तो उसने मेज पे खाना लगाया और दादी को बोला 'उठो'। उसने दादी के कान देखे और बोली, 'दादी, आपके कितने बड़े कान हैं।' इकदम भेड़िया मंजे से उठा और रेड रिडिंग हुड को पकड़ने के लिए लपका, पर क्योंकि उसका पेट इतना मोटा था, दादी थी अंदर तो वह गिर गया। इतनी देर में लकड़हारा आया। लकड़खारे ने कैंची से उसका पेट काट दिया और दादी को बीच में से निकाल दिया। उसकी जगह उसने खूब सारे पत्थर भर दिए पेट में और ऊपर से सी दिया तो बेचारा भेड़िया अपना मोटा पेट लेकर जा रहा था और वह कुए में गिर के मर गया। फिर दादी और रेड रिडिंग और लकड़हारा खूब खुश हुए और खाना खा के वह अपने घर चल पड़े।")

#print(doc.entities)


if platform.system() == "Windows":
    BACKSLASH = "\\"
else:
    BACKSLASH = "/"
    
# the directory containing files to analyze
INPUT_DIR = f"indicized_transcripts{BACKSLASH}"
OUTPUT_DIR = f"tagged_transcripts{BACKSLASH}"

FILENAMES = os.listdir(INPUT_DIR)

texts = {}


# extract texts from files and index them by speaker
for file_name in FILENAMES:
    # macOS compatibility
    if not file_name.startswith("."):
        # use the filename as a key instead
        file_prefix = file_name.split(".")[0] #
        file = open(f"{INPUT_DIR}{file_name}")
        doc = nlp(file.read())
        file.close()

        tagged_text = ""
        for sentence in doc.sentences:
            for word in sentence.words:
                    tagged_text += f"{word.text}.{word.pos} "

        tagged_text.strip()
        output = open((f"{OUTPUT_DIR}{file_prefix}_tagged.txt"), "w")

        output.write(tagged_text)

        output.close()
        