fileObject = open("poem.txt", "r")

line = fileObject.readline()
while line != '':
    print(line)
    line = fileObject.readline()

fileObject.close()



