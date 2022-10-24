def replaceSymbols(string):
    for char in string:
        if char in "~!@#$%^&()[]{},+-*|/?<>'.;:\"":
            string = string.replace(char, ' ')
    return string        

def counts(string):
    wordlist = string.split()
    for word in wordlist:
        if word in result:
            result[word] = result[word] + 1
        else:
            result[word] = 1

fileObject = open("PPAP.txt", "r")
song = fileObject.read()
fileObject.close()

result = {}
tmp = replaceSymbols(song.lower())
counts(tmp)

print(result)


