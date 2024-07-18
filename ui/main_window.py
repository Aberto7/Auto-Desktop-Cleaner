import tkinter as tk
from tkinter import filedialog, messagebox
from Cleaner.organizer import move_files_to_folders

class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Desktop Cleaner")

        self.label = tk.Label(root, text="Select folder to organize:")
        self.label.pack(pady=10)

        self.select_button = tk.Button(root, text="Browse", command=self.browse_folder)
        self.select_button.pack(pady=5)

        self.organize_button = tk.Button(root, text="Organize", command=self.organize_folder, state=tk.DISABLED)
        self.organize_button.pack(pady=20)

    def browse_folder(self):
        self.folder_path = filedialog.askdirectory()
        if self.folder_path:
            self.organize_button.config(state=tk.NORMAL)
        else:
            self.organize_button.config(state=tk.DISABLED)

    def organize_folder(self):
        try:
            move_files_to_folders(self.folder_path)
            messagebox.showinfo("Success", "Files organized by month and file type.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

def main():
    root = tk.Tk()
    app = MainWindow(root)
    root.mainloop()

if __name__ == "__main__":
    main()
