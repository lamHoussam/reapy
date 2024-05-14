import os

class ReaperDB:
    def __init__(self, reaper_path: str):
        self._reaper_path = reaper_path
        self._conf_file = os.path.join(reaper_path, "REAPER.ini")
        self._db_folder = os.path.join(reaper_path, "MediaDB")
        self.name2file = {}

        self._get_databases()
    
    def _get_databases(self) -> dict:
        with open(self._conf_file, "r") as f:
            lines = f.readlines()

            shortcutTs = {}
            shortcuts = {}
            for line in lines:
                if line.startswith("ShortcutT"):
                    number = line[9]
                    shortcutTs[number] = line.split("=")[1].strip()
                elif line.startswith("Shortcut"):
                    number = line[8]
                    shortcuts[number] = line.split("=")[1].strip()
            
        for key, value in shortcutTs.items():
            self.name2file[value] = os.path.join(self._db_folder, shortcuts[key])
        
        print("DBs: ", self.name2file)
        return self.name2file

    