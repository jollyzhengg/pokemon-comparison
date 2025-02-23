import os
import re
from PIL import Image

# Folder containing the images

"""
# Folder containing the images
folder_path = "post-process-data/pokemon_jpg"

# Regular expression to match valid filenames (1.jpg to 151.jpg)
valid_pattern = re.compile(r"^(1[0-4][0-9]|15[0-1]|[1-9][0-9]?|[1-9])\.jpg$")

# Iterate through files in the folder
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    
    # Check if it's a file and doesn't match the valid pattern
    if os.path.isfile(file_path) and not valid_pattern.match(filename):
        os.remove(file_path)
"""
#USED MACBOOK REMOVE BACKGROUND FEATURE WHICH TURNED EVERYTHING INTO A PNG
folder_path = "post-process-data/pokemon_jpg"
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    
    # Check if it's a file
    if os.path.isfile(file_path):
        # Keep files with "Background Removed" in the filename and that are PNG
        if not (filename.endswith(".png") and "Background Removed" in filename):
            os.remove(file_path)
        else:
            number = filename.split(' ')[0]
            
            # Define the new filename
            new_filename = f"{number}.png"
            new_file_path = os.path.join(folder_path, new_filename)
            
            # Rename the file
            os.rename(file_path, new_file_path)