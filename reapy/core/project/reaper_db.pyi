
class ReaperDB:

    _reaper_path: str
    _conf_file: str
    _db_folder: str
    name2file: dict[str, str]

    def __init__(self, file: str) -> None:
        """
        """
        ...
    
    def _get_databases(self) -> dict[str, str]:
        """
        """
        ...
    
    def get_audio_filepath_from_db(self, db_name: str, file_name: str) -> str:
        """
        """
        ...

    def get_audiofiles_from_db(self, db_name: str) -> list[str]:
        """
        """
        ...
