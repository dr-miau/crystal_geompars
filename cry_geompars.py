#!/usr/bin/python3
#Parser for CRYSTAL output last cell parameters
#Author: Marcos Rivera
#Some details:  -The pattern must be typed between double quotes 
#                if using wildcards: "pattern*"

import sys,glob

if len(sys.argv) < 2:
    print("Specify a filename or filenames pattern to parse.")
    sys.exit()

filenames = sorted(glob.glob(sys.argv[1]))
outfile = open("geom_params.dat","w+")
outfile.write("A\tB\tC\talpha\tbeta\tgamma\tvol\tdens\n")
truefiles = []

for rfile in filenames:
    final_lines = False
    with open(rfile,'r') as readfile:
        for line in readfile:
            if line.startswith(" FINAL OPT"):
                final_lines = True
                truefiles.append(rfile)
            if final_lines and line.startswith(" PRIMITIVE"):
                temp_line = line.split()
                volume = temp_line[temp_line.index("VOLUME=")+1]
                density = temp_line[temp_line.index("DENSITY")+1]
            if final_lines and line.startswith("         A"):
                cell_params = next(readfile).split()
        if final_lines:
            outfile.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n"\
                    .format(cell_params[0],cell_params[1],cell_params[2],
                    cell_params[3],cell_params[4],cell_params[5],
                    volume,density))
    
for tfile in truefiles:
    outfile.write("#{}\n".format(tfile))
