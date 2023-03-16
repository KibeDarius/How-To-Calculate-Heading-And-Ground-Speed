import os
import webbrowser
import pyfiglet
import csv
import time
import keyboard
import random
import pyfiglet
from colorama import init, Fore
import os
import pickle
import traceback

r = Fore.RED
lg = Fore.GREEN
rs = Fore.RESET
w = Fore.WHITE
cy = Fore.CYAN
ye = Fore.YELLOW
colors = [r, lg, w, ye, cy]
info = lg + '(' + w + 'i' + lg + ')' + rs
error = lg + '(' + r + '!' + lg + ')' + rs
success = w + '(' + lg + '*' + w + ')' + rs
INPUT = lg + '(' + cy + '~' + lg + ')' + rs
plus = lg + '(' + w + '+' + lg + ')' + rs


os.system("pip install --upgrade pip")
os.system("pip install tkinter")
os.system("pip install time")
os.system("pip install python-cfonts")
os.system("pip install get-mac")
os.system("pip install pyfiglet")
os.system("cls" if os.name=='nt' else 'clear')


print(random.choice(colors) + '                                              All Packages Installed Sucessfully   ' + rs)

print(random.choice(colors) + '                                              Thanks To Insominia Developers   ' + rs)


