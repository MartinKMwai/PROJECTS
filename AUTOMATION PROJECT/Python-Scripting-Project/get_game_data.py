#time to automate the living fuck outta this bitch

import os 
import json #dealinmg with json files
import shutil #copy and overwrite on files. File operationms here
from subprocess import PIPE, run #run any terminal commands that we want
import sys #access to cmd args

def main(source, target):
    current_working_directory = os.getcwd()
    source_path = os.path.join(current_working_directory, source)
    #do not use string concatenations since rthe path dividwers are different depending on the os
    target_path = os.path.join(current_working_directory, target)

    


if __name__ == "__main__": #wanna implement the python script if we are running this file directly
    args = sys.argv

    if len(args)!=3: #1. Code file we want to run. 2. Source directory 3. Destination directory  
        raise Exception("Specify the source target directories only")

    source, target = args[1:] #start at index 1, ignore the file name
    main(source, target)





