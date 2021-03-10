import random
import string_utils

while True:
    userChars = input("Enter the characters you want in your password: ")
    if userChars == "":
        break
    userPasswords = int(input("How many passwords do you want to generate : "))
    userLength = input("How many characters do you want in each password : ")
    if userLength.strip() == "":
        userLength = len(userChars)
    if int(userLength) > len(userChars):
        userLength = len(userChars)
    if userLength != "" :
        userLength = int(userLength)
        
    for x in range(0,userPasswords):
        password = ""
        password = string_utils.shuffle(userChars)

        passwordList = []
        passwordList[:0] = password
        #print(passwordList)
        password = ""
        e = 0
        for i in passwordList:
            if e >= userLength:
                break
            password += i
            e += 1
        print(password)
