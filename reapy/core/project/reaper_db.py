import os
import random

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
    
    def get_audio_filepath_from_db(self, db_name: str, file_name: str) -> str:
        if db_name not in self.name2file:
            return None

        db_file = self.name2file[db_name]
        return_file_path = None
        with open(db_file, "r", encoding="utf-8") as f:
            lines = f.readlines()
            for line in lines:
                if line.startswith("FILE"):
                    return_file_path = line.split("\"")[1]
                if line.startswith("DATA") and "\"" in line:
                    file_name_in_line = line.split("\"", 2)[1]
                    splitted_file_name = file_name_in_line.split(":")
                    if splitted_file_name[0] == "t" and (file_name == splitted_file_name[1] or file_name + ".wav" == splitted_file_name[1]):
                        return return_file_path

        return None
    
    def get_audiofiles_from_db(self, db_name: str) -> list[str]:
        if db_name not in self.name2file:
            return None

        db_file = self.name2file[db_name]
        audio_files = []
        with open(db_file, "r", encoding="utf-8") as f:
            lines = f.readlines()
            for line in lines:
                if line.startswith("FILE"):
                    audio_files.append(line.split("\"")[1])
        
        return audio_files
    
    def get_random_file_from_db(self, db_name: str) -> str:
        audio_files = self.get_audiofiles_from_db(db_name)
        if audio_files is None:
            return None
        
        return random.choice(audio_files)
        
    def get_n_random_files_from_db(self, db_name: str, n: int) -> list[str]:
        audio_files = self.get_audiofiles_from_db(db_name)
        if audio_files is None or n > len(audio_files):
            return None
        
        return random.sample(audio_files, n)
    