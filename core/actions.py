from pathlib import Path
import os, datetime

def change_directory(almost_new_location, current_path):
    almost_new_location = almost_new_location.strip()
    if not almost_new_location or almost_new_location == ".":
        return current_path
    elif almost_new_location == "..":
        new_location = current_path.parent
        return new_location
    else:
        new_location = current_path / almost_new_location
        if new_location.exists():
            if new_location.is_dir():
                return new_location
        else:
            print(f"Directory can't be changed. Path changing error.")
            return current_path
        
def user_help():
    print("Later... :D")

def file_list(pathdirectory):
    files = os.listdir(pathdirectory)
    total_size = 0

    for i in range(len(files)):
        filename = files[i]
        time = datetime.datetime.fromtimestamp(os.path.getmtime(os.path.join(pathdirectory, filename)))
        print(f"{i + 1}. {filename} | Дата создания: {time}")
        total_size += os.path.getsize(os.path.join(pathdirectory, filename))

    print(f"\nУспешно выполнено.")
    print(f"\nОбщий размер директории: {total_size // (8 * 1024)} Кб\n")
    print(f"Количество файлов: {i + 1}")