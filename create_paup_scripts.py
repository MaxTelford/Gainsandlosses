from Bio import SeqIO
import sys

g = SeqIO.parse(sys.argv[1], "fasta")

sequences = {}

for record in g:
    current_header = record.id
    current_seq = record.seq
    sequences[current_header] = current_seq
    
    
output = open("ancestral." + sys.argv[1] + ".paup", "w")

output.write("#NEXUS\n")
output.write("\tBegin Data;\n")
output.write("\t\tDIMENSIONS  NTAX=57 NCHAR=" + str(len(current_seq)) + ";\n")
output.write("\t\tFORMAT DATATYPE = Standard MISSING=? GAP=- ;\n")
output.write("\tMATRIX\n")

for k,v in sequences.items():
    output.write(k + "	" + str(v) + "\n")
    
end_string = """
;
 end;

begin trees;
    tree tree_1 = [&R] ((((((((((((Limulus_polyphemus:0.321519,Stegodyphus_mimosarum:0.492405):0.030186,Ixodes_scapularis:0.564533):0.133,(((Apis_mellifera:0.516731,Drosophila_melanogaster:0.720626):0.160432,Daphnia_pulex:0.64308):0.132382,Strigamia_maritima:0.539577):0.1324):0.08062,(Hypsibius_dujardini:0.332916,Ramazzottius_varieornatus:0.608903):0.824688):0.086679,(((Caenorhabditis_elegans:0.661312,Pristionchus_pacificus:0.642997):0.223644,Loa_loa:0.641527):0.459969,((Trichuris_muris:0.806301,Trichinella_spiralis:0.72056):0.361121,Romanomermis_culicivorax:0.778886):0.101942):0.265069):0.041662,Priapulus_caudatus:0.579895):0.03616,((((((((Biomphalaria_glabrata:0.47174,Lottia_gigantea:0.35248):0.053349,Crassostrea_gigas:0.406188):0.037952,Octopus_bimaculata:0.498833):0.080916,(Notospermus_geniculatus:0.410871,Phoronis_australis:0.43034):0.048585):0.024157,(Capitella_teleta:0.42549,Helobdella_robusta:0.796566):0.10225):0.0265,((((Echinococcus_multilocularis:0.701801,Schistosoma_mansoni:0.634459):0.347287,Schmidtea_mediterranea:1.069956):0.199591,Macrostomum_lignano:0.985824):0.222279):1.0E-4):0.0265,Adineta_vaga:1.100723):0.0712):1.0E-5):0.066917,(((((((((Homo_sapiens:0.041599,Mus_musculus:0.056006):0.115891,Gallus_gallus:0.138351):0.073395,Latimeria_chalumnae:0.16515):0.020379,Callorhinchus_milii:0.215089):0.030205,Danio_rerio:0.236377):0.094097,Petromyzon_marinus:0.393949):0.173827,Ciona_intestinalis:0.860678):0.058921,Branchiostoma_floridae:0.440855):0.046866,(((((Lytechinus_variegatus:0.112087,Strongylocentrotus_purpuratus:0.05702):0.286268,Apostichopus_japonicus:0.461):0.048592,(Acanthaster_planci:0.070146,Patiria_miniata:0.096153):0.256138):0.131735,((Ptychodera_flava:0.278285,Saccoglossus_kowalevskii:0.216578):0.132171,Rhabdopleura_recondita:0.523756):0.050138):0.0657,Xenoturbella_bocki:0.69):0.0176):0.0343):0.145326,(((Orbicella_faveolata:0.104757,Stylophora_pistillata:0.111691):0.2036,Nematostella_vectensis:0.322292):0.165343,Hydra_vulgaris:0.841792):0.09449):0.064391,(Hoilungia_hongkongensis:0.116016,Trichoplax_adhaerens:0.126264):0.692142):0.123474,(Mnemiopsis_leidyi:0.264632,Pleurobrachia_bachei:0.409822):0.964958):0.08,(Amphimedon_queenslandica:0.737847,Oscarella_carmela:0.68341):0.08);
end;

begin paup;
describetrees 1 /apolist=yes chglist=no;
[describetrees 1 /chglist=yes apolist=no;]
end;
quit;
"""

output.write(end_string)
    