import os
import shutil

DOWNLOADS = os.path.join(os.path.expanduser("~"), "Downloads")

def move_files_back_to_folders(downloads_folder):
    # Get all folder names in Downloads
    folders = [f for f in os.listdir(downloads_folder) if os.path.isdir(os.path.join(downloads_folder, f))]
    
    # Get all files in the root of Downloads
    files = [f for f in os.listdir(downloads_folder) if os.path.isfile(os.path.join(downloads_folder, f))]
    
    for file in files:
        file_path = os.path.join(downloads_folder, file)
        
        # Try to find a folder that matches file name or prefix
        moved = False
        for folder in folders:
            folder_path = os.path.join(downloads_folder, folder)
            
            # Example heuristic: if filename contains folder name or vice versa
            # Adjust this logic based on your file/folder naming
            if folder.lower() in file.lower() or file.lower().startswith(folder.lower()):
                dest_path = os.path.join(folder_path, file)
                try:
                    print(f"Moving '{file}' to folder '{folder}'")
                    shutil.move(file_path, dest_path)
                    moved = True
                    break
                except Exception as e:
                    print(f"Failed to move '{file}' to '{folder}': {e}")
        
        if not moved:
            # File doesn't seem to belong to any folder, leave it as is
            print(f"Leaving '{file}' in Downloads root")
            
    print("✅ Finished moving files back to folders where possible.")

if __name__ == "__main__":
    move_files_back_to_folders(DOWNLOADS)
