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
    p1 = subprocess.run([sys.executable, os.path.dirname(__file__) + os.sep + "comp_analysis_modified.py", data_folder+"/M1", "1", "XX-XX-XXXX", os.path.dirname(__file__) + os.sep + "CalFilesCB1"], encoding="utf-8", capture_output=True)
    sys.stderr.write(p1.stderr)
    sys.stderr.flush()
    p2 = subprocess.run([sys.executable, os.path.dirname(__file__) + os.sep + "comp_analysis_modified.py", data_folder+"/M2", "2", "XX-XX-XXXX", os.path.dirname(__file__) + os.sep + "CalFilesCB2"], encoding="utf-8", capture_output=True)
    sys.stderr.write(p2.stderr)
    sys.stderr.flush()
    p3 = subprocess.run([sys.executable, os.path.dirname(__file__) + os.sep + "comp_analysis_modified.py", data_folder+"/M3", "3", "XX-XX-XXXX", os.path.dirname(__file__) + os.sep + "CalFilesCB3"], encoding="utf-8", capture_output=True)
    sys.stderr.write(p3.stderr)
    sys.stderr.flush()
    all_resistances = ast.literal_eval('[\n'+p1.stdout+p2.stdout+p3.stdout+'\n]') # similar to JSON.load, but handles trailing commas without crashing
    return all_resistances

def map_resistances(resistances):
    resistance_map = {}
    for i in resistances:
        #print(type(i['resistance']).__name__)
        if type(i['resistance']).__name__ == 'bytes':
            resistance_map[str(i['module']) + '_' + str(i['board']) + '_' + str(i['channel'])] = i['resistance'].decode('utf-8')
        else:
            resistance_map[str(i['module']) + '_' + str(i['board']) + '_' + str(i['channel'])] = i['resistance']
    return resistance_map

def filter_resistances(resistance_map):
    key1 = '1_A_8'
    key2 = '2_A_1'
    key3 = '3_A_1'
    res1 = resistance_map[key1] if key1 in resistance_map else 'nan'
    res1 = resistance_map[key2] if key2 in resistance_map else 'nan'
    res1 = resistance_map[key3] if key3 in resistance_map else 'nan'
    return [res1, res2, res3]

if __name__ == '__main__':
    #folder_map = {}
    folders = enumerate_folders(sys.argv[1])
    for f in folders:
        print(f, file=sys.stderr)
        key = os.path.split(f.rstrip('/'))[1] # returns date, such as "6-22-26_run2"
        try:
            value = filter_resistances(map_resistances(get_resistances(f)))
            print(key + ": " + str(value))
        except SyntaxError:
            continue
        #folder_map[key] = value
    #print(folder_map)
