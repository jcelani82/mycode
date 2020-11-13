#!/usr/bin/env python3

# The following line will create the directory if it does not exist already

import shutil
import os

# Starting directory
os.chdir("/Users/johncelani/Documents/School/Python_Class/mycode/")

# Copy a Single File
shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy")

# Copy an Entire Directory
shutil.copytree("5g_research/", "5g_research_backup/")

