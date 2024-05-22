# Takes as input the "sequence_report" file from NCBI for reference genome assemblies and fixes chromosome names from the GenBank/RefSeq names to simple number format (e.g. 1, 2... X, Y)
# The sequence_report file must have simple number format chr. names on column 4 and GenBank format chr. names on column 7 / RefSeq format chr. names on column 10
import re

file_name = input("Enter name of file to fix chromosome names for (incl. extension): ")
sequence_report_name = input("Enter sequence report file name (incl. extension): ")
current_format = input("Current chromosome name format in input file (choices: 1. GenBank (CM), 2. RefSeq (NC)): ")

if current_format == "1":
    magic_no = 6
elif current_format == "2":
    magic_no = 9
else:
    print("Not a proper choice. Enter 1 or 2.")
    exit()

file = open(file_name, "r")
sequence_report = open(sequence_report_name, "r")
fixed_file = open(".".join(re.split("\.", file_name)[:-1]) + "_chrNameFixed." + re.split("\.", file_name)[-1], "w")

for file_line in file:
    fixed_line = file_line
    for sequence_report_line in sequence_report:
        if len(re.findall(re.split("\t", sequence_report_line)[magic_no], fixed_line))>0: # Change the magic number 6 to 9 if converting from RefSeq accession instead of GenBank
            fixed_line = re.sub(re.split("\t", sequence_report_line)[magic_no], re.split("\t", sequence_report_line)[3], fixed_line) # Do likewise as above line
    fixed_file.write(fixed_line)
    sequence_report.seek(0)
