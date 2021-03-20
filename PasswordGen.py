# Password Generater
import string_utils # this module is for shuffling the passwords

userChars = input("Enter the characters you want in your password : ")
userPasswords = int(input("How many passwords do you want to generate : "))
passwordLength = input("Enter the length of your passwords : ")

if passwordLength == "" or int(passwordLength) > len(userChars):
    passwordLength = len(userChars)
else:
    passwordLength = int(passwordLength)

# Generate the password
for x in range(0,userPasswords):
    password = ""
    password = string_utils.shuffle(userChars) # this shuffles userChar 

    passwordList = []
    passwordList[:0] = password
    # print(passwordList) optional 

    password = ""
    number = 0
    for i in passwordList:
        if number >= passwordLength:
            break
        password += i
        number += 1
    print(password) # this prints the password
