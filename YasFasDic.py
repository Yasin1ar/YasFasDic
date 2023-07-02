import requests as rq
from sys import argv
import string

def main(word: str) -> None:
	# API URL for the dictionary API
	API = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
	# Get the response from the API
	try:
		res = rq.get(API).json()[0]
	except rq.exceptions.ConnectionError:
		print("Network Error, Please be sure that your network connection is valid.")
		return None
	except KeyError:
		print(f"There is no word '{word}' in the database dictionary!")
		return None

	# Function to get the phonetic of the given list
	def get_phonetic(given_list: list) -> str:
		for i in range(len(given_list)):
			if "text" in given_list[i].keys():
				return given_list[i]["text"]

	try:
		# Get the definition of the word
		definition = res["meanings"][0]["definitions"][0]["definition"]
		# Get the part of speech of the word
		partOfSpeech = res["meanings"][0]["partOfSpeech"]
		# Get the phonetic of the word
		phonetic = get_phonetic(res["phonetics"])
		# Get the word itself
		word_itself = res["word"]
	except:
		# If the word is not found in the dictionary, print the error message
		print(f"The Word '{word}' not found in the dictionary")
		return None

	# Print the output
	print("\n")
	print("\033[1m" + "The Word : " + word_itself + "\033[0m")
	print("-" * 50)
	print("Definition : ", definition)
	print("Part Of Speech : ", partOfSpeech)
	print("Pronunciation : ", phonetic)

	print("-" * 50)
	print("\n")


if __name__ == "__main__":
	# Print the welcome message
	print(
		"\033[1m" + "\nWelcome to YasFasDic, "
		"Insert anything to get the definition\nEnter nothing to exit the program "
		+ "\033[0m",
		end="\n" * 3,
	)

	# If there are more than one argument, loop through them
	if len(argv) > 1:
		for arg in argv[1:]:
			main(arg)

	# While loop to keep the program running
	while True:
		# Get the user input
		words = input("Please Enter a word or phrase :>> ")
		# If the user input is empty, exit the program
		if words == "":
			exit()
		# Split the user input into words
		words = words.strip().split(" ")
		unwanted_chars = "'/.~`!@#$%^&*()_+=-|\<>;:}{[]"
		words = [word.translate(str.maketrans("", "", unwanted_chars)) for word in words]
		# Loop through the words
		for word in words:
			# Call the main function with the word
			main(word.strip())
