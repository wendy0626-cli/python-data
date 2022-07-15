#!/usr/bin/python
# -*- coding:utf-8 -*-
# -*- author:yyy -*-

import xlsxwriter
import re

f = open('/Users/onchain/result1.txt', 'r', encoding="utf-8")
content_list = [i for i in f if 'tx hash' in i]
# print (content_list)
f.close()

workbook = xlsxwriter.Workbook('result1.xlsx')
centered = workbook.add_format({'align': 'center'})

sheet_PR = workbook.add_worksheet('txHash')

sheet_PR.write(0, 0, 'txhash', centered)
sheet_PR.write(0, 1, 'sptime', centered)
# sheet_PR.write(0,2,'datatime',centered)

PR = 1
for j in content_list:
    # print(j.split(' '))
    line_list = [i for i in (j.split(' ')) if i != '']
    print(line_list)
    number_list = re.findall(r'\D(-?\d+)', line_list[-1])
    sheet_PR.write(PR, 0, line_list[-4], centered)
    sheet_PR.write(PR, 1, line_list[-1], centered)
    PR += 1

workbook.close()


