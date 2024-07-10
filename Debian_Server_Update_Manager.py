import os
import sys, traceback

def main():
    print("Geben sie an was sie machen wollen: ")
    print("1: System aktualisieren\n2: Auf die nächste Distro Version wechseln")

    a = str(input("Geben die bitte an was sie machen wollen: "))
    if a == "1":
        ausfuehren(a)
    elif a == "2":
        ausfuehren(a)
    else:
        print("Fehlerhafte eingabe")


def ausfuehren(choice):
    if choice == "1":
        os.system("apt update")
        os.system("apt upgrade")

    elif choice == "2":
        os.system("apt dist-upgrade")

    else:
        return "Ungültige Eingabe"


main()