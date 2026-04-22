from pathlib import Path

def scan(pathscan):

    result = []

    if isinstance(pathscan, str):
        pathscan = Path(pathscan)
    elif not isinstance(pathscan, Path):
        raise TypeError("Error. Incorrect path type.")

    if not (pathscan.exists() and pathscan.is_dir()):
        raise OSError("Error. Path not found.")
    else:
        try:
            for item in Path(pathscan).iterdir():
                if item.is_file():
                    namef = item.name
                    sizef = item.stat().st_size
                    formatf = item.suffix

                    result.append({
                        "name" : namef,
                        "size" : sizef,
                        "format" : formatf,
                        "type" : "file"
                    })

                elif item.is_dir():
                    named = item.name
                    sized = item.stat().st_size
                    formatd = ""
                    
                    result.append({
                        "name" : named,
                        "size" : sized,
                        "format" : formatd,
                        "type" : "directory"
                    })
                else:
                    raise OSError("Unknown item in directory.")
            return result
        except Exception as e:
            return f"Unknown error: {e}"