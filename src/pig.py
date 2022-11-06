import string

def toEnglish(sentence):
    english = ""
    for word in sentence:
        trans = word.split("-")
        noay =  trans[1]
        english += noay[:len(noay) - 2]+ str(trans[0]) + " "
    return english.lower()



def toPL(s):
    return



#Function to parse the input string to a usable list, depending on the 
#type of translation needed. Also prints useful output for debugging / running
#Takes in the user's input string and a flag corresponding to the type of translation

#when we call this, we can make sure that it returns a list with something in it by checking the len()
def process_input(s, translation_flag):
    
    for punc in string.punctuation:
        if punc != "-":
            s = s.replace(punc, '') #remove all punctation except the hyphens, helps w edge cases

    if len(s) < 1:
        print("There's nothing to translate from your message: ", s)
        return [] #helps us avoid the case where someone just submitted all punctuation
    
    #a flag for deciding if we're translating english --> latin or vice versa
    if translation_flag.lower() == "e": #I've decided that "e" means "translate to english"
        if "-" not in s:
            print("Every Pig Latin word needs a hyphen, so we can translate it effectively")
            return []
        else:
            return s.split(" ")
    elif translation_flag.lower() == "p": # "p" means "translate to pig latin"
        return s.split(" ")
    
    else:
        print("Invalid translation flag entered: ", translation_flag)
        return []