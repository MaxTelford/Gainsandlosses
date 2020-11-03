import os
from ete3 import Tree
import sys

mytree = Tree(sys.argv[1])

if sys.argv[2] == "sims":
    list1 = ['Limulus_polyphemus','Stegodyphus_mimosarum','Ixodes_scapularis','Apis_mellifera','Drosophila_melanogaster','Daphnia_pulex','Strigamia_maritima','Hypsibius_dujardini','Ramazzottius_varieornatus','Caenorhabditis_elegans','Pristionchus_pacificus','Loa_loa','Trichuris_muris','Trichinella_spiralis','Romanomermis_culicivorax','Priapulus_caudatus','Biomphalaria_glabrata','Lottia_gigantea','Crassostrea_gigas','Octopus_bimaculata','Notospermus_geniculatus','Phoronis_australis','Capitella_teleta','Helobdella_robusta','Echinococcus_multilocularis','Schistosoma_mansoni','Schmidtea_mediterranea','Macrostomum_lignano','Adineta_vaga','Homo_sapiens','Mus_musculus','Gallus_gallus','Latimeria_chalumnae','Callorhinchus_milii','Danio_rerio','Petromyzon_marinus','Ciona_intestinalis','Branchiostoma_floridae','Lytechinus_variegatus','Strongylocentrotus_purpuratus','Apostichopus_japonicus','Acanthaster_planci','Patiria_miniata','Ptychodera_flava','Saccoglossus_kowalevskii','Rhabdopleura_recondita','Xenoturbella_bocki','Orbicella_faveolata','Stylophora_pistillata','Nematostella_vectensis','Hydra_vulgaris','Hoilungia_hongkongensis','Trichoplax_adhaerens','Mnemiopsis_leidyi','Pleurobrachia_bachei','Amphimedon_queenslandica','Oscarella_carmela']

    list2 = ['Limulus_polyphemus','Stegodyphus_mimosarum','Ixodes_scapularis','Apis_mellifera','Drosophila_melanogaster','Daphnia_pulex','Strigamia_maritima','Hypsibius_dujardini','Ramazzottius_varieornatus','Caenorhabditis_elegans','Pristionchus_pacificus','Loa_loa','Trichuris_muris','Trichinella_spiralis','Romanomermis_culicivorax','Priapulus_caudatus','Biomphalaria_glabrata','Lottia_gigantea','Crassostrea_gigas','Octopus_bimaculata','Notospermus_geniculatus','Phoronis_australis','Capitella_teleta','Helobdella_robusta','Echinococcus_multilocularis','Schistosoma_mansoni','Schmidtea_mediterranea','Macrostomum_lignano','Adineta_vaga','Homo_sapiens','Mus_musculus','Gallus_gallus','Latimeria_chalumnae','Callorhinchus_milii','Danio_rerio','Petromyzon_marinus','Ciona_intestinalis','Branchiostoma_floridae','Lytechinus_variegatus','Strongylocentrotus_purpuratus','Apostichopus_japonicus','Acanthaster_planci','Patiria_miniata','Ptychodera_flava','Saccoglossus_kowalevskii','Rhabdopleura_recondita','Xenoturbella_bocki','Orbicella_faveolata','Stylophora_pistillata','Nematostella_vectensis','Hydra_vulgaris','Hoilungia_hongkongensis','Trichoplax_adhaerens','Mnemiopsis_leidyi','Pleurobrachia_bachei','Amphimedon_queenslandica','Oscarella_carmela']


if sys.argv[2] == "real":
    list1 = ['ANNE_Ctel', 'ANNE_Hrob', 'ARTH_Amel', 'ARTH_Dmel', 'ARTH_Dpul', 'ARTH_Isca', 'ARTH_Limu', 'ARTH_Smar', 'ARTH_Smim', 'BRAC_Paus', 'CEPH_Bflo', 'CNID_Hvul', 'CNID_Nvec', 'CNID_Ofav', 'CNID_Spis', 'CRAN_Cmil', 'CRAN_Drer', 'CRAN_Ggal', 'CRAN_Hsap', 'CRAN_Lcha', 'CRAN_Mmus', 'CRAN_Pmar', 'CTEN_Mlei', 'CTEN_Pbac', 'ECHI_Ajap', 'ECHI_Apla', 'ECHI_Lvar', 'ECHI_Pmin', 'ECHI_Spur', 'HEMI_Pfla', 'HEMI_Rrec', 'HEMI_Skow', 'MOLL_Bgla', 'MOLL_Cgig', 'MOLL_Lott', 'MOLL_Obim', 'NEMA_Celg', 'NEMA_Lloa', 'NEMA_Ppac', 'NEMA_Rcul', 'NEMA_Tmur', 'NEMA_Tspi', 'NEME_Ngen', 'PLAC_Hhon', 'PLAC_Tadh', 'PLAT_Ecmu', 'PLAT_Mlig', 'PLAT_Sman', 'PLAT_Smed', 'PORI_Aque', 'PORI_Ocar', 'PRIA_Pcau', 'ROTI_Avag', 'TARD_HdEd', 'TARD_Rvar', 'UROC_Cint', 'XENO_Xboc']

    list2 = ['ANNE_Ctel', 'ANNE_Hrob', 'ARTH_Amel', 'ARTH_Dmel', 'ARTH_Dpul', 'ARTH_Isca', 'ARTH_Limu', 'ARTH_Smar', 'ARTH_Smim', 'BRAC_Paus', 'CEPH_Bflo', 'CNID_Hvul', 'CNID_Nvec', 'CNID_Ofav', 'CNID_Spis', 'CRAN_Cmil', 'CRAN_Drer', 'CRAN_Ggal', 'CRAN_Hsap', 'CRAN_Lcha', 'CRAN_Mmus', 'CRAN_Pmar', 'CTEN_Mlei', 'CTEN_Pbac', 'ECHI_Ajap', 'ECHI_Apla', 'ECHI_Lvar', 'ECHI_Pmin', 'ECHI_Spur', 'HEMI_Pfla', 'HEMI_Rrec', 'HEMI_Skow', 'MOLL_Bgla', 'MOLL_Cgig', 'MOLL_Lott', 'MOLL_Obim', 'NEMA_Celg', 'NEMA_Lloa', 'NEMA_Ppac', 'NEMA_Rcul', 'NEMA_Tmur', 'NEMA_Tspi', 'NEME_Ngen', 'PLAC_Hhon', 'PLAC_Tadh', 'PLAT_Ecmu', 'PLAT_Mlig', 'PLAT_Sman', 'PLAT_Smed', 'PORI_Aque', 'PORI_Ocar', 'PRIA_Pcau', 'ROTI_Avag', 'TARD_HdEd', 'TARD_Rvar', 'UROC_Cint', 'XENO_Xboc']

for taxon1 in list1:
    for taxon2 in list2:
        if taxon1 != taxon2:
            mytree = Tree(sys.argv[1])
            common = mytree.get_common_ancestor(taxon1,taxon2)
            distance1 = common.get_distance(taxon1)
            distance2 = common.get_distance(taxon2)
            distance = distance1 + distance2
            #asdf = os.popen("/Users/wigo/Desktop/nt-ng/newick-tools --tip_distance " + taxon1 + "," + taxon2 + " --tree /Users/wigo/Desktop/projects/sims_relaunched/57corrected.nwk").read()
            print(taxon1 + " " + taxon2 + " " + str(distance))
    list2.remove(taxon1)
    
