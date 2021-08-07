#!/usr/bin/env python3
#! -*- coding: utf-8 -*-
import os
import time
from termcolor import colored

os.system("clear && neofetch && mpv ~/Termux-OS-iOS/login.mp3 > /dev/null && clear")
print("============================")
print(colored("Contacts", 'red', 'on_grey'))
print("----------------------------")
print(colored("Music", 'red', 'on_grey'))
print("----------------------------")
print(colored("Terminal", 'green', 'on_grey'))
print("----------------------------")
print(colored("Package Manager (coming soon)", 'blue', 'on_grey'))
print("----------------------------")
print(colored("Games", 'red', 'on_grey'))
print("----------------------------")
print(colored("Taskmgr Linux", 'red', 'on_grey'))
print("----------------------------")
print(colored("Telegram (worked only on arm64)", 'red', 'on_grey'))
print("----------------------------")
print(colored("Exit", 'cyan', 'on_grey'))
print("============================")
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
        os.system("clear && bash termuxos.sh")
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
    print("For starting OS-menu, run 'bash termuxos.sh'")
    print("------------------------------------")
    os.system("PS1=\"\w $ \"")
elif a == 'Package Manager':
    print("Sorry, it will be here later")
    time.sleep(2.5)
    os.system("clear && bash termuxos.sh")
elif a == 'Games':
    os.system("apk list | grep games")
    print("Install or play (i/p)")
    f = input()

    if f == 'i':
        print("Game for install:")
        g = input()
        os.system("apk add " + g + " -yq")
        os.system("bash termuxos.sh")
    elif f == 'p':
        print("Game for play:")
        h = input()
        os.system(h)
        os.system("bash termuxos.sh")
elif a == 'Taskmgr':
    os.system("htop")
    os.system("clear && bash termuxos.sh")
elif a == 'Telegram':
    print("Do you want install Telegram? y/n")
    i = input()

    if i == 'y'
        os.system("apk add telegram-cli -yq && telegram-cli && exit")
    elif i == 'n'
        os.system("telegram-cli")
        os.system("clear && bash termuxos.sh")
elif a == 'Exit':
    os.system("clear")
    print(colored("|==========================|", 'grey', 'on_white'))
    print(colored("| Where do you want to go? |", 'grey', 'on_white'))
    print(colored("|++++++++++++++++++++++++++|", 'grey', 'on_white'))
    print(colored("| 1.GRUB                   |", 'grey', 'on_white'))
    print(colored("|--------------------------|", 'grey', 'on_white'))
    print(colored("| 2.Exit from iSH          |", 'grey', 'on_white'))
    print(colored("|==========================|", 'grey', 'on_white'))
    j = int(input())

    if j == 1:
        os.system("clear && login")
    elif j == 2:
        os.system("mpv ~/Termux-OS-iOS/exit.mp3 > /dev/null && exit")
