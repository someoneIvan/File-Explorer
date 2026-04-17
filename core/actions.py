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
    print("""
FILE EXPLORER COMMANDS
======================

help                - Show this help message.

ls                  - List files and directories in the current directory (simple view).

list                - List files and directories in the current directory (detailed view, same as scan()).

cd <path>           - Change current directory to <path>. The path can be relative or absolute.
                      Example: cd Documents, cd /home/user

del                 - Delete a file or directory. You will be prompted to enter the path.
                      Files are removed with os.remove(), directories with shutil.rmtree().

co                  - Copy a file or directory. Prompts for source and destination paths.
                      Uses shutil.copy2() for files, shutil.copytree() for directories.

mv                  - Move a file or directory. Prompts for source and destination paths.
                      Uses shutil.move().

open <filename>     - Open a file with its default application (Windows only, uses os.startfile).
                      The file is looked up in the current directory.

q, exit, quit       - Exit the File Explorer (pauses the console before closing).

NOTES:
- The current directory is initially set to the root ("/").
- For 'cd', the path is appended to the current directory. Example: if current is /home, "cd user" goes to /home/user.
- If a command fails (e.g., file not found, permission denied), an error message is shown.
- Use relative paths where possible, or absolute paths starting with / or drive letter (Windows).
""")

def file_list(pathdirectory):
    files = os.listdir(pathdirectory)
    total_size = 0

    for i in range(len(files)):
        filename = files[i]
        time = datetime.datetime.fromtimestamp(os.path.getmtime(os.path.join(pathdirectory, filename)))
        print(f"{i + 1}. {filename} | Дата создания: {time}")
        total_size += os.path.getsize(os.path.join(pathdirectory, filename))

    print(f"\nSuccessfully completed.\nTotal directory size: {total_size // (8 * 1024)} KB.\nCount of files: {i + 1}.")