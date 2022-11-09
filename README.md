![example workflow](https://github.com/software-students-fall2022/python-package-exercise-project-3-team-7/actions/workflows/build.yaml/badge.svg)

[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-c66648af7eb3fe8bc4f294546bfd86ef473780cde1dea487d3c4ff354943c9ae.svg)](https://classroom.github.com/online_ide?assignment_repo_id=9126635&assignment_repo_type=AssignmentRepo)
# Python Package Exercise

A little exercise to create a Python package, build it, test it, distribute it, and use it. See [instructions](./instructions.md) for details.

## Group members
- [Maaz Ahmed](https://github.com/maazahmedd)
- [Hillary Davis](https://github.com/hillarydavis1)
- [Wuji Cao](https://github.com/cwj2099)
- [Ankit Jain](https://github.com/ankit181818)

# Functions in our package

> ## Our Pig Latin Translation Rules:
    Our rules for pig latin are as follows: take away the first letter of a word, then add a new word that uses the first letter of the word with "ay" added to it e.g., hello becomes ello-hay. For words that start with a vowel, you add "ay" to the end of the word e.g., enter becomes enter-ay, for words that start with a consonant, all letters are removed until a vowel is reached and then all removed consonants are used to create a second word, with "ay" added to the end of it e.g., happy becomes appy-hay

### toEnglish(string s):
This function **takes pig Latin words as input**. These words must be hyphenated at the end with their pig latin translation/addition in order for our system to be able to process them properly. As a result it returns **the english translation** to the user.

### toPl(string s, boolean intermediate_output_flag = True):
This function takes **an english word** as input and returns this word in **our pig latin translation** of it. In the case of an intermediate flag set to True (as is default) it will return the word in its hyphenated format. Otherwise it will return the word without hyphenation.

### process_input(string s, boolean translation_flag):
Function that takes in a **an input string and a flag corresponding to the type of translation** and returns a **parsed usable list**, depending on the type of translation needed. Also prints useful output for debugging / running.

When we call this function, we can make sure that it returns a non-empty list by checking the len().

### speech_bubble(string message):
**arguments:** one argument, message
**returns:** a string that is essentially ASCII art, with the message enclosed in a speech bubble

### arrow_to_bubble():
**no arguments**
**returns:** a string that represents ASCII art, pointing to the speech bubble

### print_pig():
**no_arguments**
**returns:** a string that represents ASCII art of a pig

### print_everything(message):
**arguments:** one argument, message
**returns:** a string that represents ASCII art, with a speech bubble enclosing the message, a pig and an arrow pointing from the pig to the speech bubble
<hr>

We believe that the functions most useful to potential users are (with their use shown in the example file)
 - toEnglish
 - toPL
 - speech_bubble
 - print_pig
 - print_everything



