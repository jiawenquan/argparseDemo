# -*- coding: utf-8 -*-
###互斥选项的应用
import argparse


def init_parser(subparser):
    parser = subparser.add_parser(
        'sex',
        help='可以添加互斥选项 二选一',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)  # 向参数Help添加默认值的帮助消息格式化程序。

    group = parser.add_mutually_exclusive_group()  # 可以添加互斥选项：

    group.add_argument('-female', action='store_true', help="指定性别为女")  # , metavar="female"
    group.add_argument('-male', action='store_true', help="指定性别为男")  # , metavar="male"


def main(args):
    print("输入所有参数值:", args)
    if args.male:
        print("我为男生")
    elif args.female:
        print("我是女生")
    else:
        print("必须选择输入-male or -female ")
