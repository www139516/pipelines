# coding: UTF-8
import os
import subprocess
import shutil

# input the dir containing requested files or put this program in the same directory where you store fastq files
input_dir = os.getcwd()
# input the path of the ref
# genome_path = '/home/han/v4/v4.fa'


all_files = os.listdir(input_dir)
list_sra_files_1 = list()
list_sra_files_2 = list()

for file in all_files:

    file_path = os.path.join(input_dir, file)

    if file_path.endswith('_sort.bam'):

        list_sra_files_1.append(file_path)

    # if file_path.endswith('_2.fastq') or file_path.endswith('_2.fq') or file_path.endswith('_R2.fastq') or file_path.endswith('R2.fq'):
    #
    #     list_sra_files_2.append(file_path)


for file in list_sra_files_1:

    file_dir = os.path.dirname(file)
    file_sra_name = os.path.basename(file)
    pre_file_name = file_sra_name.split('_')[0]

    print('Processing...{}'.format(file_sra_name))

    cmd_1 = 'sentieon driver -t 30 -i {}_sort.bam'.format(pre_file_name) + ' --algo LocusCollector --fun score_info {}.score'.format(pre_file_name)
    cmd_2 = 'sentieon driver -t 30 -i {}_sort.bam'.format(pre_file_name) + ' --algo Dedup --rmdup --score_info {}.score'.format(pre_file_name) + ' --metrics {}.dedup.metrics'.format(pre_file_name) + ' {}.deduped.bam'.format(pre_file_name)

    if subprocess.check_call(cmd_1, shell=True) != 0:
        raise SystemCommandError

    if subprocess.check_call(cmd_2, shell=True) != 0:
        raise SystemCommandError

