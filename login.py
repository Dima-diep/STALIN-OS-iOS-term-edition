#!/usr/bin/env python3
#! -*- coding: utf-8 -*-
import os

try:
    print("Your login: ")
    a = input()

    login = 'oldlogin'

    if a == login:
        os.system("python3 ~/STALIN-OS/boot/pass.py")
    elif a != login:
        os.system("python3 ~/STALIN-OS/boot/login.py")
except KeyboardInterrupt:
    os.system("python3 ~/STALIN-OS/boot/login.py")
