#!/usr/bin/python3
#coding=utf-8
import os,sys,time,requests
from time import sleep
    ###----------[ ANSII COLOR STYLE ]---------- ###
Z2 = "\x1b[0;90m"     # Hitam
M2 = "\x1b[38;5;196m" # Merah
H2 = "\x1b[38;5;46m"  # Hijau
K2 = "\x1b[38;5;226m" # Kuning
B2 = "\x1b[38;5;44m"  # Biru
U2 = "\x1b[0;95m"     # Ungu
O2 = "\x1b[0;96m"     # Biru Muda
P2 = "\x1b[38;5;231m" # Putih
J2 = "\x1b[38;5;208m" # Jingga
A2 = "\x1b[38;5;248m" # Abu-Abu
###----------[ ANSII COLOR STYLE 2 ]---------- ###
P1 = "\033[37;7;1m"
M1 = "\033[31;7;1m"
H1 = "\033[32;7;1m"
K1 = "\033[33;7;1m"
B1 = "\033[34;7;1m"
U1 = "\033[35;7;1m"
O1 = "\033[36;7;1m"
A1 = "\033[0m"
L1 = "\033[4m"
###----------[ ANSII COLOR STYLE 3 ]---------- ###
Z = "\x1b[1;90m"
M = "\x1b[1;91m"
H = "\x1b[1;92m"
K = "\x1b[1;93m"
B = "\x1b[1;94m"
U = "\x1b[1;95m"
O = "\x1b[1;96m"
P = "\x1b[1;97m"
###Huruf Kecil Alfabet###
if 'linux' in sys.platform:
  r = "\033[91m" # Red
  g = "\033[92m" # Green
  y = "\033[93m" # Yellow
  p = "\033[94m" # Purple
  P = "\033[95m" # Pink
  c = "\033[96m" # Cyan
  w = "\033[97m" # White
  a = "\033[0m"  # Reset
else:
  # Convert String To Variabel Name
  for i in ['r','g','y','p','P','c','w','a']:
    globals()[i] = ""

import os
import sys
import time
import json
import random
import socket
import shutil
import webbrowser
import concurrent.futures
import time, os, requests, json, random, bs4
try:
  __import__('requests')
except ModuleNotFoundError:
  os.system ('pip3 install requests')
finally:
  import requests

try:
  __import__('bs4')
except ModuleNotFoundError:
  os.system ("pip3 install bs4")
finally:
  from bs4 import BeautifulSoup as parser
#lu jangan edit ini
def mengetik(z):
    for e in z + "\n":
      sys.stdout.write(e)
      sys.stdout.flush()
      time.sleep(0.01)
NUD = "Zidan Boyyah"
NO = "The WelsyDun"
def addelia():
      os.system('cowsay Enter CTRL + C TO Cancel | lolcat')
      os.system('cowsay -f bong Enter CTRL + C TO Cancel | lolcat')
      os.system('cowsay -f btc Enter CTRL + C TO Cancel | lolcat')
      os.system('cowsay -f bunny Enter CTRL + C TO Cancel | lolcat')
      os.system('cowsay -f cheese Enter CTRL + C TO Cancel | lolcat')
      os.system('cowsay -f daemon Enter CTRL + C TO Cancel | lolcat')
      os.system('cowsay -f dragon Enter CTRL + C TO Cancel | lolcat')
      os.system('cowsay -f elephant Enter CTRL + C TO Cancel | lolcat')
      os.system('cowsay -f eyes Enter CTRL + C TO Cancel | lolcat')
      os.system('cowsay -f ghostbusters Enter CTRL + C TO Cancel | lolcat')
      os.system('cowsay -f hello Enter CTRL + C TO Cancel | lolcat')
      os.system('cowsay -f hellokitty Enter CTRL + C TO Cancel | lolcat')
      os.system('cowsay -f key Enter CTRL + C TO Cancel | lolcat')
      os.system('cowsay -f kiss Enter CTRL + C TO Cancel | lolcat')
      os.system('cowsay -f kitty Enter CTRL + C TO Cancel | lolcat')
      os.system('cowsay -f koala Enter CTRL + C TO Cancel | lolcat')
      os.system('cowsay -f kosh Enter CTRL + C TO Cancel | lolcat')
      os.system('cowsay -f meow Enter CTRL + C TO Cancel | lolcat')
      os.system('cowsay -f milk Enter CTRL + C TO Cancel | lolcat')
      os.system('cowsay -f moofasa Enter CTRL + C TO Cancel | lolcat')
      os.system('cowsay -f moose Enter CTRL + C TO Cancel | lolcat')
      os.system('cowsay -f muttlated Enter CTRL + C TO Cancel | lolcat')
      os.system('cowsay -f ren Enter CTRL + C TO Cancel | lolcat')
      os.system('cowsay -f sheep Enter CTRL + C TO Cancel | lolcat')
      os.system('cowsay -f skeleton Enter CTRL + C TO Cancel | lolcat')
      os.system('cowsay -f stegosaurus Enter CTRL + C TO Cancel | lolcat')
      os.system('cowsay -f stimpy Enter CTRL + C TO Cancel | lolcat')
      os.system('cowsay -f turkey Enter CTRL + C TO Cancel | lolcat')
      os.system('cowsay -f turtle Enter CTRL + C TO Cancel | lolcat')

def sintia():
    os.system('clear')
    os.system('cowsay Enter CTRL + C TO Cancel')
    os.system('cowsay -f bong Enter CTRL + C TO Cancel')
    os.system('cowsay -f btc Enter CTRL + C TO Cancel')
    os.system('cowsay -f bunny Enter CTRL + C TO Cancel')
    os.system('cowsay -f cheese Enter CTRL + C TO Cancel')
    os.system('cowsay -f daemon Enter CTRL + C TO Cancel')
    os.system('cowsay -f dragon Enter CTRL + C TO Cancel')
    os.system('cowsay -f elephant Enter CTRL + C TO Cancel')
    os.system('cowsay -f eyes Enter CTRL + C TO Cancel')
    os.system('cowsay -f ghostbusters Enter CTRL + C TO Cancel')
    os.system('cowsay -f hello Enter CTRL + C TO Cancel')
    os.system('cowsay -f hellokitty Enter CTRL + C TO Cancel')
    os.system('cowsay -f key Enter CTRL + C TO Cancel')
    os.system('cowsay -f kiss Enter CTRL + C TO Cancel')
    os.system('cowsay -f kitty Enter CTRL + C TO Cancel')
    os.system('cowsay -f koala Enter CTRL + C TO Cancel')
    os.system('cowsay -f kosh Enter CTRL + C TO Cancel')
    os.system('cowsay -f meow Enter CTRL + C TO Cancel')
    os.system('cowsay -f milk Enter CTRL + C TO Cancel')
    os.system('cowsay -f moofasa Enter CTRL + C TO Cancel')
    os.system('cowsay -f moose Enter CTRL + C TO Cancel')
    os.system('cowsay -f muttlated Enter CTRL + C TO Cancel')
    os.system('cowsay -f ren Enter CTRL + C TO Cancel')
    os.system('cowsay -f sheep Enter CTRL + C TO Cancel')
    os.system('cowsay -f skeleton Enter CTRL + C TO Cancel')
    os.system('cowsay -f stegosaurus Enter CTRL + C TO Cancel')
    os.system('cowsay -f stimpy Enter CTRL + C TO Cancel')
    os.system('cowsay -f turkey Enter CTRL + C TO Cancel')
    os.system('cowsay -f turtle Enter CTRL + C TO Cancel')

os.system('clear')
mengetik("\033[91m>\033[0m By The WelsyDun")
sleep(1)
mengetik("\033[91m>\033[0m Dont Edit This Script")
sleep(1)
mengetik("\033[91m>\033[0m Dont Forget To Click The Menu")
sleep(1)
os.system('clear')
colors = lambda : random.choice([r,g,y,p,P,c,w])
logo = f"{r}****     **** *******     **     **\n/**/**   **/**/**////**   //**   ** \n/**//** ** /**/**   /**    //** **  \n/** //***  /**/*******      //***   \n/**  //*   /**/**///**       **/**  \n/**   /    /**/**  //**     ** //** \n/**        /**/**   //**   **   //**\n//         // //     //   //     //\n{r}╔═════════════════════════════════════╗\n║[{p}1{r}] {c}OpenLink : {c}Semawur               {r}║\n║[{p}2{r}] {c}OpenLink : {p}Adsafelink            {r}║\n║[{p}3{r}] {c}Openlink : {r}Sub2unlock           {r} ║\n║[{p}4{r}] {c}Openlink : {c}MediaFire             {r}║\n║[{p}C{r}] {c}CREATED  : {NO}         {r} ║\n║[{p}Y{r}] {c}YOUTUBE  :{y} NO YET CREATED     {r}   ║\n║[{p}W{r}] {c}Wa       : +{y}6282119491832 {r}       ║\n║[{p}•{r}] {c}TeamCOC  :{colors()} DUTA{colors()}INDO{r}NESIA{w}CLAN{r}     ║\n╚═════════════════════════════════════╝{g}"

def menu():
  os.system('clear')
  print (logo)
  os.system ("date")
  print (g + "CHOSE MENU IN ABOVE")
  print ("%s%s" % (c,"="*37))
  print (f'{p}[{y}1{p}] {c}SemawurLink\n{p}[{y}2{p}] {p}Adsafelink\n{p}[{y}3{p}] {r}Sub2UnlockLink\n{p}[{y}4{p}] {c}Mediafire\n{p}[{y}5{p}] {y}Date\n{p}[{y}6{p}] {y}Contact{c} Me\n{p}[{y}7{p}] {r}info\n{p}[{y}8{p}] {r}Cowsay{y} Fully\n{p}[{y}9{p}] {c}Tik{y}Tok{p} Video{g} Download\n{p}[{y}0{p}] {r}EXIT')
  choice = input("%ssintia/>>> %s" % (P,g))
  if choice == '1' or choice == '01':
    url = "https://safelinku.com"
    code = webbrowser.open(url)
    if code:
      time.sleep(0.9)
      menu()
    else:
      os.system ("xdg-open "+url)
      time.sleep(0.9)
      menu()
  elif choice == '2' or choice == '02':
    url = "https://adsafelink.com"
    code = webbrowser.open(url)
    if code:
      time.sleep(0.9)
      menu()
    else:
      os.system ("xdg-open "+url)
      time.sleep(0.9)
      menu()
  elif choice == '3' or choice == '02':
    url = "https://sub2unlock.com"
    code = webbrowser.open(url)
    if code:
      time.sleep(0.9)
      menu()
    else:
      os.system ("xdg-open "+url)
      time.sleep(0.9)
      menu()
  elif choice == '4' or choice == '02':
    url = "https://mediafire.com"
    code = webbrowser.open(url)
    if code:
      time.sleep(0.9)
      menu()
    else:
      os.system ("xdg-open "+url)
      time.sleep(0.9)
      menu()
  elif choice == '5' or choice == '03':
    os.system('clear')
    os.system('pkg install tty-clock')
    os.system('tty-clock')
  elif choice == '6' or choice == '03':
    os.system('clear')
    url = "https://wa.me/6282119491832"
    code = webbrowser.open(url)
    if code:
      time.sleep(0.9)
      menu()
    else:
      os.system('xdg-open '+url)
      time.sleep(0.9)
      menu()
  elif choice == '7' or choice == '03':
    os.system('clear')
    print (f"{logo}\n{g}INFO SCRIPT\n========================\n{p}[{y}✓{p}] {c}Author: {g}The WeslyDun\n{p}[{y}✓{p}] {c}Team  : {colors()}DUTA {colors()}INDO {r}NESIA{w}CLAN\n{p}[{y}✓{p}] {c}Script: {colors()}{os.path.basename(sys.argv[0])}\n{p}[{y}✓{p}] {c}Path  : {os.path.realpath(sys.argv[0])}\n{p}[{y}✓{p}] {c}Size  : {os.stat(os.path.realpath(sys.argv[0])).st_size} Byte\n{p}[{y}✓{p}] {c}Read  : {colors()} Dont Edit This Text\n{p}[{y}✓{p}] {c}TikTok: {colors()}{NUD}\n{p}[{y}✓{p}] {c}Version : 0.77\n\n{g}Contact Me ^_^\n==================\n{p}[{y}✓{p}] {c}Youtube: {colors()}The WelsyDun\n{p}[{y}✓{p}] {c}Fb.   : {colors()}no yet created fb\n{p}[{y}✓{p}] {c}Wa.   : {colors()}+62 82119491832\n{p}[{y}✓{p}] {c}Email : {colors()}termux.indonesia01@gmail.com\n{a}")
    sleep(2)
    print ("\033[91mExit The Info. Time 3s")
    sleep(3)
    menu()
  if choice == '8' or choice == '08':
    sintia()
    print (f'{p}[{y}!{p}] {g}Do you want to rainbow cowsay this ? {g}(y/{r}n)\n')
    echa = input("%saddelia/>>>> %s" % (p,g)).lower()
    if echa == 'y':
     addelia()
    elif echa == 'n':
     menu()
  if choice == '9' or choice == '09':
   mengetik("\033[1;30m<════════════[\033[1;33;41m • \033[1;37m Status \033[1;33m• \033[0m\033[1;30m]══════════════>")
   os.system('pkg install toilet && toilet Instal | lolcat && toilet ling | lolcat && toilet Dont | lolcat  && toilet Close | lolcat && pkg install git && python3 -m pip install requests && cd /sdcard && python Tik.py')
   if choice == '00' or choice == '0':
    os.abort()                
   else:
        print ("%s[!] Select Input!" % (y))
        time.sleep(0.9)
        menu()
                    
if __name__ == "__main__":
   menu()   
