import os
import subprocess
import sys

path = os.path.dirname(os.path.abspath(__file__))
os.chdir(path)
f = open("Labels1.py", "w")
f.close()
f = open("Labels1.py", "a")
header = open("Labels-header.txt", "r")
headertext = header.read()
header.close()
f.write(headertext)
p1 = subprocess.run(["python3", "comp_analysis_modified.py", sys.argv[1]+"/M1", "1", sys.argv[2], "False"], encoding="utf-8", capture_output=True)
f.write(p1.stdout)
p2 = subprocess.run(["python3", "comp_analysis_modified.py", sys.argv[1]+"/M2", "2", sys.argv[2], "False"], encoding="utf-8", capture_output=True)
f.write(p2.stdout)
p3 = subprocess.run(["python3", "comp_analysis_modified.py", sys.argv[1]+"/M3", "3", sys.argv[2], "False"], encoding="utf-8", capture_output=True)
f.write(p3.stdout)
footer = open("Labels-footer.txt", "r")
footertext = footer.read()
footer.close()
f.write(footertext)
f.close()