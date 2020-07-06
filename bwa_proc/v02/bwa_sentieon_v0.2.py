# coding: UTF-8
import os
import subprocess
import shutil
from file_processor import FilePorcessor
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

file_proc = FilePorcessor()
file_proc = file_proc.fit(input_dir)
paired_fpaths = file_proc.get_paired_seq_fpaths()

for paired_fpath_dic in paired_fpaths:

    file_1 = paired_fpath_dic['fpath_r1']
    file_2 = paired_fpath_dic['fpath_r2']

    file_dir = os.path.dirname(file_1)
    file_sra_name = os.path.basename(file_1)
    pre_file_name = file_sra_name.split('_')[0]
    if re.findall(r'\.f(ast)?q\.*(\.gz)?', file_sra_name):

        print('Processing...{}'.format(os.path.basename(file_1)) + "====={}".format(os.path.basename(file_2)))

        cmd_bwa = "bwa mem -M -R '@RG\\tID:{}".format(pre_file_name) + "\\tSM:{}".format(
            pre_file_name) + "\\tPL:illumina' -t 30 {}".format(genome_path) + \
                  " {}".format(file_1) + " {}".format(file_2) + " | sentieon util sort -o {}_sort.bam --sam2bam -".format(
            pre_file_name)

        if subprocess.check_call(cmd_bwa, shell=True) != 0:
            raise SystemCommandError

    # for file in list_sra_files_single:
    #
    #     pre_file_name = file.split('.')[0]
    #     cmd_bwa = "bwa mem -M -R '@RG\\tID:{}".format(pre_file_name) + "\\tSM:{}".format(
    #         pre_file_name) + "\\tPL:illumina' -t 60 {}".format(genome_path) + \
    #               " {}".format(file) + " | sentieon util sort -o {}_sort.bam --sam2bam -".format(
    #         pre_file_name)
    #
    #     if subprocess.check_call(cmd_bwa, shell=True) != 0:
    #         raise SystemCommandError



