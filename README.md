# pipelines
Pipelines for processing a batch of files automatically. All the scripts were required Python 3.x.
### main_salmon
Using salmon to process the RNA-seq data, obtaining TPM value of each gene.
* single_ended.py: This program is used for processing the single ended sequencing data
* for the paired-ended sequencing data, use main_salmon.py
* for merging the results of salmon, using main_merge_data.py
* The detailed infomation of how to use the programs, just type the conrespondance names of scripts plus "--help".


# bwa_proc
In the bwa_proc dictionary, it contains all the bwa_sention process.
For how to use the program, just copy correspondance file to the dictionary that contains the files you want to process. And type python $your_program.
