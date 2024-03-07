def wordInRange():
    #Type your code here
    wordList = open(input(), 'r')
    min = str(input()).lower()
    max = str(input()).lower()
    word = wordList.readline()
    while word != "":
        strippedWord = word.strip("\n")
        if strippedWord.lower() >= min and strippedWord.lower() <= max:
            print(strippedWord + " - in range")
        else:
            print(strippedWord + " - not in range")
        word = wordList.readline()
    return
if __name__ == '__main__':
    wordInRange()