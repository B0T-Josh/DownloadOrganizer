#Import os class. subprocess class
import os as o 
import subprocess as s

#Constant variables for file filtering
CATEGORIES = {
    "Documents": [".txt", ".md", ".rtf", ".log", ".csv", ".tsv", ".yml", ".ini",
                    ".doc", ".docx", ".dot", ".dotx", ".xls", ".xlsx", ".xlsm", ".xltx", ".ppt", ".pptx", ".pps", ".ppsx",
                    ".odt", ".ods", ".odp", ".odg", ".ott",
                    ".pdf", ".ps", ".ai", ".indd", ".idml", ".epub", ".mobi", ".azw3",
                    ".tex", ".bib", ".dif", ".xps"],
    "Programming": [".py", ".js", ".ts", ".jsx", ".tsx", ".java", ".c", ".cpp", ".h", ".hpp", ".cs", ".go", 
                    ".rb", ".php", ".swift", ".kt", ".kts", ".rs", ".lua", ".sh", ".bat", ".ps1", ".pl", 
                    ".r", ".m", 
                    ".yml", ".md", ".ipynb"],
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".svg", ".ico", ".webp", ".heic", ".psd", ".raw"],
    "Audio": [".mp3", ".wav", ".ogg", ".flac", ".aac", ".m4a", ".wma", ".mid", ".aiff"],
    "Videos": [".mp4", ".avi", ".mkv", ".mov", ".wmove", ".flv", ".webm", ".3gp", ".mpeg"],
    "Compressed": [".zip", ".rar", ".7z", ".tar", ".gz", ".bz2", ".xz", ".iso", ".cab"],
    "Executable": [".exe", ".msi", ".bat", ".sh", ".bin", ".dll", ".sys", ".apk", ".deb", ".rpm", ".cmd"],
    "Database": [".db", ".sqlite", ".mdb", ".accdb", ".sql", ".dbf"],
    "Websites": [".html", ".htm", ".css", ".js", ".ts", ".php", ".asp", ".aspx", ".jsp", ".vue", ".json", ".xml"],
    "Configurations": [".ini", ".cfg", ".conf", ".env", ".yaml", ".yml", ".toml", ".properties"],
    "Data": [".pkl", ".npy", ".npz", ".h5", ".parquet", ".sav", ".mat"]
}

def findDownloads() -> str:
    try:
        path: str = s.run("cd", shell=True, capture_output=True, text=True).stdout
        final_path: str = ""
        counter: int = 0
        for c in path:
            if counter < 3:
                final_path += c
            else: break
            if c == "\\": counter += 1
        
        return final_path + "\\Downloads"
    except:
        None

#Function to read download directory files
def contents() -> list[str]:
    try:
        o.chdir(findDownloads())
    except:
        print("Change directory unsuccessful")
        return []
        
    contents: list[str] = s.run("dir /b", shell=True, capture_output=True, text=True).stdout.replace(" ", "|").split()
    return contents

def moveFile(file: str, destination: str) -> bool:
    dir: str = destination
    exist: bool = o.path.isdir(dir)
    if not exist:
        o.makedirs(dir)
        print("Folder successfully created")
        try:
            s.run("move {} {}".format("\"" + file.replace("|", " ") + "\"", dir), shell=True, capture_output=True, text=True)
            return True
        except: 
            print("Failed to move {} to {}".format("\"" + file.replace("|", " ") + "\"", dir))
            return False
    else:
        try:
            s.run("move {} {}".format("\"" + file.replace("|", " ") + "\"", dir), shell=True, capture_output=True, text=True)
            return True
        except: 
            print("Failed to move {} to {}".format("\"" + file.replace("|", " ") + "\"", dir))
            return False

def getFileCategory(ext: str) -> str:
    category = next((key for key, values in CATEGORIES.items() if ext in values), None)
    return category
    
#Function to create folders for the files 
def filter() -> int:
    try:
        files: list[str] = contents()
        if len(files) < 1: return 0
        for file in files:
            try:
                index: int = file.index(".")
                ext: str = file[index:]
                category: str = getFileCategory(ext)
                if moveFile(file, category):
                    continue
                else:
                    return 0
            except:
                continue
    except:
        return 0
    return 1            
                
def main() -> int:
    if filter() > 0:
        return 1
    else:
        return 0
                    
if __name__ == "__main__":
    if main() > 0:
        print("Organization successful")
    else: 
        print("Organization unsuccessful")