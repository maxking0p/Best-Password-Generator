import random
import time
import pywhatkit as kit
time.sleep(1)
print("Okay! lets generate some passwords")
print(".")
time.sleep(1)
print("..")
time.sleep(1)
pass_char = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz123456789)(*&^%$#@!"
user_input = int(input("bro how much pass.. do you wanna generate for your, whatever. :- "))
pass_length = int(input(" and what will be the password lenth:- "))
if user_input == 1:
    print("your password is :- \n")
elif user_input == 0:
    print("you are a noob! but i still have password for you")
    for i in range(1):
        passwords = ""
    for c in range(6,20):
        passwords += random.choice(pass_char)
    print(passwords)
    exit()
else:
    print("your passwords are :- \n")
for i in range(user_input):
    passwords = ""
    for c in range(pass_length):
        passwords += random.choice(pass_char)
    print(passwords)
if pass_length <=5:
    print("its a weak password you noob! you can't even generate stronger passwords ")
    print("try one more time")
    while True:
        pass_char = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz123456789)(*&^%$#@!"
        user_input = int(input("how many password you wanna generate"))
        pass_length = int(input(" choose atleast 6 or greater than 6 digits length of password . :- "))
        print("your passwords are :- \n")
        for i in range(user_input):
            passwords = ""
            for c in range(pass_length):
                passwords += random.choice(pass_char)
            print(passwords)
        if pass_length <=5:
            kit.playonyt("https://www.youtube.com/watch?v=DlH-ax6LsoA")
            print("\U0001F4A9")
            break
        
    
else:
    print("its a strong password")
    print("now wait!")


kit.playonyt("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

time.sleep(1)
print("T", end='')
time.sleep(1)
print("H", end='')
time.sleep(1)
print("A", end='')
time.sleep(1)
print("N", end='')
time.sleep(1)
print("K", end='')
time.sleep(1)
print("Y", end='')
time.sleep(1)
print("O", end='')
time.sleep(1)
print("U", end='')



