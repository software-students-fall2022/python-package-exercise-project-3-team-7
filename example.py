from piglatinTeam7 import pig

#Converting English to PigLatin
print(pig.toPL("hello"))

#Convert PigLatin to English
print(pig.toEnglish("`ello-hay"))

#Print the CUTE pig
print(pig.print_pig())

#Print the speech bubble with a message in string
print(pig.speech_bubble("My name is foo"))

#Print ascii art with with a message and a CUTE pig
print(pig.print_everything("My name is Bart"))

#Using other internal funcstion as arguments to print diferent things
print(pig.speech_bubble(pig.toPL("hello")))
print(pig.print_everything(pig.toPL("hello")))
