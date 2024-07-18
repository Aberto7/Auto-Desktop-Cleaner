import os
from datetime import datetime

# Define file type categories
FILE_TYPES = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'],
    'Videos': ['.mp4', '.mov', '.avi', '.mkv', '.flv', '.wmv'],
    'Documents': ['.pdf', '.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx', '.txt'],
    'Audio': ['.mp3', '.wav', '.aac', '.flac', '.ogg'],
    'Archives': ['.zip', '.rar', '.7z', '.tar', '.gz'],
    'Scripts': ['.py', '.js', '.html', '.css', '.java', '.c', '.cpp'],
    'Others': []
}

def get_creation_month_year(file_path):
    """Get the creation month and year of a file."""
    timestamp = os.path.getctime(file_path)
    creation_date = datetime.fromtimestamp(timestamp)
    return creation_date.strftime("%B %Y")

def get_file_type(file_extension):
    """Get the file type category based on its extension."""
    for category, extensions in FILE_TYPES.items():
        if file_extension in extensions:
            return category
    return 'Others'
