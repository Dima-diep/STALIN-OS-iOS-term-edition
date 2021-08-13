#!/usr/bin/env python3
#! -*- coding: utf-8 -*-
import os
import time
from termcolor import colored

print("============================")
print(colored("Contacts", 'red', 'on_grey'))
print("----------------------------")
print(colored("Music", 'red', 'on_grey'))
print("----------------------------")
print(colored("Package Manager", 'cyan', 'on_grey'))
print("----------------------------")
print(colored("Games", 'red', 'on_grey'))
print("----------------------------")
print(colored("Taskmgr Linux", 'red', 'on_grey'))
print("----------------------------")
print(colored("Telegram (supported for arm64)", 'red', 'on_grey'))
print("----------------------------")
print(colored("File Manager", 'cyan', 'on_grey'))
print("----------------------------")
print(colored("Terminal tools", 'green', 'on_grey'))
print("----------------------------")
print(colored("System menu", 'magenta' ,'on_grey'))
print("----------------------------")
print(colored("Help for STALIN-OS", 'magenta', 'on_grey'))
print("----------------------------")
print(colored("Plugin Vim Install (PVI)", 'green', 'on_grey'))
print("----------------------------")
print(colored("Tor", 'magenta', 'on_grey'))
print("----------------------------")
print(colored("For developers", 'yellow', 'on_grey'))
print("----------------------------")
print(colored("Open file in android app (Open)", 'red', 'on_grey'))
print("----------------------------")
print(colored("Calculator", 'green', 'on_grey'))
print("----------------------------")
print(colored("Test Network Speed(TNS), 'yellow', 'on_grey'))
print("----------------------------")
print(colored("Open file into text editor (OFTE)", 'yellow', 'on_grey'))
print("----------------------------")
print(colored("Exit to GRUB (GRUB)", 'cyan', 'on_grey'))
print("============================")
print(colored("Run app:", 'grey', 'on_blue'))
a = input()

if a == 'Contacts':
    os.system("clear && cat ~/STALIN-OS/chroot/contacts.txt")
    print("---------------------------")
    print("call or add contact")
    print("call/add")
    b = input()

    if b == 'call':
        print("Contact for call:")
        c = input()
        os.system(c)
        os.system("clear && python3 ~/STALIN-OS/chroot/chroot.py")
    elif b == 'add':
        print("His name?")
        d = input()
        print("His phone (start +7...)")
        e = input()
        os.system("echo \"alias " + d + "=\"termux-telephony-call " + e + "\" >> ~/.bashrc && echo \"alias " + d + "=\"termux-telephony-call " + e + "\" >> ~/.zshrc && source ~/.bashrc && source ~/.zshrc")
        os.system("echo \"" + d + e + "\" >> ~/STALIN-OS/chroot/contacts.txt")
        os.system("clear && python3 ~/STALIN-OS/chroot/chroot.py")

elif a == 'Music':
    os.system("python3 ~/STALIN-OS/home/Music-Termux/player.py && python3 ~/STALIN-OS/chroot/chroot.py")
elif a == 'Package Manager':
    os.system("python3 ~/STALIN-OS/chroot/pacman.py")
elif a == 'Games':
    print("Game for play:")
    h = input()
    os.system(h)
    os.system("python3 ~/STALIN-OS/chroot/chroot.py")
elif a == 'Taskmgr':
    os.system("htop")
    os.system("clear && python3 ~/STALIN-OS/chroot/chroot.py")
elif a == 'Telegram':
    print("Do you want install Telegram (supported only for arm64) (y for install, n for login now")
    i = input()

    if i == 'y':
        os.system("apt install telegram-cli -yq")
        os.system("telegram-cli")
        os.system("clear && python3 ~/STALIN-OS/chroot/chroot.py")
    elif i == 'n':
        os.system("telegram-cli")
        os.system("clear && python3 ~/STALIN-OS/chroot/chroot.py")
elif a == 'File Manager':
    os.system("mc && python3 ~/STALIN-OS/chroot/chroot.py")
elif a == 'Terminal tools':
    os.system("python3 ~/STALIN-OS/chroot/terminal.py")
elif a == 'Help for Termux-OS':
    os.system("termux-open ~/STALIN-OS/system/help.html")
    os.system("python3 ~/STALIN-OS/chroot/chroot.py")
elif a == 'PVI':
    os.system("vim ~/.vimrc")
    os.system("python3 ~/STALIN-OS/chroot/chroot.py")
elif a == 'System menu':
    os.system("python3 ~/STALIN-OS/boot/login.py")
    os.system("python3 ~/STALIN-OS/system/setting.py")
    os.system("python3 ~/STALIN-OS/chroot/chroot.py")
elif a == 'Tor':
    os.system("tor")
    print("Ctrl-Z for stopping")
    os.system("python3 ~/STALIN-OS/chroot/chroot.py")
elif a == 'For developers':
    os.system("termux-open ~/STALIN-OS/system/fordev.html")
    os.system("python3 ~/STALIN-OS/chroot/chroot.py")
elif a == 'Open':
    print("Path to file (full path)")
    j = input()
    os.system("termux-open " + j)
    os.system("python3 ~/STALIN-OS/chroot/chroot.py")
elif a == 'Calculator':
    os.system("clear && calc")
    os.system("python3 ~/STALIN-OS/chroot/chroot.py")
elif a == 'TNS':
    os.system("clear && ping 8.8.8.8")
    os.system("python3 ~/STALIN-OS/chroot/chroot.py")
elif a == 'OFTE':
    os.system("clear")
    print(colored("| === === === === |", 'yellow', 'on_grey'))
    print(colored("| 1.nano          |", 'yellow', 'on_grey'))
    print(colored("|-----------------|", 'yellow', 'on_grey'))
    print(colored("| 2.vim           |", 'yellow', 'on_grey'))
    print(colored("|-----------------|", 'yellow', 'on_grey'))
    print(colored("| 3.micro         |", 'yellow', 'on_grey'))
    print(colored("|-----------------|", 'yellow', 'on_grey'))
    print(colored("| 4.neovim        |", 'yellow', 'on_grey'))
    print(colored("|-----------------|", 'yellow', 'on_grey'))
    print(colored("| 5.joe           |", 'yellow', 'on_grey'))
    print(colored("|-----------------|", 'yellow', 'on_grey'))
    print(colored("| 6.emacs         |", 'yellow', 'on_grey'))
    print(colored("|-----------------|", 'yellow', 'on_grey'))
    print(colored("| 7.mcedit        |", 'yellow', 'on_grey'))
    print(colored("|-----------------|", 'yellow', 'on_grey'))
    print(colored("| 8.System editor |", 'yellow', 'on_grey'))
    print(colored("|-----------------|", 'yellow', 'on_grey'))
    print(colored("| 9.vi            |", 'yellow', 'on_grey'))
    print(colored("|-----------------|", 'yellow', 'on_grey'))
    print(colored("| 10.exit         |", 'yellow', 'on_grey'))
    print(colored("| === === === === |", 'yellow', 'on_grey'))
    print(colored("Select your editor:", 'green', 'on_grey'))
    k = int(input())
    print(colored("Full path to file:", 'green', 'on_grey'))
    l = input()

    if k == 1:
        os.system("nano " + l)
        os.system("clear && python3 ~/STALIN-OS/chroot/chroot.py")
    elif k == 2:
        os.system("vim " + l)
        os.system("clear && python3 ~/STALIN-OS/chroot/chroot.py")
    elif k == 3:
        os.system("micro " + l)
        os.system("clear && python3 ~/STALIN-OS/chroot/chroot.py")
    elif k == 4:
        os.system("neovim " + l)
        os.system("clear && python3 ~/STALIN-OS/chroot/chroot.py")
    elif k == 5:
        os.system("joe " + l)
        os.system("clear && python3 ~/STALIN-OS/chroot/chroot.py")
    elif k == 6:
        os.system("emacs " + l)
        os.system("clear && python3 ~/STALIN-OS/chroot/chroot.py")
    elif k == 7:
        os.system("mcedit " + l)
        os.system("clear && python3 ~/STALIN-OS/chroot/chroot.py")
    elif k == 8:
        os.system("termux-open " + l)
        os.system("clear && python3 ~/STALIN-OS/chroot/chroot.py")
    elif k == 9:
        os.system("vi " + l)
        os.system("clear && python3 ~/STALIN-OS/chroot/chroot.py")
    elif k == 10:
        os.system("clear && python3 ~/STALIN-OS/chroot/chroot.py")
