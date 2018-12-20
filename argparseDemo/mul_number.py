# -*- coding: utf-8 -*-
import argparse


def init_parser(subparser):
    parser = subparser.add_parser(
        'mul',
        help='整数求积命令',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)  # 向参数Help添加默认值的帮助消息格式化程序。

    parser.add_argument(
        'numbers',
        nargs='+',
        help='请输入相乘的数,以空格分割 ', type=int)


def main(args):
    # 这里运行逻辑
    # print("sssssss")
    sum = 1

    str_val = ""
    for number in args.numbers:
        sum = sum * number

    str_val = " * ".join([str(i) for i in args.numbers])
    # print(str_val)
    str_val = str_val + " = " + str(sum)
    if args.verbose <= 0:
        print(sum)
        # pass  # 无日志
    elif args.verbose == 1:
        print(str_val)
        # print(sum)

        # pass  # 简单描述
    elif args.verbose > 1:
        print("有" + str(len(args.numbers)) + "个数相乘")
        print(str_val)
        # pass  # 详情描述
    else:
        print(sum)
