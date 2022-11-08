import pig

def menu():
    """Prompt user menus """
    print("Welcome to the best pig latin translator!")
    print("1. Translate from English to Pig Latin")
    print("2. Translate from Pig Latin to English (hyphenating pig latin portion)")
    print("3. Exit")
def main():
    choice = ""
    while choice != "3":
        menu()
        choice = input("Enter your choice (1 - 3): ")
        if choice == "1":
            word = ""
            word = input("Enter English word: ")
            word = pig.toPL(word, True)
            pig.speech_bubble(word)
            pig.arrow_to_bubble()
            pig.print_pig()
        elif choice == "2":
            word = ""
            word = input("Enter Pig Latin word (hyphenate the pig latin portion): ")
            p_word = pig.toEnglish(word)
            pig.speech_bubble(p_word)
            pig.arrow_to_bubble()
            pig.print_pig()
        elif choice == "3":
            print("Oodgay yebay!\n")
        else:
            print("Invalid choice. Please try again or enter 3 to exit.\n")

if __name__ == '__main__':
    main()