#!/usr/bin/env python3
#! -*- coding: utf-8 -*-
import os
import time
from termcolor import colored

print("---------------------------------")
os.system("uname -a")
print(" ")
print("Termux GRUB by Dima-diep")
print("|=== === === === === === === ===|")
print("| 1.Termux OS                   |")
print("| 2.proot-system login          |")
print("| 3.proot-system installer      |")
print("|=== === === === === === === ===|")
print("Select your system: ")
a = int(input())

if a == 1:
    os.system("python3 ~/Termux-OS/login.py")
    os.system("neofetch")

elif a == 2:
    os.system("clear")
    time.sleep(2.5)
    print("(===    ===   ===)")
    print("( 1.atilo        )")
    print("( 2.proot-distro )")
    print("(===   ===    ===)")
    print("Your proot type: ")
    b = int(input())

    if b == 1:
        print("Your OS: ")
        c = input()
        print("Mounting " + c + " rootfs...")
        time.sleep(1)
        os.system("atilo pull " + c)
        os.system("exit")
    elif b == 2:
        print("Your OS: ")
        d = input()
        print("Mounting " + d + " rootfs...")
        time.sleep(1)
        os.system("proot-distro login " + d)
        os.system("exit")
elif a == 3:
    os.system("clear")
    print(colored("|=== === === === === === === ===", 'grey', 'on_blue'))
    print(colored("| Types of installation:       |", 'grey', 'on_blue'))
    print(colored("|=== === === === === === === ===", 'grey', 'on_blue'))
    print(colored("| 1.atilo                      |", 'grey', 'on_blue'))
    print(colored("|------------------------------|", 'grey', 'on_blue'))
    print(colored("| 2.proot-distro Termux-repo   |", 'grey', 'on_blue'))
    print(colored("|------------------------------|", 'grey', 'on_blue'))
    print(colored("Select your type: ", 'grey', 'on_white'))
    f = int(input())

    if f == 1:
        os.system("clear")
        print(colored("Do you install it at first time?", 'grey', 'on_blue'))
        print("yes/no")
        g = input()

        if g == 'yes':
            os.system("echo \"deb [trusted=yes] https://yadominjinta.github.io/files/ termux extras\" >> /etc/apt/sources.list && apk update -yq && apk add atilo -yq && clear")
            print("List supported system:")
            os.system("atilo images")
            print("What do you want install?")
            h = input()
            os.system("atilo pull " + h)
            os.system("atilo run " + h)
            os.system("exit")

        elif g == 'no':
            print("List supported system:")
            os.system("atilo images")
            print("What do you want install?")
            i = input()
            os.system("atilo pull " + i)
            os.system("atilo run " + i)
            os.system("exit")
    elif f == 2:
        os.system("clear && apk add proot proot-distro -yq && clear")
        os.system("proot-distro list")
        print("What system do you want install?")
        j = input()
        os.system("proot-distro install " + j)
        os.system("proot-distro login " + j)
        os.system("exit")
