""" Clear Result Images 
This script is to be used after performing GUI testing using the test
directory. It looks in every folder in the test directory and subdirectories,
and removes all non-txt files from these directories. Original test reference
images in the main directory are not affected. This script automates the
post-testing cleanup process.
"""

import os


def clean_directory(path):
    """ Iteratively delete non-text files in path and its subdirectories """
    
    # Categorise items in path directory into files and subdirectories
    files, subdirs = [], []
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        if os.path.isfile(item_path):
            files.append(item_path)
        else:
            subdirs.append(item_path)
    
    if path != os.path.dirname(__file__): # Skip this section to keep ref images
        # Remove non-text files from current directory        
        for file in files:
            if not item.endswith('.txt') and not item.endswith('.TXT'):
                os.remove(file)
    
    # Remove non-text files from subdirectories
    for subdir in subdirs:
        clean_directory(subdir)
    


def main():
    test_dir = os.path.dirname(__file__)
    clean_directory(test_dir)


if __name__ == '__main__':
    main()