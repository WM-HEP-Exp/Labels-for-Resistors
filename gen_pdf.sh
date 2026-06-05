#!/bin/zsh

cd "$(dirname "$0")"
echo -n >Labels1.py
cat Labels-header.txt >>Labels1.py
python3 comp_analysis_modified.py "$1/M1" 1 $2 >>Labels1.py
python3 comp_analysis_modified.py "$1/M2" 2 $2 >>Labels1.py
python3 comp_analysis_modified.py "$1/M3" 3 $2 >>Labels1.py
cat Labels-footer.txt >>Labels1.py
python3 Labels1.py