# Anagram_search
This program takes a user-specified string and reads through the EnglishWords.txt file to check if the string is an anagram of any words found in the text file.

First, the main function asks the user for a word.

Then, it trys to read through the EnglishWords.txt file. It will print an error message if it cannot find the text file or no anagrams for the user-specified string were found.

Once it finds and reads the text file, it will remove any newline characters and add each line into a text string list.

Afterwards, it will loop through the text list and look for the string "START". This will be where all the matching words are found.

When "START" is found, the rest_of_file string list will be updated with the words starting from the position of "START".

Then it will loop through the rest of the file to check for anagrams of the user-specified string:
- The string and current file word will be sorted in alphabetical order, converted to lowercase, and compared for equality.
- If they are equal, the file word is added into the anagrams list.
- This will continue for all the remaining lines of the text file.

After all possible anagrams are found, the list is sorted and returned to the main funcion.
