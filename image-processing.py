import os
import re

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

