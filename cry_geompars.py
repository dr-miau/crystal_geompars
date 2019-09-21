#!/usr/bin/python3
#Parser for CRYSTAL output last cell parameters
#Author: Marcos Rivera
#Some details:  -The pattern must be typed between double quotes 
#                if using wildcards: "pattern*"

import sys,glob,re
#import glob

#final_geom = re.compile(r"FINAL GEOM*")

if len(sys.argv) < 2:
    print("Specify a pattern for files to parse.")
    sys.exit()

filenames = sorted(glob.glob(sys.argv[1]))
#final_lines=False

for rfile in filenames:
    print(rfile)
    final_lines = False
    with open(rfile,'r') as readfile:
        for line in readfile:
            if line.startswith(" FINAL OPT"):
                final_lines = True
            if final_lines and line.startswith(" PRIMITIVE"):
                temp_line = line.split()
                volume = temp_line[temp_line.index("VOLUME=")+1]
                density = temp_line[temp_line.index("DENSITY")+1]
            if final_lines and line.startswith("         A"):
                cell_params = next(readfile).split()
        if final_lines:
            print("VOL =",volume)
            print("DENS =",density)
            print("A =",cell_params[0])
            print("B =",cell_params[1])
            print("C =",cell_params[2])
            print("alpha =",cell_params[3])
            print("beta =",cell_params[4])
            print("gamma =",cell_params[5])
                


