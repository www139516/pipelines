#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/6/24 10:13
# @Author : Yuancong Wang
# @Site : 
# @File : merge_data.py
# @Software: PyCharm
# @E-mail: wangyuancong@163.com
'''
Description:
Output: 
Input:
Other notes:
'''
import argparse
from processors.gene_expression_proc import GeneExprProc


def main():
    parser = argparse.ArgumentParser(description="Trim the sequencing data in the directory.")
    parser.add_argument('-d', '--directory', help='The directory where you put the sequencing files.')
    args = parser.parse_args()
    gene_proc = GeneExprProc()
    gene_proc.fit(args.directory)
    gene_proc.merge_tpm()
    gene_proc.merge_counts()


if __name__ == '__main__':
    main()
