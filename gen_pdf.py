import os
import subprocess
import sys

DATA_FILES = "/Users/celebrimbor/Documents/6-13-26"
DATE = "6-13-26"

if len(sys.argv) < 2:
	filepath = DATA_FILES
	filedate = DATE
path = os.path.dirname(os.path.abspath(__file__))
os.chdir(path)
f = open("Labels1.py", "w")
f.close()
f = open("Labels1.py", "a", encoding="utf-8")
header = open("Labels-header.txt", "r")
headertext = header.read()
header.close()
f.write(headertext)
print("running modules...")
p1 = subprocess.run(["python3", "comp_analysis_modified.py", filepath+"/M1", "1", filedate], encoding="utf-8", capture_output=True)
f.write(p1.stdout)
sys.stderr.write(p1.stderr) # debugging
#sys.stderr.write(os.linesep)
sys.stderr.flush()
print("mod 1 done")
p2 = subprocess.run(["python3", "comp_analysis_modified.py", filepath+"/M2", "2", filedate], encoding="utf-8", capture_output=True)
f.write(p2.stdout)
sys.stderr.write(p2.stderr) # debugging
#sys.stderr.write(os.linesep)
sys.stderr.flush()
print("mod 2 done")
p3 = subprocess.run(["python3", "comp_analysis_modified.py", filepath+"/M3", "3", filedate], encoding="utf-8", capture_output=True)
f.write(p3.stdout)
sys.stderr.write(p3.stderr) # debugging
#sys.stderr.write(os.linesep)
sys.stderr.flush()
print("mod 3 done")
footer = open("Labels-footer.txt", "r")
footertext = footer.read()
footer.close()
f.write(footertext)
f.close()
subprocess.run(["python3", "Labels1.py", filedate])