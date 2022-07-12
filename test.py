# -*- coding: utf-8 -*-
__author__ = 'Guibin'

import sys
import json


def parse(file_name):
    data = []
    with open(file_name) as f:
        c = f.readlines()
        for row in c:
            rlist = row.strip().split()
            k = rlist[-4]
            v = rlist[-1]
            data.append({'txHash': k, 'st': int(v)})
    return data


def compute(data):
    length = len(data)
    resp = []
    for i in range(length):
        if i == length - 1:
            break
        t1 = data[i].get('st')
        t2 = data[i+1].get('st')
        v = t2 - t1
        resp.append({'txHash': data[i+1].get('txHash'), 'value': v})
    return resp

if __name__ == '__main__':
    f = sys.argv[1]
    data = parse(f)
    print(json.dumps(compute(data)))
