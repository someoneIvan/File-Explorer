from pathlib import Path

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