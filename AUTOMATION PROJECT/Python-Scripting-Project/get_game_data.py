#time to automate the living fuck outta this bitch

import os 
import json #dealing with json files
import shutil #copy and overwrite on files. File operations here
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


'''Getting the names of the games, stripping their game tag and then loading the names onto a target'''

def get_name_from_paths(game_paths, stripped_tag): #target here?
    new_game_names = []
    for path in game_paths:
        _, dir_name = os.path.split(path) #do not use regex or other character-dependent methods, use built-in functions
        new_directory_name = dir_name.replace(stripped_tag, "")
        new_game_names.append(new_directory_name) 

    return new_game_names
        


def create_directory(path):
    if not os.path.exists(path):
        os.mkdir(path)

def copy_and_overwrite_names(source, destination):
    if os.path.exists(destination):
        shutil.rmtree(destination) #removes destination folder. Recursive delete
    shutil.copytree(source, destination) #copies the contents of the source into the destination
   
def make_json_metadata_file(path, game_directories):
    metadata = {
        "GameName": game_directories,
        "NumberOfGames": len(game_directories)
    }

    with open(path, "w") as file: #W = write and overwrite, r = read. Using "With" ensures the file closes once we exit the function
        json.dump(metadata, file, indent = 4)


def compiling_game_files(new_game_directories):
    pass


def main(source, target):
    current_working_directory = os.getcwd()
    source_path = os.path.join(current_working_directory, source)
    #do not use string concatenations since rthe path dividwers are different depending on the os
    target_path = os.path.join(current_working_directory, target)
    
    path_to_games = find_all_game_paths(source_path)

    new_game_directories = get_name_from_paths (path_to_games, "_game")

    create_directory(target_path)

    #we need to loop through all paths that we have, then run the copy and overwrite command
    for source, destination in zip(path_to_games, new_game_directories): #takes two lists, and creates tumples matching the values using their in-list indexes
        destination_path =  os.path.join(target_path, destination)
        copy_and_overwrite_names(source, destination_path)
        #RESUME HERE

    json_path = os.path.join(target_path, "metadata.json")

    make_json_metadata_file(json_path, new_game_directories)

  



'''We are using the function below so that this only runs when we are running the script itself, 
rather than when we are importing functions from here to other files'''

if __name__ == "__main__": #wanna implement the python script if we are running this file directly
    args = sys.argv

    if len(args)!=3: #1. Code file we want to run. 2. Source directory 3. Destination directory  
        raise Exception("Specify the source target directories only")

    source, target = args[1:] #start at index 1, ignore the file name
    main(source, target)





