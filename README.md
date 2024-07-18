# Auto Desktop Cleaner

Auto Desktop Cleaner is a simple tool to organize files on your desktop by categorizing them into folders based on their creation month/year and file type.

## Features

- Categorizes files into folders by creation month/year.
- Further categorizes files into subfolders by file type.
- Supports common file types such as Images, Videos, Documents, Audio, Archives, Scripts, and Others.
- Simple graphical user interface (GUI) for selecting the folder to organize.

## Requirements

- Python 3.x
- `tkinter` (Python's standard GUI package)

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/Aberto7/Auto-Desktop-Cleaner.git
    cd desktop_cleaner
    ```

2. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Run the application:
    ```sh
    python main.py
    ```

2. In the GUI, click the "Browse" button to select the folder you want to organize.

3. Click the "Organize" button to start organizing the files. The files will be moved to folders categorized by month/year and file type.

## Project Structure

```plaintext
desktop_cleaner/
├── cleaner/
│   ├── __init__.py
│   ├── file_categorizer.py
│   ├── folder_creator.py
│   ├── organizer.py
├── ui/
│   ├── __init__.py
│   ├── main_window.py
├── main.py
├── requirements.txt
├── README.md
