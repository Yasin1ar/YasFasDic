import requests as rq
from sys import argv


def main(word: str) -> None:
    API = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    res = rq.get(API).json()[0]

    def get_phonetic(given_list: list) -> str:
        for i in range(len(given_list)):
            if "text" in given_list[i].keys():
                return given_list[i]["text"]

    try:
        definition = res["meanings"][0]["definitions"][0]["definition"]
        partOfSpeech = res["meanings"][0]["partOfSpeech"]
        phonetic = get_phonetic(res["phonetics"])
        word_itself = res["word"]
    except:
        print(f"The Word '{word}' not found in the dictionary")
        return None

    print("\n" * 2)
    print("-" * 50)

    print("The Word : ", word_itself)
    print("Definition : ", definition)
    print("Part Of Speech : ", partOfSpeech)
    print("Pronunciation", phonetic)

    print("-" * 50)
    print("\n" * 2)


if __name__ == "__main__":
    print(
        "\n Welcome to YasFasDic, Insert anything to get the definition\n Enter nothing"
        " to exit the program ",
        end="\n" * 5,
    )

    if len(argv) > 1:
        for arg in argv[1:]:
            main(arg)

    while True:
        words = input("Please Enter a word or phrase :>> ")
        if words == "":
            exit()
        words = words.strip().split(" ")
        for word in words:
            main(word.strip())