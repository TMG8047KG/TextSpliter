import sys

if len(sys.argv) > 1:
    file = open(sys.argv[1], "r")
if len(sys.argv) > 2:
    if sys.argv[2] == "\\n":
        splitText = file.read().split("\n")
        print("Split into " + str(len(splitText)) + " files.")
    else:
        splitText = file.read().split(sys.argv[2])
file.close()

i = 0
for text in splitText:
    newFile = open(str(i) + "_text.txt", "w")
    newFile.write(text)
    newFile.close()
    i=i+1