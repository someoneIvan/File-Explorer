from core.scan import scan
from core.action import change_directory

from pathlib import Path
import shutil

if __name__ == "__main__":
    print("Welcome to File Explorer!\n")
    while True:
        print(f"{scan(Path.home)}\nВведите команду:")