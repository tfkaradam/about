#!/usr/bin/env python3 



import os 
import sys
import webbrowser
import time

os.system("pkg install figlet")
os.system("sudo apt install figlet")
os.system("clear")

logo =  """
\33[93m
 _  __    _    ____      _    ____    _    __  __
| |/ /   / \  |  _ \    / \  |  _ \  / \  |  \/  |
| ' /   / _ \ | |_) |  / _ \ | | | |/ _ \ | |\/| |
| . \  / ___ \|  _ <  / ___ \| |_| / ___ \| |  | |
|_|\_\/_/   \_\_| \_\/_/   \_\____/_/   \_\_|  |_|

"""

menu = """
 [-1-]  BEN KİMİM
 [-2-]  INSTAGRAM
 [-3-]  GITHUB
 [-4-]  ÇIKIŞ YAP
 """

social = """
 [-2-]  INSTAGRAM
 [-3-]  GITHUB
 [-4-]  ÇIKIŞ YAP
 """
kimim = """
BEN KİMİM :
            KARADAM

________________________________________________
YETENEKLERİM : 
GÜÇ :    [************          ] %50
HIZ :    [**********************] %100
HACK :   [*****************     ] %70
________________________________________________
KİCKBOKS : [**************        ]%60
SOLAK :    [**********************]%100
GAMER :    [*****                 ]%25
ÇEVRE :    [*                     ]%5
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
    if secim == "2":
        os.system("clear")  
        webbrowser.open("https://www.instagram.com/tfkaradam")
    if secim == "3":
        os.system("clear")
        webbrowser.open("https://www.github.com/tfkaradam")          

    elif (secim == "4"):
        os.system("clear")
        os.system("figlet Tekrar Gel")
        time.sleep(0.5)
        quit()

