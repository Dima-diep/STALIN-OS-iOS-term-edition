#!/usr/bin/env python3
#! -*- coding: utf-8 -*-
import os
import getpass

try:
    a = getpass.getpass("Your pass:" )

    passwd = 'oldpass'

    if a == passwd:
        os.system("python3 ~/Termux-OS-iOS/chroot.py")
    elif a != passwd:
        os.system("python3 ~/Termux-OS-iOS/login.py")
except KeyboardInterrupt:
    os.system("python3 ~/Termux-OS-iOS/login.py")
