import os

def create_folder(folder_path):
    """Create a folder if it doesn't already exist."""
    try:
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
    except Exception as e:
        print(f"Error creating folder '{folder_path}': {e}")
