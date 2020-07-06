# coding: UTF-8
import os
import subprocess
import shutil
import re
def fozu():
    print("                            _ooOoo_                     ")
    print("                           o8888888o                    ")
    print("                           88  .  88                    ")
    print("                           (| -_- |)                    ")
    print("                            O\\ = /O                    ")
    print("                        ____/`---'\\____                ")
    print("                      .   ' \\| |// `.                  ")
    print("                       / \\||| : |||// \\               ")
    print("                     / _||||| -:- |||||- \\             ")
    print("                       | | \\\\\\ - /// | |             ")
    print("                     | \\_| ''\\---/'' | |              ")
    print("                      \\ .-\\__ `-` ___/-. /            ")
    print("                   ___`. .' /--.--\\ `. . __            ")
    print("                ."" '< `.___\\_<|>_/___.' >'"".         ")
    print("               | | : `- \\`.;`\\ _ /`;.`/ - ` : | |     ")
    print("                 \\ \\ `-. \\_ __\\ /__ _/ .-` / /      ")
    print("         ======`-.____`-.___\\_____/___.-`____.-'====== ")
    print("                            `=---='  ")
    print("                                                        ")
    print("         .............................................  ")
    print("                  Prey for no bug                      ")
    print("                  Zen of python:                       ")
    print("                  Beautiful is better than ugly.；      ")
    print("                  Explicit is better than implicit.     ")
    print("                  Simple is better than complex.        ")
    print("                  Complex is better than complicated.   ")
    print("                  Flat is better than nested.           ")
    print("                  Sparse is better than dense.          ")
    print("                  Readability counts.                   ")
    print("                  Now is better than never.             ")


fozu()
# input the dir containing requested files or put this program in the same directory where you store fastq files
input_dir = os.getcwd()
# input the path of the ref
genome_path = '/home/han/v4/v4.fa'




if os.path.exists(genome_path):

    print('The genome file has been found.')

    all_files = os.listdir(input_dir)
    list_sra_files_1 = list()
    list_sra_files_2 = list()
    list_sra_files_single = list()

    for file in all_files:

        file_path = os.path.join(input_dir, file)

        if file_path.endswith('_1.fastq') or file_path.endswith('_1.fq') or file_path.endswith('_R1.fastq') or \
                file_path.endswith('R1.fq'):
            list_sra_files_1.append(file_path)

        elif file_path.endswith('_1.fastq.gz') or file_path.endswith('_1.fq.gz') or file_path.endswith('_R1.fastq.gz') or \
                file_path.endswith('R1.fq.gz'):
            list_sra_files_1.append(file_path)

        elif file_path.endswith('_2.fastq') or file_path.endswith('_2.fq') or file_path.endswith('_R2.fastq') or \
                file_path.endswith('R2.fq'):
            list_sra_files_2.append(file_path)

        elif file_path.endswith('_2.fastq.gz') or file_path.endswith('_2.fq.gz') or file_path.endswith('_R2.fastq.gz') or \
                file_path.endswith('R2.fq.gz'):
            list_sra_files_2.append(file_path)

        if (file_path.endswith('fastq.gz') or file_path.endswith('fq.gz')) and ((('_1.fastq' not in file_path) and ('_2.fastq' not in file_path)) and (('_1.fq' not in file_path) and ('_2.fq' not in file_path))):
            list_sra_files_single.append(file_path)

    print('list1 ====' + ', '.join(list_sra_files_1))
    print('list2 ====' + ', '.join(list_sra_files_2))
    print('list_single ====' + ', '.join(list_sra_files_single))

    for file in list_sra_files_1:

        file_dir = os.path.dirname(file)
        file_sra_name = os.path.basename(file)
        pre_file_name = file_sra_name.split('_')[0]

        for file_2 in list_sra_files_2:

            file_2_name = os.path.basename(file_2)
            pre_file_2_name = file_2_name.split('_')[0]

            if pre_file_name == pre_file_2_name:

                print('Processing...{}'.format(file_sra_name) + "====={}".format(file_2_name))

                cmd_bwa = "bwa mem -M -R '@RG\\tID:{}".format(pre_file_name) + "\\tSM:{}".format(pre_file_name) + "\\tPL:illumina' -t 30 {}".format(genome_path) + \
                             " {}".format(file) + " {}".format(file_2) + " | sentieon util sort -o {}_sort.bam --sam2bam -".format(pre_file_name)

                if subprocess.check_call(cmd_bwa, shell=True) != 0:
                    raise SystemCommandError

    for file in list_sra_files_single:

        pre_file_name = file.split('.')[0]
        cmd_bwa = "bwa mem -M -R '@RG\\tID:{}".format(pre_file_name) + "\\tSM:{}".format(
            pre_file_name) + "\\tPL:illumina' -t 30 {}".format(genome_path) + \
                  " {}".format(file) + " | sentieon util sort -o {}_sort.bam --sam2bam -".format(
            pre_file_name)

        if subprocess.check_call(cmd_bwa, shell=True) != 0:
            raise SystemCommandError

else:
    print('The path of genome file is not exist, please change the path where you store the genome files related')


