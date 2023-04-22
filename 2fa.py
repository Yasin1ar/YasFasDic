from translate import Translator
from sys import argv
import requests as rq
word = 'hello'
API = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
res = rq.get(API).json()
try:
    definition = res[0]["meanings"][0]["definitions"][0]["definition"]
    print(definition)
    partOfSpeech = res[0]["meanings"][0]["partOfSpeech"]
    print(partOfSpeech)
    def get_phonetic(given_list:list) -> str:
        for i in range(len(given_list)):
            if "text" in given_list[i].keys():
                return given_list[i]["text"]
    phonetic = get_phonetic(res[0]["phonetics"])
    print(phonetic)
except:
    print(f"The Word '{word}' not found in the dictionary")
    exit()

        


exit()
translator = Translator(to_lang="fa")

if len(argv) > 1:
    args = "   ".join(argv[1:])
    print(translator.translate(args))

else:
    print(
        "\n Welcome to 2fa Translator, Insert anything to translate into Farsi/Persian\n Enter nothing"
        " to exit the program ",
        end="\n" * 10,
    )
    while True:
        t = input("\n Insert anything to translate into Farsi : ")
        if t == "":
            exit()
        print()
        print("  " + translator.translate(t))
