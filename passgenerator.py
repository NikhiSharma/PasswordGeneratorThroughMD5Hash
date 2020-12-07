'''import string,random

def generatePassword(num):
    password=''

    for n in range(num):
        x=random.randint(0,94)
        password+=string.printable[x]
    return password

print(generatePassword(16))
'''
import hashlib

flag = 0

pass_hash = input("Enter md5 hash: ")

wordlist = input("File name: ")

try:
    pass_file = open(wordlist, "r")
except:
    print("No file found")
    quit()

for word in pass_file:

    enc_word = word.encode('utf-8')
    digest = hashlib.md5(enc_word.strip()).hexdigest()
    
    print(word)
    print(digest)
    print(pass_hash)

    if digest == pass_hash:
        print("password found")
        print("password is "+word)
        flag = 1
        break

if flag==0:
    print("password not in list")
