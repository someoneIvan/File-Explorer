from pathlib import Path
import os
import shutil
import subprocess
import platform


def user_help():
    print("""
Доступные команды:
  ls          - Показать файлы в текущей папке
  cd <path>   - Перейти в директорию (напр. cd .. или cd my_folder)
  del         - Удалить файл или папку
  co          - Скопировать файл или папку
  mv          - Переместить / переименовать
  open        - Открыть файл в системе
  q / exit    - Выйти из программы
""")


def file_list(path: Path):
    print(f"\nСодержимое директории: {path}")
    print("-" * 40)
    try:
        for item in path.iterdir():
            prefix = "[DIR] " if item.is_dir() else "      "
            print(f"{prefix}{item.name}")
    except PermissionError:
        print("Ошибка: Нет доступа к этой папке.")
    print("-" * 40)


def change_directory(target: str, current_path: Path) -> Path:
    new_path = (current_path / target).resolve()
    if new_path.exists() and new_path.is_dir():
        return new_path
    else:
        print(f"Ошибка: Директория '{target}' не найдена!")
        return current_path


def open_file(filepath: Path):
    """Кроссплатформенное открытие файла"""
    system_name = platform.system()
    
    if system_name == "Windows":
        os.startfile(filepath)
    elif system_name == "Darwin":  # macOS
        subprocess.run(["open", str(filepath)], check=False)
    else:  # Linux
        subprocess.run(["xdg-open", str(filepath)], check=False)