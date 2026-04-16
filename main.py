from core.scan import scan
from core.action import change_directory, user_help

from pathlib import Path
import shutil, os

if __name__ == "__main__":
    print("Welcome to File Explorer!\n")
    while True:
        p = Path.home()
        p_1 = scan(p)
        print(f"{p_1}\n")
        choise = input("Enter the command:")

        if choise == "help":
            user_help()
        elif choise == "cd":
            try:
                p = change_directory(p / ' '.join(choise[1:]))
            except:
                p = choise[1:]
            print(scan(p))
        elif choise == "list":
            print(scan(p))
        elif choise == "delete":
            choise_1 = input("Enter path:")

            try:
                os.remove(choise_1)
            except PermissionError or IsADirectoryError:
                shutil.rmtree(choise_1)
        elif choise == "copy":
            choise_1 = input("Enter source path:")
            choise_2 = input("Enter destination path:")

            try:
                shutil.copy2(choise_1, choise_2)
            except IsADirectoryError:
                shutil.copytree(choise_1, choise_2)
        elif choise == "move":
            choise_1 = input("Enter source path:")
            choise_2 = input("Enter destination path:")

            shutil.move(choise_1, choise_2)
        elif choise == "open":
            choise_1 = p / input("Enter file name:")

            os.startfile(choise_1)