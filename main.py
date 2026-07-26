from pathlib import Path
import os
import shutil
import sys

from core.actions import change_directory, user_help, file_list, open_file
from core.scanmdl import scan_folder


if __name__ == "__main__":
    print("Welcome to File Explorer!\n")
    p = Path.cwd() # Начинаем с текущей рабочей директории

    while True:
        try:
            choise = input(f"\n[{p}] > ").strip()

            if not choise:
                print('Empty command. Use "help" to get command list')
                continue

            if choise == "help":
                user_help()

            elif choise == "ls":
                file_list(p)

            elif choise.startswith("cd "):
                target = choise[3:].strip()
                if not target:
                    print("Use: cd <path>")
                else:
                    p = change_directory(target, p)
                    file_list(p)

            elif choise == "del":
                target_str = input("Enter path to delete: ").strip()
                target_path = (p / target_str).resolve() if not Path(target_str).is_absolute() else Path(target_str)

                if not target_path.exists():
                    print("Error: File or directory does not exist.")
                    continue

                try:
                    if target_path.is_dir():
                        shutil.rmtree(target_path)
                        print("Directory successfully deleted.")
                    else:
                        target_path.unlink()
                        print("File successfully deleted.")
                except Exception as e:
                    print(f"Error deleting target: {e}")

            elif choise == "co":
                src = input("Enter source path: ").strip()
                dst = input("Enter destination path: ").strip()

                src_path = (p / src).resolve()
                dst_path = (p / dst).resolve()

                try:
                    if src_path.is_dir():
                        shutil.copytree(src_path, dst_path)
                    else:
                        shutil.copy2(src_path, dst_path)
                    print("Copied successfully.")
                except Exception as e:
                    print(f"Copy error: {e}")

            elif choise == "mv":
                src = input("Enter source path: ").strip()
                dst = input("Enter destination path: ").strip()

                src_path = (p / src).resolve()
                dst_path = (p / dst).resolve()

                try:
                    shutil.move(src_path, dst_path)
                    print("Moved successfully.")
                except Exception as e:
                    print(f"Move error: {e}")

            elif choise == "open":
                filename = input("Enter file name: ").strip()
                target_path = (p / filename).resolve()

                if target_path.exists():
                    open_file(target_path)
                else:
                    print("Error: File does not exist.")

            elif choise == "open":
                filename = input("Enter file name: ").strip()
                target_path = (p / filename).resolve()

                if target_path.exists():
                    open_file(target_path)
                else:
                    print("Error: File does not exist.")

            elif choise in ["q", "exit", "quit"]:
                print("Goodbye!")
                break

            else:
                print('Unknown command. Type "help" to get available commands.')

        except KeyboardInterrupt:
            print("\nUse 'exit' or 'q' to quit.")
            break