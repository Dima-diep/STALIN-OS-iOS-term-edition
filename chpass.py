#!/usr/bin/env python3
#! -*- coding: utf-8 -*-

print("Old pass:")
a = input()
print("New pass:")
b = input()

with open("~/Termux-OS/pass.py", "r") as f:
    raw = f.read().lower().replace(a, b)
    file = open("~/Termux-OS/pass.py", "w")
    file.write(raw)
    file.close()
    f.close()
