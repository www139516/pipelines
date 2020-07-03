#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/6/23 9:11
# @Author : Yuancong Wang
# @Site : 
# @File : cmd_proc.py
# @Software: PyCharm
# @E-mail: wangyuancong@163.com
'''
Description:
Output: 
Input:
Other notes:
'''
import subprocess
import os
import re


class CmdProcessor:

    def __init__(self):
        self._in_lst_fpath_1 = []
        self._in_lst_fpath_2 = []
        self._wk_dpath = None
        self._out_dpath = None
        # 86 does not have fqtrim
        # self._fqtrim_path = '/home/aggl/wyc/opt/biosoft/fqtrim-0.9.7.Linux_x86_64/fqtrim'  # for jaas server
        self._fqtrim_path = '/home/wangyc/opt/biosoft/fqtrim-0.9.7.Linux_x86_64/fqtrim'  # for 87 server
        # self._btrim_path = '/home/han/opt/btrim64'  # for 86 server
        # self._btrim_path = '/home/aggl/wyc/opt/biosoft/btrim64'  # for jaas server
        self._btrim_path = '/home/wangyc/opt/biosoft/btrim64'  # for 87 server
        # self._paired_seq_file_path = '/public/usr/local/bin/paired_end_trim.pl'  # for jaas server
        # self._paired_seq_file_path = '/home/han/opt/paired_end_trim.pl'  # for 86 server
        self._paired_seq_file_path = '/home/wangyc/opt/biosoft/paired_end_trim.pl' # for 87 server
        self._is_genome = None
        self._prefix_r1 = None
        self._prefix_r2 = None
        self._dic_btrim_out = dict()
        self._ref_path = None

    def fit(self, lst_paired_fpath, ref_path, is_genome=False):
        self._is_genome = is_genome
        self._wk_dpath = os.path.dirname(lst_paired_fpath[0]['fpath_r1'])
        self._out_dpath = os.path.join(self._wk_dpath, 'out')
        self._ref_path = os.path.abspath(ref_path)
        if not os.path.exists(self._out_dpath):
            os.mkdir(self._out_dpath)
        for dic_path in lst_paired_fpath:
            fname1 = os.path.basename(dic_path['fpath_r1'])
            # fname2 = os.path.basename(dic_path['fpath_r2'])
            if re.findall(r'\.f(?:ast)?q(\.gz)?$', fname1) or re.findall(r'\.f(ast)?q\.pe\.gz$', fname1):
                self._in_lst_fpath_1.append(dic_path['fpath_r1'])
                self._in_lst_fpath_2.append(dic_path['fpath_r2'])

    def execute_salmon(self):
        # get the output fnames and fpaths
        print("executing..salmon")
        for i in range(0, len(self._in_lst_fpath_1)):
            fpath_r1 = self._in_lst_fpath_1[i]
            fpath_r2 = self._in_lst_fpath_2[i]
            fname1 = os.path.basename(fpath_r1)
            # fname2 = os.path.basename(fpath_r2)
            self._prefix_r1 = re.split(r'_\d+', fname1)[0]
            # self._prefix_r2 = re.split(r'.f(?:ast)?q', fname2)[0]
            # btrim_out_fname1 = self._prefix_r1 + '.btrim.fq'
            # btrim_out_fname2 = self._prefix_r2 + '.btrim.fq'
            # btrim_out_fpath1 = os.path.join(self._out_dpath, btrim_out_fname1)
            # btrim_out_fpath2 = os.path.join(self._out_dpath, btrim_out_fname2)

            cmd = f'salmon quant -i {self._ref_path} -l A -1 {fpath_r1} -2 {fpath_r2} -p 8 -o ./salmon_res/{self._prefix_r1}/'
            print(cmd)
            if subprocess.check_call(cmd, shell=True) != 0:
                raise SystemCommandError
