import os
import shutil

GREEN = '\033[92m'
RED = '\033[91m'
RESET = '\033[0m'
text = "\r\n░░█ █ █▄░█ ▀▄▀ ▀▄▀ █▄▄ █▄▄\r\n█▄█ █ █░▀█ █░█ █░█ █▄█ █▄█"
text1 = "Multiple File Search"
print(GREEN + text + RESET)
print(RED + text1 + RESET)



search_text = input("Search word: ")
search_directory = input("Input Path: ")
destination_directory = input("Output path: ")
move = input("Enter 'y' for move or 'n' for copy: ")
saved_files = 0  # Initialize saved_files to 0

if move == "y":
    for filename in os.listdir(search_directory):
        filepath = os.path.join(search_directory, filename)
        if os.path.isfile(filepath):
            try:
                with open(filepath, 'rb') as file:
                    file_content = file.read().lower()  # Read content and convert to lowercase
                    if search_text.lower().encode('utf-8') in file_content:
                        shutil.move(filepath, os.path.join(destination_directory, filename.lower()))
                        saved_files += 1
                        print(f"{filepath} Saved.")
            except Exception as e:
                print(f"Error processing file {filepath}: {str(e)}")

    print(f"Saved {saved_files} files.")
else:
    for filename in os.listdir(search_directory):
        filepath = os.path.join(search_directory, filename)
        if os.path.isfile(filepath):
            try:
                with open(filepath, 'rb') as file:
                    file_content = file.read().lower()  # Read content and convert to lowercase
                    if search_text.lower().encode('utf-8') in file_content:
                        shutil.copy(filepath, os.path.join(destination_directory, filename.lower()))
                        saved_files += 1
                        print(f"{filepath} Saved.")
            except Exception as e:
                print(f"Error processing file {filepath}: {str(e)}")

    print(f"Saved {saved_files} files.")