# -*- coding: utf-8 -*-
import argparse


def init_parser(subparser):
    parser = subparser.add_parser(
        'sub',
        help='整数求差命令',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)  # 向参数Help添加默认值的帮助消息格式化程序。

    parser.add_argument(
        'numbers',
        nargs='+',
        help='请输入相减的数,以空格分割 ', type=int)


def main(args):

    number_len = len(args.numbers)

    for i in range(number_len):
        if i == 0:
            sum = args.numbers[i]
        else:
            sum = sum - args.numbers[i]

    str_val = " - ".join([str(i) for i in args.numbers])

    str_val = str_val + " = " + str(sum)
    if args.verbose <= 0:
        print(sum)
        # pass  # 无日志
    elif args.verbose == 1:
        print(str_val)

        # 简单描述
    elif args.verbose > 1:
        print("有" + str(len(args.numbers)) + "个数相减")
        print(str_val)
        # 详情描述
    else:
        print(sum)
