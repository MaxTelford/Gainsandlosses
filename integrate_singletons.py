import argparse
from Bio import SeqIO

#HERE BEGINS THE INPUT ARGUMENTS DEFINITION
usage = "A script extend a gene presence/absence alignment to include singleton information"
toolname = "F2PA"
footer = "Who \n Paschalis Natsidis (p.natsidis@ucl.ac.uk); \n \nWhere \n Telford Lab, UCL;\n\
 ITN IGNITE; \n  \nWhen\n January 2020; \n\n"

parser = argparse.ArgumentParser(description = usage, prog = toolname, epilog = footer, formatter_class=argparse.RawDescriptionHelpFormatter,)
parser.add_argument('-a', metavar = 'filename', dest = 'alignment', required = True,
                    help = 'full path to initial alignment file')
parser.add_argument('-u', metavar = 'filename', dest = 'unassigned', required = True,
                    help = 'full path to the file with unassigned genes per species information')

#parser.print_help()

args = parser.parse_args()

#READ USER INPUT
alignment_file = args.alignment
unassigned_file = args.unassigned

g = SeqIO.parse(alignment_file, "fasta")

f = open(unassigned_file, "r")
lines = f.readlines()
splitted = [x.strip().split("\t") for x in lines]

species = splitted[0]
numbers = splitted[1][1:]

unassigned_per_species = {}

for i in range(len(species)):
    unassigned_per_species[species[i]] = int(numbers[i])

sequences_to_write = {}

for record in g:
    current_species = record.id
    current_sequence = record.seq
    sequences_to_write[current_species] = current_sequence

g = SeqIO.parse(alignment_file, "fasta")

for record in g:
    current_species = record.id
    current_to_add = unassigned_per_species[current_species]
    for k, v in sequences_to_write.items():
        if k == current_species:
            string_to_add = current_to_add * "1"
            sequences_to_write[k] += string_to_add
        else:
            string_to_add = current_to_add * "0"
            sequences_to_write[k] += string_to_add
    print(len(sequences_to_write[current_species]))


output = open("with_singletons.fasta", "w")

for k, v in sequences_to_write.items():
    output.write(">" + k + "\n" + str(v) + "\n")