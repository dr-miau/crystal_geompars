# Parser for CRYSTAL output last cell parameters

In my common workflow with CRYSTAL (an ab-initio program - that uses localized gaussian basis functions - for electronic structure of periodic systems), I need to read multiple files to extract the cell parameters obtained from geometry optimizations. I build this small script for helping in this task, and to start to refresh my programming habilities.

This script need as argument the filename or a pattern for multiple filenames (between quotation marks) where it will search for final optimized cell parameters. Here is an example using a pattern; it could also need wildcards as used in bash:

>./cry_geompars.py "pattern*"

The result is a file named "geom_params.dat", with the parameters tabulated in order. The last lines show the filenames in order, so you can retrive to which file each row of parameters belong. It only writes parameters if there is a final optimized geometry in the file, and only writes the names of such files. Hopefully, the format of the output file could be readed by many programs (i.e. gnuplot, grace, any spreadsheet).

For now, it reads files only in the folder of excecution. If want to test it, in the CRYSTAL web tutorials you can find this i/o files list: http://tutorials.crystalsolutions.eu/tutorial.html?td=optgeom&tf=opt_tut#inplist . It's design for reading CRYSTAL14 output, so it might not work with newer or older versions.

I hope this can be useful for any other. If you have any comment, I'm very glad to hear it.
