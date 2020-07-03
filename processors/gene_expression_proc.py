#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/6/23 14:02
# @Author : Yuancong Wang
# @Site : 
# @File : gene_expression_proc.py
# @Software: PyCharm
# @E-mail: wangyuancong@163.com
'''
Description:
Output: 
Input:
Other notes:
'''

import pandas as pd
import os


class GeneExprProc:

    def __init__(self):
        self._in_dpath = None
        self._in_salmon_dnames = []
        self._in_fpaths = []
        self._df_tpm = pd.DataFrame()
        self._df_counts = pd.DataFrame()

        self._out_df_tpm_fpath = None
        self._out_df_counts_fpath = None


    def fit(self, in_dpath):
        self._in_dpath = os.path.abspath(in_dpath)
        self._in_salmon_dnames = [dname for dname in os.listdir(self._in_dpath) if os.path.isdir(f'{self._in_dpath}/{dname}')]
        self._in_salmon_dnames.sort()
        self._in_fpaths = [os.path.join(f'{self._in_dpath}/{dname}', 'quant.sf') for dname in self._in_salmon_dnames]

    def merge_tpm(self):
        """
        Name	Length	EffectiveLength	TPM	NumReads
        GRMZM5G889790_T01	345	96.007	0.755963	1.000
        GRMZM5G851921_T01	324	75.118	0.000000	0.000
        GRMZM5G861353_T01	414	165.000	0.000000	0.000
        GRMZM5G844605_T01	321	72.167	3.017052	3.000
        GRMZM5G859187_T01	735	486.000	10.304221	69.000
        GRMZM5G856972_T01	348	99.004	0.733075	1.000
        :return:
        """
        self._df_tpm = pd.read_csv(self._in_fpaths[0], sep='\t', usecols=['Name'])

        # self._df_tpm = df_tpm.loc[:, ['Name']]

        for dname in self._in_salmon_dnames:
            in_path = os.path.join(f'{self._in_dpath}/{dname}', 'quant.sf')
            df_tmp = pd.read_csv(in_path, sep='\t')
            self._df_tpm[dname] = df_tmp.loc[:, 'TPM']
        self._out_df_tpm_fpath = os.path.join(self._in_dpath, 'tpm_result.txt')
        self._df_tpm.to_csv(self._out_df_tpm_fpath, sep='\t', index=None)
        return self._out_df_tpm_fpath

    def merge_counts(self):
        self._df_counts = pd.read_csv(self._in_fpaths[0], sep='\t', usecols=['Name'])

        # self._df_tpm = df_tpm.loc[:, ['Name']]

        for dname in self._in_salmon_dnames:
            in_path = os.path.join(f'{self._in_dpath}/{dname}', 'quant.sf')
            df_tmp = pd.read_csv(in_path, sep='\t')
            self._df_counts[dname] = df_tmp.loc[:, 'NumReads']
        self._out_df_counts_fpath = os.path.join(self._in_dpath, 'counts_result.txt')
        self._df_counts.to_csv(self._out_df_counts_fpath, sep='\t', index=None)
        return self._out_df_tpm_fpath


