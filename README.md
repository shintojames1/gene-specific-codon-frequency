# gene-specific-codon-frequency

## Steps to use
1. For the required organism, use the following settings to download .fna file from NCBI assembly:
    * Souce database : RefSeq
    * File type : CDS from genomic Fasta (.fna)

2. Change file_path variable in the code to the path of the .fna file 


## Description

This code uses the .fna file for a given organism and prints :
1. Total number of genes containing atleast one of the target codons and the total number of genes in .fna file
2. Frequency of genes containing atleast one of the target codons


Target codons : ['TCA', 'TTA', 'CTA']
