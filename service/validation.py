#!/usr/bin/env python
# coding: utf-8

# Created by Noskov Alexey
# version
# 22.09.2019 - 1.0.0 - Релиз

from termcolor import colored, cprint

def bool(x, isPrint = True):
    if x == True :
        if isPrint:
            cprint("YES", 'grey', 'on_green')
        else :
            return colored("YES", 'grey', 'on_green')
    else :
        if isPrint:
            cprint ("NO", 'grey', 'on_red')
        else :
            return colored("NO", 'grey', 'on_red')
        
def boolReverse(x, isPrint = True):
    if x == True :
        if isPrint:
            cprint("YES", 'grey', 'on_red')
        else :
            return colored("YES", 'grey', 'on_red')
    else :
        if isPrint:
            cprint ("NO", 'grey', 'on_green')
        else :
            return colored("NO", 'grey', 'on_green')
        
def UF(x, isPrint = True):
    if x < 0.95 :
        if isPrint:
            cprint("OK", 'grey', 'on_green')
        else :
            return colored("OK", 'grey', 'on_green')
                
    elif x >= 1.0 :
        if isPrint:
            cprint ("NO", 'grey', 'on_red')
        else :
            return colored("NO", 'grey', 'on_red')
                
    else :
        if isPrint:
            cprint ("OK", 'grey', 'on_yellow')
        else :
            return colored("OK", 'grey', 'on_yellow')