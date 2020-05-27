dict = {
    "0": "0011 0000",
    "1": "0011 0000",
    "2": "0011 0001",
    "3": "0011 0010",
    "4": "0011 0100",
    "5": "0011 0101",
    "6": "0011 0110",
    "7": "0011 0111",
    "8": "0011 1000",
    "9": "0011 1001",
    "A": "0100 0001",
    "B": "0100 0010",
    "C": "0100 0011",
    "D": "0100 0100",
    "E": "0100 0101",
    "F": "0100 0110",
    "G": "0100 0111",
    "H": "0100 1000",
    "I": "0100 1001",
    "J": "0100 1010",
    "K": "0100 1011",
    "L": "0100 1100",
    "M": "0100 1101",
    "N": "0100 1110",
    "O": "0100 1111",
    "P": "0101 0000",
    "Q": "0101 0001",
    "R": "0101 0010",
    "S": "0101 0011",
    "T": "0101 0100",
    "U": "0101 0101",
    "V": "0101 0110",
    "W": "0101 0111",
    "X": "0101 1000",
    "Y": "0101 1001",
    "Z": "0101 1010",
    "a": "0110 0001",
    "b": "0110 0010",
    "c": "0110 0011",
    "d": "0110 0100",
    "e": "0110 0101",
    "f": "0110 0110",
    "g": "0110 0111",
    "h": "0110 1000",
    "i": "0110 1001",
    "j": "0110 1010",
    "k": "0110 1011",
    "l": "0110 1100",
    "m": "0110 1101",
    "n": "0110 1110",
    "o": "0110 1111",
    "p": "0111 0000",
    "q": "0111 0001",
    "r": "0111 0010",
    "s": "0111 0011",
    "t": "0111 0100",
    "u": "0111 0101",
    "v": "0111 0110",
    "w": "0111 0111",
    "x": "0111 1000",
    "y": "0111 1001",
    "z": "0111 1010",
    ".": "0010 1110",
    ",": "0010 0111",
    ":": "0011 1010",
    ";": "0011 1011",
    "?": "0011 1111",
    "!": "0010 0001",
    "'": "0010 1100",
    '"': "0010 0010",
    "(": "0010 1000",
    ")": "0010 1001",
    " ": "0010 0000",
}

import os
from time import sleep
import getpass

def clear():
    os.system('cls')

def secret():
    clear()
    print("                                                 PRTS Rhodes Island")
    usr = input("Enter username : ")
    usr_pass = getpass.getpass("Enter Password : ")
    print("Checking...")
    sleep(5)
    if usr in "Adnachiel" and usr_pass in "1982":
        print("Secret revealed!\nNext version 2.0 will available soon with more features also some rewards!")
        sleep(2)
        clear()
        print("                                                 Text to Binary 1.0")
    else:
        clear()
        print("Wrong Username or Password!")
        sleep(1)
        clear()
        print("                                                 Text to Binary 1.0")


print("                                                 Text to Binary 1.0")
while True:
    try:
        for c in input("Enter Text : "):
            if (c in "0"):
                print(dict.get("0"), end=' ')
            if (c in "1"):
                print(dict.get("1"), end=' ')
            if (c in "2"):
                print(dict.get("2"), end=' ')
            if (c in "3"):
                print(dict.get("3"), end=' ')
            if (c in "4"):
                print(dict.get("4"), end=' ')
            if (c in "5"):
                print(dict.get("5"), end=' ')
            if (c in "6"):
                print(dict.get("6"), end=' ')
            if (c in "7"):
                print(dict.get("7"), end=' ')
            if (c in "8"):
                print(dict.get("8"), end=' ')
            if (c in "9"):
                print(dict.get("9"), end=' ')
            if (c in "A"):
                print(dict.get("A"), end=' ')
            if (c in "B"):
                print(dict.get("B"), end=' ')
            if (c in "C"):
                print(dict.get("C"), end=' ')
            if (c in "D"):
                print(dict.get("D"), end=' ')
            if (c in "E"):
                print(dict.get("E"), end=' ')
            if (c in "F"):
                print(dict.get("F"), end=' ')
            if (c in "G"):
                print(dict.get("G"), end=' ')
            if (c in "H"):
                print(dict.get("H"), end=' ')
            if (c in "I"):
                print(dict.get("I"), end=' ')
            if (c in "J"):
                print(dict.get("J"), end=' ')
            if (c in "K"):
                print(dict.get("K"), end=' ')
            if (c in "L"):
                print(dict.get("L"), end=' ')
            if (c in "M"):
                print(dict.get("M"), end=' ')
            if (c in "N"):
                print(dict.get("N"), end=' ')
            if (c in "O"):
                print(dict.get("O"), end=' ')
            if (c in "P"):
                print(dict.get("P"), end=' ')
            if (c in "Q"):
                print(dict.get("Q"), end=' ')
            if (c in "R"):
                print(dict.get("R"), end=' ')
            if (c in "S"):
                print(dict.get("S"), end=' ')
            if (c in "T"):
                print(dict.get("T"), end=' ')
            if (c in "U"):
                print(dict.get("U"), end=' ')
            if (c in "V"):
                print(dict.get("V"), end=' ')
            if (c in "W"):
                print(dict.get("W"), end=' ')
            if (c in "X"):
                print(dict.get("X"), end=' ')
            if (c in "Y"):
                print(dict.get("Y"), end=' ')
            if (c in "Z"):
                print(dict.get("Z"), end=' ')
            if (c in "a"):
                print(dict.get("a"), end=' ')
            if (c in "b"):
                print(dict.get("b"), end=' ')
            if (c in "c"):
                print(dict.get("c"), end=' ')
            if (c in "d"):
                print(dict.get("d"), end=' ')
            if (c in "e"):
                print(dict.get("e"), end=' ')
            if (c in "f"):
                print(dict.get("f"), end=' ')
            if (c in "g"):
                print(dict.get("g"), end=' ')
            if (c in "h"):
                print(dict.get("h"), end=' ')
            if (c in "i"):
                print(dict.get("i"), end=' ')
            if (c in "j"):
                print(dict.get("j"), end=' ')
            if (c in "k"):
                print(dict.get("k"), end=' ')
            if (c in "l"):
                print(dict.get("l"), end=' ')
            if (c in "m"):
                print(dict.get("m"), end=' ')
            if (c in "n"):
                print(dict.get("n"), end=' ')
            if (c in "o"):
                print(dict.get("o"), end=' ')
            if (c in "p"):
                print(dict.get("p"), end=' ')
            if (c in "q"):
                print(dict.get("q"), end=' ')
            if (c in "r"):
                print(dict.get("r"), end=' ')
            if (c in "s"):
                print(dict.get("s"), end=' ')
            if (c in "t"):
                print(dict.get("t"), end=' ')
            if (c in "u"):
                print(dict.get("u"), end=' ')
            if (c in "v"):
                print(dict.get("v"), end=' ')
            if (c in "w"):
                print(dict.get("w"), end=' ')
            if (c in "x"):
                print(dict.get("x"), end=' ')
            if (c in "y"):
                print(dict.get("y"), end=' ')
            if (c in "z"):
                print(dict.get("z"), end=' ')
            if (c in "."):
                print(dict.get("."), end=' ')
            if (c in ","):
                print(dict.get(","), end=' ')
            if (c in ":"):
                print(dict.get(":"), end=' ')
            if (c in ";"):
                print(dict.get(";"), end=' ')
            if (c in "?"):
                print(dict.get("?"), end=' ')
            if (c in "!"):
                print(dict.get("!"), end=' ')
            if (c in "'"):
                print(dict.get("'"), end=' ')
            if (c in '"'):
                print(dict.get('"'), end=' ')
            if (c in "("):
                print(dict.get("("), end=' ')
            if (c in ")"):
                print(dict.get(")"), end=' ')
            if (c in " "):
                print(dict.get(" "), end=' ')
            if (c in "+"):
                secret()

    except Exception as e:
        print(e)