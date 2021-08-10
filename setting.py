#!/usr/bin/env python3
#! -*- coding: utf-8 -*-
import os
from termcolor import colored
import time

os.system("clear")
print(colored("| === === === === === === === === |", 'grey', 'on_white'))
print(colored("| 1.Uninstall OS                  |", 'grey', 'on_white'))
print(colored("| 2.Change login                  |", 'grey', 'on_white'))
print(colored("| 3.Change password               |", 'grey', 'on_white'))
print(colored("| 4.Initialize recovery.          |", 'grey', 'on_white'))
print(colored("| 5.Add your script into recovery |", 'grey', 'on_white'))
print(colored("| 6.Exit to chroot menu           |", 'grey', 'on_white'))
print(colored("| === === === === === === === === |", 'grey', 'on_white'))
a = int(input())

if a == 1:
    print(colored("Are you seriously want uninstall OS? yes/no", 'yellow', 'on_grey'))
    b = input()

    if b == 'yes':
        os.system("bash ~/Termux-OS/system/uninstall.sh")
    elif b == 'no':
        os.system("python3 ~/Termux-OS/chroot/chroot.py")
elif a == 2:
    os.system("python3 ~/Termux-OS/chroot/chlogin.py")
    os.system("python3 ~/Termux-OS/chroot/chroot.py")
elif a == 3:
    os.system("python3 ~/Termux-OS/chroot/chpass.py")
    os.system("python3 ~/Termux-OS/chroot/chroot.py")
elif a == 4:
    os.system("bash ~/Termux-OS/.initialize/initialize.sh")
    time.sleep(5)
    os.system("python3 ~/Termux-OS/chroot/chroot.py")
elif a == 5:
    os.system("python3 ~/Termux-OS/.initialize/initialize.py")
    os.system("python3 ~/Termux-OS/chroot/chroot.py")
elif a == 6:
    os.system("python3 ~/Termux-OS/chroot/chroot.py")
