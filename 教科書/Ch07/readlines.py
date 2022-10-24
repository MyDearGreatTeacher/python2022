fileObject = open("poem.txt", "r")

content = fileObject.readlines()
for line in content:
    print(line)

fileObject.close()



