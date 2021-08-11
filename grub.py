#!/usr/bin/env python3
#! -*- coding: utf-8 -*-
import os
import time
from termcolor import colored

os.system("cd ~/STALIN-OS/home")
os.system("bash ~/STALIN-OS/system/.killhist.sh")
os.system("clear")
print("---------------------------------")
os.system("uname -a")
print(" ")
print("Termux GRUB v3.0 by Dima-diep")
print("STALIN-OS-iOS v3.1.0 term-edition by Dima-diep")
print("|=== === === === === === === ===|")
print("| 1.Termux OS                   |")
print("| 2.proot-system login          |")
print("| 3.proot-system installer      |")
print("| 4.OS-Recovery Mode            |")
print("|=== === === === === === === ===|")
print("For exit, press Ctrl-C or Ctrl-Z")
os.system("python3 ~/STALIN-OS/boot/login.py")
print("Select your system: ")
a = int(input())

if a == 1:
    os.system("clear")
    os.system("python3 ~/STALIN-OS/boot/boot.py")
    os.system("clear")
    os.system("python3 ~/STALIN-OS/chroot/chroot.py")

elif a == 2:
    os.system("clear")
    time.sleep(2.5)
    print("(===    ===   ===)")
    print("( 1.atilo        )")
    print("( 2.proot-distro )")
    print("( 3.Andronix OS  )")
    print("(===   ===    ===)")
    print("Your proot type: ")
    b = int(input())

    if b == 1:
        print("Your OS: ")
        c = input()
        print("Mounting " + c + " rootfs...")
        time.sleep(1)
        os.system("atilo pull " + c)
        os.system("login")
    elif b == 2:
        print("Your OS: ")
        d = input()
        print("Mounting " + d + " rootfs...")
        time.sleep(1)
        os.system("proot-distro login " + d)
        os.system("login")
    elif b == 3:
        print("Your OS (filename without ./): ")
        e = input()
        print("Mounting " + e + " rootfs...")
        time.sleep(1)
        os.system("bash " + e)
        os.system("login")
elif a == 3:
    os.system("clear")
    print(colored("|=== === === === === === === ===", 'grey', 'on_blue'))
    print(colored("| Types of installation:       |", 'grey', 'on_blue'))
    print(colored("|=== === === === === === === ===", 'grey', 'on_blue'))
    print(colored("| 1.atilo                      |", 'grey', 'on_blue'))
    print(colored("|------------------------------|", 'grey', 'on_blue'))
    print(colored("| 2.proot-distro Termux-repo   |", 'grey', 'on_blue'))
    print(colored("|------------------------------|", 'grey', 'on_blue'))
    print(colored("| 3.Andronix OS                |", 'grey', 'on_blue'))
    print(colored("|------------------------------|", 'grey', 'on_blue'))
    print(colored("Select your type: ", 'grey', 'on_white'))
    f = int(input())

    if f == 1:
        print("List supported system:")
        os.system("atilo images")
        print("What do you want install?")
        i = input()
        os.system("atilo pull " + i)
        os.system("atilo run " + i)
        os.system("login")
    elif f == 2:
        os.system("clear && apt install proot proot-distro -yq && clear")
        os.system("proot-distro list")
        print("What system do you want install?")
        j = input()
        os.system("proot-distro install " + j)
        os.system("proot-distro login " + j)
        os.system("login")

    elif f == 3:
        os.system("clear && git clone https://github.com/Dima-diep/Linux-Installer-Termux && cd Linux-Installer-Termux && chmod 777 *.py && chmod +x install-requirements.sh && bash install-requirements.sh && clear")
        print(colored("The first installer can install Debian, Kali Linux, Ubuntu, Arch Linux, Manjaro, Fedora, Void, Alpine, BackBox, CentOS, openSUSE", 'grey', 'on_blue'))
        print(colored("---------------------------------------------", 'grey', 'on_blue'))
        print(colored("The second installer can install Debian, Kali Linux, Ubuntu, Manjaro, Parrot, Arch, Alpine, Fedora, Void", 'grey', 'on_blue'))
        print(colored("Select your system (1/2):", 'grey', 'on_white'))
        k = int(input())

        if k == 1:
            os.system("python3 linux.py && login")
        elif k == 2:
            os.system("python3 linux2.py && login")
elif a == 4:
    os.system("clear")
    print(colored("WARNING! FOR ANY USAGE OF THIS MODE, YOU NEED INITIALIZE IT", 'yellow', 'on_grey'))
    time.sleep(1)
    if os.path.exists("/root/STALIN-OS/.recovery"):
        print(colored("WARNING! YOU STARTED RECOVERY MODE! BE CAREFUL BECAUSE YOU CAN DESTROY SYSTEM!", 'yellow', 'on_grey'))
        print(" ")
        print(" ")
        print(colored("Select your script:", 'cyan', 'on_grey'))
        l = int(input())

        if l == 1:
            os.system("bash ~/../.recovery/script1.sh || bash login")
        elif l == 2:
            os.system("bash ~/../.recovery/script2.sh || bash login")
        elif l == 3:
            os.system("ls ~/../.recovery")
            print("Run your script:")
            m = input()
            os.system("bash ~/../.recovery/" + m + " && clear && login")
        elif l == 4:
            os.system("clear && login")
    else:
        print(colored("WARNING! THE RECOVERY MODE ISN'T INITIALIZED", 'yellow', 'on_grey'))
        time.sleep(2.5)
        os.system("clear && login")
