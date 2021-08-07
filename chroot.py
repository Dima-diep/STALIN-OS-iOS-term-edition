#!/usr/bin/env python3
#! -*- coding: utf-8 -*-
import os
import time
from termcolor import colored

os.system("clear")
print("----------------------------")
print(colored("Contacts", 'red', 'on_grey'))
print(colored("Music", 'red', 'on_grey'))
print(colored("Terminal", 'green', 'on_grey'))
print(colored("Package Manager (coming soon)", 'blue', 'on_grey'))
print(colored("Games", 'red', 'on_grey'))
print(colored("Taskmgr Linux", 'red', 'on_grey'))
print(colored("Telegram", 'red', 'on_grey'))
print("----------------------------")
print(colored("Run app:", 'grey', 'on_blue'))
a = input()

if a == 'Contacts':
    os.system("clear && cat contacts.txt")
    print("---------------------------")
    print("Call or add contact")
    b = input()

    if b == 'call':
        print("Contact for call:")
        c = input()
        os.system(c)
        os.system("clear && termuxos")
    elif b == 'add':
        print("His name?")
        d = input()
        print("His phone (start +7..)")
        e = input()
        os.system("echo \"alias " + d + "=\"termux-telephony-call " + e + "\" >> ~/.bashrc && echo \"alias " + d + "=\"termux-telephony-call " + e + "\" >> ~/.zshrc && source ~/.bashrc && source ~/.zshrc")
        os.system("echo \"" + d + e + "\" >> ~/Termux-OS/contacts.txt")
        os.system("clear && termuxos")

elif a == 'Music':
    os.system("python3 ~/Music-Termux/player.py")
elif a == 'Terminal':
    os.system("clear && cd ~ && bash")
    print("For starting OS-menu, run 'termuxos'")
    print("------------------------------------")
elif a == 'Package Manager':
    print("Sorry, it will be here later")
    time.sleep(2.5)
    os.system("clear && termuxos.sh")
elif a == 'Games':
    os.system("apk list | grep games")
    print("Install or play (i/p)")
    f = input()

    if f == 'i':
        print("Game for install:")
        g = input()
        os.system("apk add " + g + " -yq")
        os.system("termuxos")
    elif f == 'p':
        print("Game for play:")
        h = input()
        os.system(h)
        os.system("termuxos")
elif a == 'Taskmgr':
    os.system("htop")
    os.system("clear && termuxos")
elif a == 'Telegram':
    os.system("telegram-cli")
    os.system("clear && termuxos")
