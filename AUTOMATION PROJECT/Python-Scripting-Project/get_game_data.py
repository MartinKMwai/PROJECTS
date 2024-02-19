#time to automate the living fuck outta this bitch

import os 
import json #dealinmg with json files
import shutil #copy and overwrite on files. File operationms here
from subprocess import PIPE, run #run any terminal commands that we want
import sys #access to cmd args

GAME_DIR_PATTERN ="game" 


def find_all_game_paths(source):
    game_paths = []

    for root, dirs, files in os.walk(source):#we are walking the source path
        for directory in dirs:
            if GAME_DIR_PATTERN in directory.lower():
                path = os.path.join(source, directory)
                game_paths.append(path)
                
        break #we do not need to go deeper than the first level of the source directory.

    return game_paths    


def create_directory(path):
    if not os.path.exist(path):
        os.mkdir(path)

def main(source, target):
    current_working_directory = os.getcwd()
    source_path = os.path.join(current_working_directory, source)
    #do not use string concatenations since rthe path dividwers are different depending on the os
    target_path = os.path.join(current_working_directory, target)
    path_to_games = find_all_game_paths(source_path)
    create_directory(target_path)

    print(path_to_games)



'''We are using the function below so that this only runs when we are running the script itself, 
rather than when we are importing functions from here to other files'''

if __name__ == "__main__": #wanna implement the python script if we are running this file directly
    args = sys.argv

    if len(args)!=3: #1. Code file we want to run. 2. Source directory 3. Destination directory  
        raise Exception("Specify the source target directories only")

    source, target = args[1:] #start at index 1, ignore the file name
    main(source, target)





