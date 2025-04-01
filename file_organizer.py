import os
import shutil
import subprocess
#import ctypes  # For Windows

#Windows | Define the source and destination directories
#r"C:\Users\RonVallejo\Downloads"

# Windows | Define the source and destination directories
#DOWNLOADS_FOLDER = r"C:\Users\RonVallejo\Downloads"
#DESKTOP_FOLDER = r"C:\Users\RonVallejo\Desktop\Organized"

# macOS | Define the source and destination directories
DOWNLOADS_FOLDER = "/Users/ronvallejo86/Downloads"
DESKTOP_FOLDER = "/Users/ronvallejo86/Desktop/Organized"

# Define the file type categories and corresponding folders
FILE_TYPE_MAP = {
    "Images": ['.jpeg', '.jpg', '.png', '.gif', '.bmp', '.svg'],
    "Documents": ['.pdf', '.docx', '.doc', '.txt', '.xls', '.xlsx', '.ppt', '.pptx'],
    "Videos": ['.mp4', '.mov', '.avi'],
    "Music": ['.mp3', '.wav'],
    "Archives": ['.zip', '.tar', '.gz', '.rar', '.7z'],
    "Intro_Python": ['.py', '.js', '.sh', '.json', '.html', '.css'],
    "Others": []  # Catch-all for files without matching extensions
}

# Create directories for each category on the Desktop if they don't exist
for folder in FILE_TYPE_MAP.keys():
    folder_path = os.path.join(DESKTOP_FOLDER, folder)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

# Function to move files to their categorized folders
def move_file(file_path, filename):
    file_extension = os.path.splitext(filename)[1].lower()

    moved = False
    for folder, extensions in FILE_TYPE_MAP.items():
        if file_extension in extensions:
            shutil.move(file_path, os.path.join(DESKTOP_FOLDER, folder, filename))
            print(f"Moved {filename} to {folder} on Desktop")
            moved = True
            break

    # Move files with unknown extensions to the 'Others' folder
    if not moved:
        shutil.move(file_path, os.path.join(DESKTOP_FOLDER, "Others", filename))
        print(f"Moved {filename} to Others on Desktop")

# Function to recursively move files from folders to their categorized destinations
def move_files_in_folder(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            move_file(file_path, file)

# Function to organize and move the files and folders
def organize_files_and_folders():
    for item in os.listdir(DOWNLOADS_FOLDER):
        item_path = os.path.join(DOWNLOADS_FOLDER, item)

        # If it's a folder, move files inside it to their respective categories
        if os.path.isdir(item_path):
            print(f"Processing folder: {item}")
            move_files_in_folder(item_path)
            shutil.rmtree(item_path)  # Remove the folder after files have been moved
            print(f"Removed folder {item} after moving files")
        else:
            # If it's a file, categorize and move it
            move_file(item_path, item)

# Function to empty the Trash on macOS using AppleScript via osascript
def empty_trash():
    try:
        subprocess.run(['osascript', '-e', 'tell app "Finder" to empty'], check=True)
        print("Trash successfully emptied.")
    except subprocess.CalledProcessError:
        print("Failed to empty the Trash.")

#def empty_trash():
#    # SHEmptyRecycleBin function from shell32.dll
#    SHERB_NOCONFIRMATION = 0x00000001
#    SHERB_NOPROGRESSUI = 0x00000002
#    SHERB_NOSOUND = 0x00000004

#    result = ctypes.windll.shell32.SHEmptyRecycleBinW(None, None, SHERB_NOCONFIRMATION | #SHERB_NOPROGRESSUI | SHERB_NOSOUND)
#    if result == 0:
#        print("Recycle Bin successfully emptied.")
#    else:
#        print("Failed to empty the Recycle Bin.")        

if __name__ == "__main__":
    organize_files_and_folders()

    # After organizing, empty the Trash
    empty_trash()