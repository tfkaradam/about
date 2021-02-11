#!/usr/bin/env python3 
# instagram: turkerarabacii 
# github : https://github.com/tfkaradam

import os 
import sys
import webbrowser
import time

os.system("pkg install figlet")
os.system("sudo apt install figlet")
os.system("clear")

logo =  """
\33[93m
    *******************************************************
    *********************************************************
    ***  _____         _                          _       ***
_  __    _    ____      _    ____    _    __  __
| |/ /   / \  |  _ \    / \  |  _ \  / \  |  \/  |
| ' /   / _ \ | |_) |  / _ \ | | | |/ _ \ | |\/| |
| . \  / ___ \|  _ <  / ___ \| |_| / ___ \| |  | |
|_|\_\/_/   \_\_| \_\/_/   \_\____/_/   \_\_|  |_|
    ***                                                   ***
    ***         K A R A D A M => V1.0        ***
    *********************************************************
    *********************************************************
"""

menu = """
 [-1-]  BEN KİMİM
 [-2-]  ÇIKIŞ YAP
 """


kimim = """
BEN KİMİM :
            TFKARADAM
Eğlencesine yapılmış bir tanıtma tooludur
________________________________________________
YETENEKLERİM : 
GÜÇ :    [***************      ] %70
HIZ :    [**********************] %100
HACK :   [********************* ] %96
________________________________________________
SOLAK :    [**********************]%100
GAMER :    [*****                 ]%25
ÇEVRE :    [*                     ]%5
________________________________________________
Web Site : tfkaradam.com
________________________________________________
                ---- SON  ----
"""
while(1):
    os.system("clear")
    print (logo + menu)
    secim = input("seçenek : ")
    os.system("clear")
    print(logo)
    if (secim == "1"):
        print(kimim)
        input()
    if secim == "":
        os.system("clear")  
        webbrowser.open("https://www.instagram.com/turkerarabacii")
    if secim == "3":
        os.system("clear")
        webbrowser.open("https://tfkaradam.com")   
    if secim == "4":
        os.system("clear")
        webbrowser.open("https://www.github.com/tfkaradam")          

    elif (secim == "2"):
        os.system("clear")
        os.system("figlet Good Bye")
        time.sleep(0.5)
        quit()


