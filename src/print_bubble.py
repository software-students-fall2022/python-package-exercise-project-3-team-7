def speech_bubble(message):
    print()
    words = message.split(" ")
    
    lines = []

    words_per_line = 7
    line = ""
    max_lines = 0
    for i in range(len(words)):
        # append the current line to lines if max number of words in line is reached
        if (i % words_per_line == 0 and i != 0):
            lines.append(line)
            line = ""

        # if new line, start without a space
        if i % words_per_line != 0:
            line += " " + words[i]
        else:
            line += words[i]

        # if (i == len(words) - 1 and i % words_per_line != 0):
        if (i == len(words) - 1):
            lines.append(line)

    for i in range(len(lines)):
        if len(lines[i]) > max_lines:
            max_lines = len(lines[i])

    print(" " + "-" * max_lines)
    for i in range(len(lines)):
        print("(" + lines[i] + " " * (max_lines - len(lines[i])) + ")")
    print(" " + "-" * max_lines)

def arrow_to_bubble():
    print("       \\")
    print("        \\")

def print_pig():
    # print()
    print("         <`--'\>______")
    print("         /. .  `'     \\")
    print("        (`')  ,        @")
    print("         `-._,        /")
    print("            )-)_/--( >")
    print("           ''''  ''''")
    print()



speech_bubble("Hello, my name is Maaz. I am a great person.")
arrow_to_bubble()
print_pig()