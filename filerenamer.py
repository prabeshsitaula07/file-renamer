import os

def rename_files(directory):
    """Rename files in the given directory."""
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            new_filename = input(f"Enter new name for '{filename}': ")
            new_file_path = os.path.join(directory, new_filename)
            try:
                os.rename(file_path, new_file_path)
                print(f"File '{filename}' renamed to '{new_filename}'.")
            except OSError as e:
                print(f"Error renaming file '{filename}': {e}")


directory = input("Enter the directory path where the files are located: ")
rename_files(directory)
