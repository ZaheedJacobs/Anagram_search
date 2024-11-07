# Print anagrams of a given word in alphabetical order

def are_anagrams(word_1: str, word_2: str)-> bool:
    # Compare 2 words to see if they are anagrams

    word_1 = sorted(word_1.lower())
    word_2 = sorted(word_2.lower())

    return word_1 == word_2

def find_all_anagrams(string: str)-> list[str]:
    # Find all anagrams within a text file

    text: list[str] = []
    anagrams: list[str] = []
    not_start: int = 0
    rest_of_file: list[str] = []

    # Read the file and split each line after removing newlines, then add them to the text list
    with open("EnglishWords.txt", "r") as f:
        for file_line in f:
            file_line = file_line.replace("\n", " ")
            text.append(file_line[:-1])

    # Iterate over the text list to find the position of "START"

    for text_pos in text:
        if text[text_pos] != "START":
            not_start += 1
            continue
        else:
            rest_of_file = text[text_pos:]
            break

    # Iterate over the rest of the file to find anagrams
    for line in rest_of_file:
        if are_anagrams(string, line):
            anagrams.append(line)

    # Sort the anagrams list
    anagrams.sort()
    return anagrams

def main():
    print("***** Anagram Finder *****")
    word = input("Enter a word: ")

    try:
        print(find_all_anagrams(word))

    except IOError as er_text:
        print("Sorry, could not find file 'EnglishWords.txt'.")
        print(er_text)

    except:
        print(f"Sorry, anagrams of \'{word}\' could not be found")

if __name__ == "__main__":
    main()
