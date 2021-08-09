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
print(colored("Package Manager", 'blue', 'on_grey'))
print("----------------------------")
print(colored("Games", 'red', 'on_grey'))
print("----------------------------")
print(colored("Taskmgr Linux", 'red', 'on_grey'))
print("----------------------------")
print(colored("Telegram (worked only on arm64)", 'red', 'on_grey'))
print("----------------------------")
print(colored("File Manager", 'cyan', 'on_grey'))
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
        os.system("clear && python3 ~/Termux-OS/chroot.py")
    elif b == 'add':
        print("His name?")
        d = input()
        print("His phone (start +7..)")
        e = input()
        os.system("echo \"alias " + d + "=\"termux-telephony-call " + e + "\" >> ~/.bashrc && echo \"alias " + d + "=\"termux-telephony-call " + e + "\" >> ~/.zshrc && source ~/.bashrc && source ~/.zshrc")
        os.system("echo \"" + d + e + "\" >> ~/Termux-OS-iOS/contacts.txt")
        os.system("clear && python3 ~/Termux-OS/chroot.py")

elif a == 'Music':
    os.system("python3 ~/Music-Termux/player.py")
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
        os.system("python3 ~/Termux-OS/chroot.py")
    elif f == 'p':
        print("Game for play:")
        h = input()
        os.system(h)
        os.system("python3 ~/Termux-OS/chroot.py")
elif a == 'Taskmgr':
    os.system("htop")
    os.system("clear && python3 ~/Termux-OS/chroot.py")
elif a == 'Telegram':
    print("Do you want install Telegram? y/n")
    i = input()

    if i == 'y'
        os.system("apk add telegram-cli -yq && telegram-cli && exit")
    elif i == 'n'
        os.system("telegram-cli")
        os.system("clear && python3 ~/Termux-OS/chroot.py")
elif a == 'Exit':
    os.system("clear")
    os.system("mpv ~/Termux-OS-iOS/exit.mp3 > /dev/null && kill -9 /home/Termux-OS/chroot.py")
