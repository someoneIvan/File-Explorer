from pathlib import Path

def scan_folder(path: Path):
    total_files = 0
    total_dirs = 0

    try:
        for item in path.rglob("*"):
            if item.is_dir():
                total_dirs += 1
            else:
                total_files += 1
                
        print(f"\n--- Статистика папки {path.name} ---")
        print(f"Файлов: {total_files}")
        print(f"Папок: {total_dirs}\n")

    except PermissionError:
        print("Ошибка: Нет доступа к некоторым подпапкам.")