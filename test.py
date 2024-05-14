# from reapy import Project
import reapy


def create_tracks_with_audio(audio_file_paths):
    project = reapy.Project()  # This will reference the current project
    for i, file_path in enumerate(audio_file_paths):
        track = project.add_track(index=i, name=f"Track {i+1}")
        track.add_item(start=0, length=10)  # Create an item with a specific length, adjust as needed
        # Import the audio file into the track
        # project.import_media_into_track(filepath=file_path, track_id=track.index)

def test_get_dbs():
    reaper_path = "C:\\Users\\houss\\AppData\\Roaming\\REAPER"
    db = reapy.ReaperDB(reaper_path)
    # file = db.get_audio_filepath_from_db("DB_Test_01", "NP01 0001 Trans motorcycle pass.wav")
    files = db.get_audiofiles_from_db("DB_Test_01")
    print('\n'.join(files))

# List of audio file paths

# DB_Test_01

audio_file_paths = [
    "C:\\Users\\houss\\Desktop\\Boom\\NP01 0001 Trans motorcycle pass-converted.wav",
    "C:\\Users\\houss\\Desktop\\Boom\\NP01 0002 Trans car pass cobblestone-converted.wav",
    # "C:\\Users\\houss\\Desktop\\Boom\\.wav",
    # "C:\\Users\\houss\\Desktop\\Boom\\.wav",
    # "C:\\Users\\houss\\Desktop\\Boom\\.wav"  
]

# create_tracks_with_audio(audio_file_paths)
test_get_dbs()
