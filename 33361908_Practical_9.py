#cd c://programs python
#python 33361908_Practical_9.py

#Question 1
#Convert int to decimal
hexDecimal = input("Enter value to convert to decimal: ")
base = int(input("Enter base of the value: "))
def convertToBase(result,newChar,base):
    return result * base + newChar

def convertHexadecimalToDecimal(hexDecimal,base):
    result = 0;
    for char in hexDecimal:
        newChar = ''
        if 'A' <= char <= 'F':
            newChar = ord(char) - ord('A') + 10
            result = convertToBase(result,newChar,base)
        else:
            newChar = ord(char) - ord('0')
            result = convertToBase(result,newChar,base)
    print(result)
convertHexadecimalToDecimal(hexDecimal,base)

#Question 2
#Check for Palindrome
string = input("Enter a word to test for palindrome: ")
print('')
def checkPalindrome(string):
    caseFoldString = string.casefold()
    stringLength=len(caseFoldString)
    stringmiddle=stringLength//2
    reverse=-1
    for digit in range(stringLength):
        print(string[digit] + ' -- ' +string[reverse])
        if caseFoldString[digit]==caseFoldString[reverse]:
            reverse-=1
        else:
            print('\n-->Not Palindrome')
            break
    else:
        print('\n-->Palindrome')
checkPalindrome(string)
