def speech_bubble(message):
    result = "\n"
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

    result += " " + "-" * max_lines + "\n"
    for i in range(len(lines)):
        result += "(" + lines[i] + " " * (max_lines - len(lines[i])) + ")" + "\n"
    result += " " + "-" * max_lines

    return result

def arrow_to_bubble():
    result = "       \\\n"
    result += "        \\"

    return result

def print_pig():
    result = "         <`--'\>______" + "\n"
    result += "         /. .  `'     \\" + "\n"
    result += "        (`')  ,        @" + "\n"
    result += "         `-._,        /" + "\n"
    result += "            )-)_/--( >" + "\n"
    result += "           ''''  ''''" + "\n"
    return result


def print_everything():
    result = speech_bubble("Hello, my name is Foo. I am a great person.") + "\n"
    result += arrow_to_bubble() + "\n"
    result += print_pig()

    return result

# print(print_everything())
print(speech_bubble("Hello, my name is Foo."))
