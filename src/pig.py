def toEnglish(s):
    sentence = s.split(" ")
    english = ""
    for word in sentence:
        if word[:len(word) - 4:-1] == 'yaw':
            english += word[:len(word) - 3] + " "
        else: 
            noay = word[:len(word) - 2]
            firstconsonants = noay.split("a")[-1]
            print(noay)
            consonantsremoved = noay[:len(noay) - (len(firstconsonants)+1)]
            print((len(firstconsonants)+1))
            english += firstconsonants[-1] + consonantsremoved + " "
    return english.lower()

print(toEnglish("Avehay away icenay ayday"))