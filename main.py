ODDELOVAC = ("=" * 79)

print(ODDELOVAC)

from users import user_bob
from users import user_ann
from users import user_liz
from users import user_mike

#===================================================
#vstup name a password

uzivatel = input("username: ")
heslo = input("password: ")
uvitaci_obrazovka = ("Welcome to the app,", uzivatel, "We have 3 texts to be analyzed.")

#===================================================
#podminky prihlaseni

if uzivatel == "bob" and heslo == user_bob:
    print("Vítej Bob")
elif uzivatel == "ann" and heslo == user_ann:
    print("Vítej Ann")
elif uzivatel == "mike" and heslo == user_mike:
    print("Vítej Mike")
elif uzivatel == "liz" and heslo == user_liz:
    print("Vítej Liz")
else:
  print("neregistrovaný uživatel")
print(ODDELOVAC)
#===================================================
