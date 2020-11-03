# Gainsandlosses
This repository contains code and results produced in the framework of the study "Systematic errors in orthology inference: a bug or a feature for evolutionary analyses?"

## Contents
`create_LG_matrices.py` template to create LG matrices with fixed amino-acid exchangeabilities and random amino-acid frequencies based on frequencies from real data.
`create_ALF_config_files.py` template to create configuration files for ALF simulation software.
`integrate_singletons.py` used to incorporate species-specific genes (singletons) in ortholog presence/absence matrices.
`pairwise_distances.py` used to calculate pairwise patristic distances among all species in a phylogenetic tree.
`create_PAUP_scripts.py` template to create PAUP scripts for gene gain/loss analysis.
`574_orthogroups.zip` contains the 574 orthogroups used to estimate parameters for informing the simulations
`guide_tree.nwk` the tree that was used in ALF to simulate the evolution of orthologs. In each simulation all branch lengths were multiplied with a multiplier to account for different evolutionary rates.
`orthology_and_rf_scores.csv` results of orthology inference and RF scores for the 200 simulations.
`phylostratigraphy_results.csv` results of phylostratigraphy analysis for the 200 simulations.

## Other scripts used in this paper
- https://github.com/pnatsi/OGFilter to select orthogroups with min 80% of species present and max. 4 gene copies per species
- https://github.com/pnatsi/ParaFilter to filter out paralogs and create 574 single-copy orthologs
- https://github.com/pnatsi/Al2PrunedTree to prune the guide tree to keep only species present in each of the 574 alignments
- https://github.com/pnatsi/orthocounts2bin to create gene presence/absence alignment from OrthoFinder gene counts file.










