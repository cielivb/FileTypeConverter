""" Clear Result Images 
This script is to be used after performing GUI testing using the test
directory. It looks in every folder in the test directory, and removes all
non-txt files from these directories. Original test reference images in
the main directory are not affected. This script automates the post-testing
cleanup process.
"""

import os

