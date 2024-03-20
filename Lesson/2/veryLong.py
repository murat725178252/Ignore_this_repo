
import os
os.system("pip install colorama")
import colorama
import random

PasswordChars = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "@",
    "-",
    "_",
    "*",
    "?",
    "!",
    "%",
    "^",
    ".",
    "#",
    "$",
    ">",
    "<",
    "/",
    "&",
    "+",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "0",
]
Password = ""

def CreatePassword(Len: int):
    global Password
    for _ in range(PasswordLen):

        i = random.choice(PasswordChars)

        Password = Password + i

print(colorama.Fore.YELLOW + "---- Password Creator ----")
while True:
    PasswordLen = int(input(colorama.Fore.YELLOW + "Enter Password Length >>>"))
    CreatePassword(PasswordLen)
    print("Password : '" + Password + "'")