# coding: UTF-8


import os
import subprocess

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



"""
This class is used for processing files in the designated directory.
Methods:
    get_the_abs_path:
        :return the dir path or file path based on the input path
    get_the_paired_seq_file
        :return the paths of paired input file
"""


class FilePorcessor:

    def __init__(self):
        self._in_path = None
        self._in_dpath = None
        self._in_fpath = None
        self._in_lst_fnames = []
        self._in_lst_fpaths = []
        self._in_lst_paired_fnames = []
        self._in_lst_paired_fpaths = []

    def fit(self, path=None):
        """
        initialize the self variables in the object
        :return: self
        """
        if not path:
            self._in_path = os.getcwd()
        else:
            self._in_path = path
            self._in_path = self._get_the_abs_path()
        if os.path.isdir(self._in_path):
            self._in_dpath = self._in_path
            self._in_lst_fnames = os.listdir(self._in_dpath)
            self._in_lst_fpaths = self.get_the_fpath_lst()
        else:
            self._in_fpath = self._in_fpath
        self._get_the_paired_seq_file_path()
        return self

    def get_the_fpath_lst(self):
        lst_fpaths = []
        for fname in self._in_lst_fnames:
            fpath = os.path.join(self._in_dpath, fname)
            lst_fpaths.append(fpath)
        return lst_fpaths


    def _get_the_abs_path(self):
        return os.path.abspath(self._in_path)

    def _get_the_paired_seq_file_path(self):
        """
        serch the files in the directory, and find the paired seq files, store them to the dic
        :return: the list containing dict with paired seq files
        """
        self._in_lst_fnames.sort()
        print("Find {} files in the directory.".format(len(self._in_lst_fnames)))
        # iterate all the file names in the fname list
        for i in range(0, len(self._in_lst_fnames)-1):
            dic_pair_fname = dict()
            dic_pair_fpath = dict()
            j = i + 1
            lst_fname_i = re.split(r'_[Rr]?[12]', self._in_lst_fnames[i])
            # search the files behind the ith file, find the one match the other file of paired file[i]
            for k in range(j, len(self._in_lst_fnames)):
                lst_fname_k = re.split(r'_[Rr]?[12]', self._in_lst_fnames[k])
                if lst_fname_i == lst_fname_k:
                    dic_pair_fname['fname_r1'] = self._in_lst_fnames[i]
                    dic_pair_fname['fname_r2'] = self._in_lst_fnames[k]
                    self._in_lst_paired_fnames.append(dic_pair_fname)
                    dic_pair_fpath['fpath_r1'] = os.path.join(self._in_dpath, dic_pair_fname['fname_r1'])
                    dic_pair_fpath['fpath_r2'] = os.path.join(self._in_dpath, dic_pair_fname['fname_r2'])
                    self._in_lst_paired_fpaths.append(dic_pair_fpath)
                    break

    def get_paired_seq_fpaths(self):
        print(self._in_lst_paired_fpaths)
        print(self._in_lst_paired_fnames)
        return self._in_lst_paired_fpaths


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



