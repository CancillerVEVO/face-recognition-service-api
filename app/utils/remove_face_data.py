import os
from shutil import rmtree


def remove_face_data(path):
    try:
        print("🟢 Removing face data... 🗑️")
        if os.path.exists(path):
            rmtree(path)
            return None
        else:
            print("😵 Path does not exist")
            return None

    except Exception as e:
        print(e)
        print("Error: Could not remove face data")
        return False
