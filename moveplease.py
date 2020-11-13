#!/usr/bin/env python3

# The following line will rename a file

import shutil
import os

# Starting Directory
os.chdir('/Users/johncelani/Documents/School/Python_Class/mycode')

# Move file to destination
shutil.move('raynor.obj', 'ceph_storage/')

# Prompt User for a new name for the kerrigan.obj file
xname = input('What is the new name for kerrigan.obj? ')

# Rename the file with the user input
shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)

