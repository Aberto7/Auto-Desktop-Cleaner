import os
import shutil
from Cleaner.file_categorizer import get_creation_month_year, get_file_type, FILE_TYPES
from Cleaner.folder_creator import create_folder

def move_files_to_folders(source_folder):
    """Move files to folders categorized by month/year and file type."""
    try:
        files = os.listdir(source_folder)
        
        for file_name in files:
            source = os.path.join(source_folder, file_name)
            
            if os.path.isfile(source):
                try:
                    file_extension = os.path.splitext(file_name)[1].lower()
                    month_year_folder = get_creation_month_year(source)
                    file_type_folder = get_file_type(file_extension)
                    
                    destination_folder_path = os.path.join(source_folder, month_year_folder, file_type_folder)
                    create_folder(destination_folder_path)
                    
                    destination = os.path.join(destination_folder_path, file_name)
                    shutil.move(source, destination)
                except Exception as e:
                    print(f"Error moving file '{file_name}' to '{destination_folder_path}': {e}")
            
            elif os.path.isdir(source) and file_name not in FILE_TYPES.keys():
                try:
                    month_year_folder = get_creation_month_year(source)
                    destination_folder_path = os.path.join(source_folder, month_year_folder, "Folders")
                    create_folder(destination_folder_path)
                    
                    destination = os.path.join(destination_folder_path, file_name)
                    shutil.move(source, destination)
                except Exception as e:
                    print(f"Error moving folder '{file_name}' to '{destination_folder_path}': {e}")

    except Exception as e:
        print(f"Error accessing source folder '{source_folder}': {e}")
