from core.scan import scan
from core.action import change_directory, user_help

from pathlib import Path
import shutil, os

if __name__ == "__main__":
    print("Welcome to File Explorer!\n")
    while True:
        p = Path.home
        print(f"{scan(p)}\n")
        choise = input("Введите команду:")

        try:
            if choise == "help":
                user_help()
            elif choise[0] == "cd":
                p = change_directory(p, choise[:0])
                print(scan(p))
            elif choise == "list":
                print(scan(p))
            elif choise[0] = "del":
                try:
                    os.remove(os.path.join(p, choise[:0]))
                except PermissionError or IsADirectoryError:
                    shutil.rmtree(os.path.join(p, choise[:0]))
            elif