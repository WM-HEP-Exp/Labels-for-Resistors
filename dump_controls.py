import os
import sys
import ast
import subprocess

def enumerate_folders(directory):
    data_folders = []
    first_level = filter(lambda x: os.path.isdir(directory + os.sep + x), os.listdir(directory))
    for d in first_level:
        data_folders.extend(map(lambda x: directory + os.sep + d + os.sep + x, os.listdir(directory + os.sep + d)))
    return data_folders

def get_resistances(data_folder):
    p1 = subprocess.run([sys.executable, __file__ + os.sep + "comp_analysis_modified.py", data_folder+"/M1", "1", "XX-XX-XXXX"], encoding="utf-8", capture_output=True)
    p2 = subprocess.run([sys.executable, __file__ + os.sep + "comp_analysis_modified.py", data_folder+"/M2", "2", "XX-XX-XXXX"], encoding="utf-8", capture_output=True)
    p3 = subprocess.run([sys.executable, __file__ + os.sep + "comp_analysis_modified.py", data_folder+"/M3", "3", "XX-XX-XXXX"], encoding="utf-8", capture_output=True)
    all_resistances = ast.literal_eval('[\n'+p1.stdout+p2.stdout+p3.stdout+'\n]') # similar to JSON.load, but handles trailing commas without crashing
    return all_resistances
