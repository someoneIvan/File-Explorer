from core.scan import scan
from core.actions import change_directory, user_help, file_list

from pathlib import Path
import shutil, os

if __name__ == "__main__":
    print("Welcome to File Explorer!\n")
    p = Path("/").resolve()
    while True:
        choise = input("Enter the command:")

        if choise == "help":
            user_help()
        elif choise == "ls":
            file_list(p)
        elif choise.startswith("cd "):
            target = choise[3:].strip()
            if not target:
                print("Use: cd <path>")
            else:
                p = change_directory(choise, p)
                print(f"Directory successfully changed to {p}")
        elif choise == "list":
            print(scan(p))
        elif choise == "del":
            choise_1 = input("Enter path:")
            try:
                os.remove(choise_1)
                print("File successfully deleted.")
            except (PermissionError, IsADirectoryError):
                shutil.rmtree(choise_1)
                print("Directory succesfuly deleted.")
        elif choise == "co":
            choise_1 = input("Enter source path:")
            choise_2 = input("Enter destination path:")

            try:
                shutil.copy2(choise_1, choise_2)
            except IsADirectoryError:
                shutil.copytree(choise_1, choise_2)
        elif choise == "mv":
            choise_1 = input("Enter source path:")
            choise_2 = input("Enter destination path:")

            shutil.move(choise_1, choise_2)
        elif choise == "open":
            choise_1 = p / input("Enter file name:")

            os.startfile(choise_1)
        elif choise in ["q", "exit", "quit"]:
            os.system("pause")
            break
        else:
            print('Unknown command. Type "help" to get available commands.')