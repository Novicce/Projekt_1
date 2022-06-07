"""
2
projekt_1.py: první projekt do Engeto Online Python Akademie
3
4
author: Martin Nováček
5
email: mnovacek@me.com
6
discord: Novicce #7276
"""






ODDELOVAC = ("=" * 79)

print(ODDELOVAC)

from users import user_bob
from users import user_ann
from users import user_liz
from users import user_mike
from task_template import text_1,text_2,text_3

#===================================================
#vstup name a password

uzivatel = input("username: ")
heslo = input("password: ")
uvitaci_obrazovka = ("Welcome to the app,", uzivatel, "We have 3 texts to be analyzed.")

#===================================================
#podminky prihlaseni

if uzivatel == "Bob" and heslo == user_bob:
    print(ODDELOVAC)
    print(f"Welcome to the app, {uzivatel}.")
    print("We have 3 texts to be analyzed.")
elif uzivatel == "Ann" and heslo == user_ann:
    print("Welcome to the app,", uzivatel,".")
    print("We have 3 texts to be analyzed.")
elif uzivatel == "Mike" and heslo == user_mike:
    print("Welcome to the app,", uzivatel,".")
    print("We have 3 texts to be analyzed.")
elif uzivatel == "Liz" and heslo == user_liz:
    print("Welcome to the app,", uzivatel,".")
    print("We have 3 texts to be analyzed.")
else:
  print("unregistered user, terminating the program..")
  exit()
print(ODDELOVAC)
# print("Enter a number btw. 1 and 3 to select: 1")
# print(ODDELOVAC)
#===================================================
#práce s textem

vyber = int(input("Enter a number btw. 1 and 3 to select: "))
print(ODDELOVAC)
if vyber == 1:
    from collections import Counter 
    input_string = text_1
    print("Zvolený text je: "+"\n"+input_string + "\n") 
    output1 = {key:input_string.count(key) for key in input_string.split()} 

elif vyber == 2:
    from collections import Counter 
    input_string = text_2
    print("Zvolený text je: "+"\n"+input_string + "\n") 
    output1 = {key:input_string.count(key) for key in input_string.split()} 

elif vyber == 3:
    from collections import Counter 
    input_string = text_3
    print("Zvolený text je: "+"\n"+input_string + "\n") 
    output1 = {key:input_string.count(key) for key in input_string.split()} 
else:
    print("Not find")
    exit()
print(ODDELOVAC)

#===================================================

# oddelovac: str = "+--+----------+--+"

# rozdělím `str` na `list` bez diakritiky a malým písmem
vycistena_slova = list()

for slovo in text_1.split():
    vycistena_slova.append(
        slovo.strip(",.:;")
    )
#print(vycistena_slova)
