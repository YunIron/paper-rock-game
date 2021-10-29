from time import sleep
import random
import os
from color import *
global scoreplayer
global scoreAi

scoreplayer = 0
scoreAi = 0

clist = ["Tas", "Kagit", "Makas"]

def isleyis():
    global choice
    global cRandom
    print(f"{green}Sen : {scoreplayer}\n{red}AI : {scoreAi}{normal}")
    choice = str(input(f"{yellow}Tas/Kagit/Makas ? :  {normal}")).lower()
    if not choice in ["tas", "kagit", "makas"]:
        print(f"{red}[ - ] Sadece yanda yazan degerleri girebilirsiniz! {normal}")
        sleep(1.5)
        os.system("cls")
        isleyis()
    cRandom = random.choice(clist)


def tas():
    global scoreplayer
    global scoreAi
    if cRandom == "Tas":
        print(f"{red}\n\nAI : {cRandom}")
        print(f"{blue}Berabere !\n\n{normal}")
        sleep(1.5)
        os.system("cls")
    elif cRandom == "Kagit":
        print(f"{red}\n\nAI : {cRandom}")
        print(f"{red}Kaybettiniz! \n\n{normal}")
        scoreAi += 1
        sleep(1.5)
        os.system("cls")
    else:
        print(f"{red}\n\nAI : {cRandom}")
        print(f"{green}Kazandiniz!\n\n{normal}")
        scoreplayer += 1
        sleep(1.5)
        os.system("cls")

def makas():
    global scoreplayer
    global scoreAi
    if cRandom == "Makas":
        print(f"{red}\n\nAI : {cRandom}")
        print(f"{blue}Berabere !\n\n{normal}")
        sleep(1.5)
        os.system("cls")
    elif cRandom == "Tas":
        print(f"{red}\n\nAI : {cRandom}")
        print(f"{red}Kaybettiniz! \n\n{normal}")
        scoreAi += 1
        sleep(1.5)
        os.system("cls")
    else:
        print(f"{red}\n\nAI : {cRandom}")
        print(f"{green}Kazandiniz!\n\n{normal}")
        scoreplayer += 1
        sleep(1.5)
        os.system("cls")

def kagit():
    global scoreplayer
    global scoreAi
    if cRandom == "Kagit":
        print(f"{red}\n\nAI : {cRandom}")
        print(f"{blue}Berabere !\n\n{normal}")
        sleep(1.5)
        os.system("cls")
    elif cRandom == "Makas":
        print(f"{red}\n\nAI : {cRandom}")
        print(f"{red}Kaybettiniz! \n\n{normal}")
        scoreAi += 1
        sleep(1.5)
        os.system("cls")
    else:
        print(f"{red}\n\nAI : {cRandom}")
        print(f"{green}Kazandiniz!\n\n{normal}") 
        scoreplayer += 1
        sleep(1.5)
        os.system("cls")

while True:
    isleyis()
    if choice == "tas":
        tas()

    if choice == "kagit":
        kagit()

    if choice == "makas":
        makas()