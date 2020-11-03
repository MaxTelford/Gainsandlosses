import numpy as np
import argparse
import os

usage = "A script to produce model matrices that will be used in ALF simulations"
toolname = "ModelFileMaker"
footer = "Who \n Paschalis Natsidis (p.natsidis@ucl.ac.uk); \n \nWhere \n Telford Lab, UCL;\n\
 ITN IGNITE; \n  \nWhen\n December 2019; \n\n"

parser = argparse.ArgumentParser(description = usage, prog = toolname, epilog = footer, formatter_class=argparse.RawDescriptionHelpFormatter,)
parser.add_argument('-n', metavar = 'integer', dest = 'replicates', required = True,
                    help = 'number of matrices to produce')
parser.add_argument('-lg', metavar = 'filename', dest = 'lgmatrix', required = True,
                    help = 'path to LGmatrix file that will be used as template')
parser.add_argument('-o', metavar = 'directory', dest = 'output_dir', required = True,
                    help = 'directory where the output will be written')

args = parser.parse_args()

input_replicates = args.replicates
input_lg = args.lgmatrix
output_directory = args.output_dir

os.system("mkdir " + output_directory)

dirichlet_params = [15.587174,   
13.385089   ,
10.191291   ,
13.680386   ,
 4.375704   ,
 10.292063  ,
 16.638240   ,
 12.907106   ,
 6.003040   ,
 13.726724   ,
 23.631826   ,
 15.755237    ,
 5.993808    ,
 9.848469   ,
 10.164202  ,
 17.251680  ,
 12.636493  ,
  2.543981  ,
  7.706336  ,
  15.855581]

sample = np.random.dirichlet(dirichlet_params, int(input_replicates))

for i in range(np.shape(sample)[0]):
    entry = sample[i]
    entry.tolist()
    entry[-1] = 1 - sum(entry[:-1])
    string_to_append = ""
    for j in entry:
        string_to_append += str(round(j, 6)) + " "
    
    input_matrix = open(input_lg, "r")
    output_matrix = open(output_directory + "/matrix" + str(i) + ".txt", "w")
    
    for line in input_matrix.readlines():
        output_matrix.write(line)
    output_matrix.write(string_to_append)
    output_matrix.close()