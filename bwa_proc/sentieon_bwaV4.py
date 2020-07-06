# coding: UTF-8
import os
import subprocess
import shutil

# input the dir containing requested files or put this program in the same directory where you store fastq files
input_dir = os.getcwd()
# input the path of the ref
genome_path = '/home/han/v4/v4.fa'

all_files = os.listdir(input_dir)
list_sra_files_1 = list()
list_sra_files_2 = list()

for file in all_files:

    file_path = os.path.join(input_dir, file)

    if file_path.endswith('_1.fastq') or file_path.endswith('_1.fq') or file_path.endswith('R1.fastq') or file_path.endswith('R1.fq'):

        list_sra_files_1.append(file_path)

    if file_path.endswith('_2.fastq') or file_path.endswith('_2.fq') or file_path.endswith('R2.fastq') or file_path.endswith('R2.fq'):

        list_sra_files_2.append(file_path)


for file in list_sra_files_1:

    file_dir = os.path.dirname(file)
    file_sra_name = os.path.basename(file)
    pre_file_name = file_sra_name.split('_')[0]

    for file_2 in list_sra_files_2:

        file_2_name = os.path.basename(file_2)
        pre_file_2_name = file_2_name.split('_')[0]

        if pre_file_name == pre_file_2_name:
            print('Processing...{}'.format(file_sra_name) + "====={}".format(file_2_name))



            cmd_bwa = "bwa mem -M -R '@RG\tID:{}".format(pre_file_name) + "\tSM:{}".format(pre_file_name) + "\tPL:illumina' -t 30 {}".format(genome_path) + \
                         " {}".format(file) + " {}".format(file_2) + " | sentieon util sort -o {}_sort.bam --sam2bam -".format(pre_file_name)

            if subprocess.check_call(cmd_bwa, shell=True) != 0:
                raise SystemCommandError


