def toEnglish(s):
    if "-" not in s:
        return s
    sentence = s.split(" ")
    english = ""
    for word in sentence:
        trans = word.split("-")
        noay =  trans[1]
        english += noay[:len(noay) - 2]+ str(trans[0])
    return english.lower()
