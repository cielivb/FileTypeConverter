""" Clear Result Images 
This script is to be used after performing GUI testing using the test
directory. It looks in every folder in the test directory, and removes all
non-txt files from these directories. Original test reference images in
the main directory are not affected. This script automates the post-testing
cleanup process.
"""

import os


def main():
    test_dir = os.path.dirname(__file__)
    
    for name in os.listdir(test_dir):
        directory = os.path.join(test_dir, name)
        
        if os.path.isdir(directory):
            # Remove all non-txt files and directories from directory
            for item in os.listdir(directory):
                
                # Keep text files
                if item.endswith('.txt') or item.endswith('.TXT'):
                    continue
                
                # Remove everything else
                os.remove(os.path.join(directory, item))
    


if __name__ == '__main__':
    main()