# Exercise 2
try:
    fhand = open("mbox-short.txt")
    for line in fhand:
        words = line.split()

        if len(words) < 3:
            continue
        if words[0] != "From":
            continue
        print(words[2])
except:
    print("Unable to open file! File may not exist in the directory")
    quit()
