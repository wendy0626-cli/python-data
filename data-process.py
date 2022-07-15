#!/usr/bin/python
# -*- coding:utf-8 -*-
# -*- author:yyy -*-

import sys
import os

KEY_WORD = '耗时'
COUNTER = 0
COUNT_MAP = {}


def generate_data(k):
    if k in COUNT_MAP:
        COUNT_MAP[k] = COUNT_MAP.get(k) + 1
    else:
        COUNT_MAP[k] = 1


def filter_file(cost):
    if cost < 10:
        k = '0-9'
    elif cost < 100:
        k = '10-99'
    elif cost < 200:
        k = '100-199'
    elif cost < 300:
        k = '200-299'
    elif cost < 800:
        k = '300-799'
    else:
        k = '800'
    generate_data(k)


def read_file(file_name):
    with open(file_name) as fn:
        for i in fn:
            if KEY_WORD not in i:
                continue
            try:
                t_str = i.split(':')[-1].strip()
                filter_file(int(t_str))
            except Exception as e:
                print('Error: {0}, Content: {1}'.format(e, i))
                continue


def dumps_data():
    print('RESULT:')
    for k, v in COUNT_MAP.items():
        print('{} ==> {}'.format(k, v))


def main():
    args = sys.argv
    if len(args) != 2:
        print('Invalid args, Example: {0} filename'.format(args[0]))
        sys.exit(2)
    f = args[1]
    if not os.path.exists(f):
        print('Not found file: {0}'.format(f))
        sys.exit(2)
    read_file(f)
    dumps_data()


if __name__ == '__main__':
    main()
