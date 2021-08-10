#!/usr/bin/env python3
#! -*- coding: utf-8 -*-
import os
from termcolor import colored
import time

if os.file.exists("/home/STALIN-OS/.recovery"):
    print("What script do you want load to recovery?")
    print("If your script isn't bash, then make bash script for running it!")
    a = input()
    os.system("mv " + a + " ~/STALIN-OS/.recovery")
    os.system("python3 ~/STALIN-OS/chroot.py")
else:
    print(colored("WARNING! THE RECOVERY MODE ISN'T INITIALIZED", 'yellow', 'on_grey'))
    time.sleep(2.5)
    os.system("python3 ~/STALIN-OS/chroot.py")
