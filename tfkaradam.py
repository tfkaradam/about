#!/usr/bin/env python3 
# -*-coding: utf-8 -*-


import os 
import sys
import webbrowser
import time

os.system("pkg install figlet")
os.system("sudo apt install figlet")
os.system("clear")

logo =  """
\33[93m
    *********************************************************
    *********************************************************
      _                       _
     | | ____ _ _ __ __ _  __| | __ _ _ __ ___
     | |/ / _` | '__/ _` |/ _` |/ _` | '_ ` _ \
     |   < (_| | | | (_| | (_| | (_| | | | | | |
     |_|\_\__,_|_|  \__,_|\__,_|\__,_|_| |_| |_|
--
--           KARADAM - V.1 -
    *********************************************************
    *********************************************************
"""

menu = """
 [-1-]  BEN KİMİM
 [-2-]  INSTAGRAM
 [-3-]  GITHUB
 [-4-]  ÇIKIŞ YAP
 """

social = """
 [-1-]  INSTAGRAM
 [-2-]  GITHUB
 [-4-]  ÇIKIŞ YAP
 """
kimim = """
BEN KİMİM :
            KARADAM
KISACA KİMSİN SORULARINI ATLATMAK
TANIŞMA FASTINI ATLATMAK İÇİN YAPILMIŞTIR 
BİLİŞİM KONUSUYLA BİLGİLİ VE BAZI ŞEYLERE İLGİLİ
ALTINA BELLİ BİR ŞEKİLDE KATAGORİZE ETTİM
________________________________________________
YETENEKLERİM : 
GÜÇ :    [************          ] %50
HIZ :    [**********************] %100
HACK :   [******************    ] %80
________________________________________________
KİCKBOKS : [****************      ]%70
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
        webbrowser.open("https://www.instagram.com/turkerarabacii")
    if secim == "3":
        os.system("clear")
        webbrowser.open("https://www.github.com/tfkaradam")          

    elif (secim == "4"):
        os.system("clear")
        os.system("figlet Tekrar Gel")
        time.sleep(0.5)
        quit()

