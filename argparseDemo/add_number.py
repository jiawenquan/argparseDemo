# -*- coding: utf-8 -*-
import argparse


def init_parser(subparser):
    parser = subparser.add_parser(
        'add',
        help='整数求和命令',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)  # 向参数Help添加默认值的帮助消息格式化程序。

    parser.add_argument(
        'numbers',
        nargs='+',
        help='请输入相加的数,以空格分割 ', type=int)


def main(args):
    # 这里运行逻辑
    # print("sssssss")
    sum = 0
    str_val = ""
    for number in args.numbers:
        sum = sum + number
        # str_val = str_val + str(number) + " + "

    str_val = " + ".join([str(i) for i in args.numbers])

    str_val = str_val + " = " + str(sum)
    if args.verbose <= 0:
        print(sum)
        # pass  # 无日志
    elif args.verbose == 1:
        print(str_val, end=' ')

        # pass  # 简单描述
    elif args.verbose > 1:
        print("有" + str(len(args.numbers)) + "个数相加")
        print(str_val)
        # pass  # 详情描述
    else:
        print(sum)
