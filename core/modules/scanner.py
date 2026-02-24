from pathlib import Path

def scan(pathscan):
    if not (Path.exists and Path.is_dir):
        raise OSError("Error. Path not found.")
    else:
        try:
            for item in Path(pathscan).iterdir():
                if item.is_file:
                    pass
                elif item.is_dir:
                    pass
                else:
                    raise OSError("Unknown unique in directory.")
        except Exception as e:
            return f"Unknown error: {e}"

if __name__ == "__main__":
    pathscan = input(f"Test directory path: ")
    scan(pathscan)