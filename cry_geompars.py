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
efrac = open("geom_errors.dat","w+")
outfile.write("A\tB\tC\talpha\tbeta\tgamma\tvol\tdens\n")
efrac.write("A\tB\tC\talpha\tbeta\tgamma\tvol\tdens\n")
truefiles = []

for rfile in filenames:
    final_lines = False
    final_param = False
    points = 0
    nextline = "null"
    unext = False
#    filezero = True
#    temp_line = []
    with open(rfile,'r') as readfile:
        for line in readfile:
#            nextline = next(readfile,"nolines")
            if line.startswith(" PRIMITIVE CELL") and points == 0:
                temp_line = line.split()
                volume0 = float(temp_line[temp_line.index("VOLUME=")+1])
                density0 = float(temp_line[temp_line.index("DENSITY")+1])
            if unext and points == 0:
                ori_params = list(map(float,line.split()))
                points += 1
                unext = False
            if points == 0 and line.startswith("         A"):
                unext = True
            if line.startswith(" FINAL OPT"):
                final_lines = True
                truefiles.append(rfile)
            if final_lines and line.startswith(" PRIMITIVE"):
                temp_line = line.split()
                volume = float(temp_line[temp_line.index("VOLUME=")+1])
                density = float(temp_line[temp_line.index("DENSITY")+1])
            if final_lines and unext:
                unext = False
                cell_params=list(map(float,line.split()))
            if final_lines and line.startswith("         A"):
                unext = True
        if final_lines:
            outfile.write("{:.8f}\t{:.8f}\t{:.8f}\t{:.2f}\t{:.2f}\t{:.2f}\t{:.6f}\t{:.3f}\n"
                    .format(cell_params[0],cell_params[1],
                    cell_params[2],cell_params[3],cell_params[4],
                    cell_params[5],volume,density))
            err_array = []
            for i in range(6):
                err_array.append(abs(cell_params[0]-ori_params[0])
                        /ori_params[0])
            err_vol = abs(volume-volume0)/volume0
            err_dens = abs(density-density0)/density0
            efrac.write("{:.8f}\t{:.8f}\t{:.8f}\t{:.2f}\t{:.2f}\t{:.2f}\t{:.6f}\t{:.3f}\n"
                    .format(err_array[0],err_array[1],
                    err_array[2],err_array[3],err_array[4],
                    err_array[5],err_vol,err_dens))
    
for tfile in truefiles:
    outfile.write("#{}\n".format(tfile))
    efrac.write("#{}\n".format(tfile))
