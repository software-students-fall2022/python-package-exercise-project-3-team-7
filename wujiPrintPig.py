def PrintPig(isFollowingBox):
    #Use this variable to determine if we want the to \ or not
    if(isFollowingBox):
        print("\            __,---.__")
        print(" \      __,-'         `-.")
    else:
        print("             __,---.__")
        print("        __,-'         `-.")
    print("       /_ /_,'           \&")
    print("       _,'''              \"")
    print("      ('')            .    |")
    print("         ``--|__|--..-'`.__|")


def PrintBox(toPrint):
    
    upper="   "
    lower="   "
    for x in toPrint:
        upper+="-"
        lower+="-"
        
    #print the upper box
    print(upper+"   ")
    
    #print the content
    toPrint="< "+toPrint+" >"
    print(toPrint);

    #print the lower box
    print(lower+"   ")


PrintBox("I love Bryan")    
PrintPig(True)





