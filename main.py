ODDELOVAC = ("=" * 79)

print(ODDELOVAC)

from traceback import print_tb
from users import user_bob
from users import user_ann
from users import user_liz
from users import user_mike
from task_template import TEXTS

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
print("Enter a number btw. 1 and 3 to select: 1")
print(ODDELOVAC)
#===================================================

