ODDELOVAC = ("=" * 79)

print(ODDELOVAC)

#===================================================
#vstup name a password

uzivatel = input("username: ")
heslo = input("password: ")
uvitaci_obrazovka = "Vítejte"

#===================================================
#podminky prihlaseni

if uzivatel == "Martin":
    print("Vitej!")
else:
    print("neregistrovaný uživatel")

if heslo == int(243567):
    print(uvitaci_obrazovka)


