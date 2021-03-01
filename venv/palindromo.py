

def convertInputString():

    rawInput = input("\ndame palabra, sentencia o frase \npara verificar si es un palidromo: ")
    rawString = rawInput.lower()
    rawList = list(rawString)
    return rawList


def stripAnalphabetics(dirtyList):
    analphabeticList = [" ", "-", ".", ",", ":", ";", "!", "?", "'", "\""]
    for character in analphabeticList:
        if character in dirtyList:
            dirtyList.remove(character)
            return stripAnalphabetics(dirtyList)
    return dirtyList

def runPalindromeCheck(straightList):
    reversedList = straightList[::-1]
    if reversedList == straightList:
        return "el texto escrito es un palindromo!"
    else:
        return "el texto escrito no es un palindromo."

def main():
    print("\nvalidador de palinfromo")
    originalList = convertInputString()
    originalList = stripAnalphabetics(originalList)
    palindromeCheck = runPalindromeCheck(originalList)
    print(palindromeCheck)

main()
