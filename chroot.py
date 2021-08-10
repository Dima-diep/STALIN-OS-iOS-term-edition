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
print(colored("Terminal Tools", 'green', 'on_grey'))
print("----------------------------")
print(colored("System menu", 'magenta', 'on_grey'))
print("----------------------------")
print(colored("Help for Termux-OS", 'magenta', 'on_grey'))
print("----------------------------")
print(colored("Plugin Vim Install (PVI)", 'green', 'on_grey'))
print("============================")
print(colored("Run app:", 'grey', 'on_blue'))
a = input()

if a == 'Contacts':
    os.system("clear && cat ~/Termux-OS/chroot/contacts.txt")
    print("---------------------------")
    print("Call or add contact (call/add)")
    b = input()

    if b == 'call':
        print("Contact for call:")
        c = input()
        os.system(c)
        os.system("clear && python3 ~/Termux-OS/chroot/chroot.py")
    elif b == 'add':
        print("His name?")
        d = input()
        print("His phone (start +7..)")
        e = input()
        os.system("echo \"alias " + d + "=\"termux-telephony-call " + e + "\" >> ~/.bashrc && echo \"alias " + d + "=\"termux-telephony-call " + e + "\" >> ~/.zshrc && source ~/.bashrc && source ~/.zshrc")
        os.system("echo \"" + d + e + "\" >> ~/Termux-OS/chroot/contacts.txt")
        os.system("clear && python3 ~/Termux-OS/chroot/chroot.py")

elif a == 'Music':
    os.system("python3 ~/Termux-OS/home/Music-Termux/player.py")
elif a == 'Package Manager':
    os.system("python3 ~/Termux-OS/chroot/pacman.py")
    os.system("clear && python3 ~/Termux-OS/chroot/chroot.py")
elif a == 'Games':
    os.system("apk list | grep games")
    print("Install or play (i/p)")
    f = input()

    if f == 'i':
        print("Game for install:")
        g = input()
        os.system("apk add " + g)
        os.system("python3 ~/Termux-OS/chroot/chroot.py")
    elif f == 'p':
        print("Game for play:")
        h = input()
        os.system(h)
        os.system("python3 ~/Termux-OS/chroot/chroot.py")
elif a == 'Taskmgr':
    os.system("htop")
    os.system("clear && python3 ~/Termux-OS/chroot/chroot.py")
elif a == 'Telegram':
    print("Do you want install Telegram? y/n")
    i = input()

    if i == 'y'
        os.system("apk add telegram-cli && telegram-cli")
        os.system("python3 ~/Termux-OS/chroot/chroot.py")
    elif i == 'n'
        os.system("telegram-cli")
        os.system("clear && python3 ~/Termux-OS/chroot/chroot.py")
elif a == 'File Manager':
    os.system("mc")
    os.system("python3 ~/Termux-OS/chroot/chroot.py")
elif a == 'Terminal Tools':
    os.system("python3 ~/Termux-OS/system/terminal.py")
    os.system("python3 ~/Termux-OS/chroot/chroot.py")
elif a == 'System menu':
    os.system("python3 ~/Termux-OS/boot/login.py")
    os.system("python3 ~/Termux-OS/system/setting.py")
elif a == 'PVI':
    os.system("vim ~/.vimrc")
    os.system("python3 ~/Termux-OS/system/setting.py")
elif a == 'Help for Termux-OS':
    os.system("termux-open ~/Termux-OS/system/help.html")
    os.system("python3 ~/Termux-OS/chroot/chroot.py")
