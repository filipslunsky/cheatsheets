import os

folder_path = os.getcwd()

print(f"Listing all files in: {folder_path}\n")

for filename in os.listdir(folder_path):
    full_path = os.path.join(folder_path, filename)
    if os.path.isfile(full_path):
        print("File:     ", filename)
    elif os.path.isdir(full_path):
        print("Folder:   ", filename)