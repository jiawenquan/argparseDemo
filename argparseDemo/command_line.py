#!/usr/bin/env python3
# -*- coding=utf-8 -*-
import argparse
import argparseDemo.add_number as add_number
import argparseDemo.sub_number as sub_number
import argparseDemo.mul_number as mul_number
import argparseDemo.div_number as div_number
import argparseDemo.sex_choose as sex_choose


def main():
    # parser = argparse.ArgumentParser(
    #     description='这是一个argparse的使用测试小Demo',
    #     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    #
    # parser.add_argument(
    #     '--verbose',
    #     help='Print logs (-1: no logs, 0: progress indicator, 1+: increased verbosity)',
    #     default=1, type=int)
    #

    parser = argparse.ArgumentParser(
        description="这是一个argparse的使用测试小demo",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument(
        "--verbose",
        help="打印日志(-1:无日志，0:进度指示器，1+:增加的详细程度)",
        default=1, type=int
    )
    sub_parsers = parser.add_subparsers(dest='command')

    # init subparsers
    add_number.init_parser(sub_parsers)
    sub_number.init_parser(sub_parsers)
    mul_number.init_parser(sub_parsers)
    div_number.init_parser(sub_parsers)
    sex_choose.init_parser(sub_parsers)
    args = parser.parse_args()
    try:
        if args.command == 'add':
            add_number.main(args)

        elif args.command == 'sub':
            sub_number.main(args)
        elif args.command == 'mul':
            mul_number.main(args)
        elif args.command == 'div':
            div_number.main(args,parser)
        elif args.command == 'sex':
            sex_choose.main(args)
        else:
            parser.print_help()
    except Exception as e:
        print(e)
        parser.print_help()

    # try:
    #     if args.command == 'convert':
    #         pass
    #         # convert.main(args)
    #     elif args.command == 'info':
    #         # info.main(args)
    #         pass
    #     elif args.command == 'merge':
    #         pass
    #         # merger.main(args)
    #     elif args.command == 'export':
    #         pass
    #         # export.main(args)
    #     else:
    #         parser.print_help()
    # except Exception as e:
    #     print(e)
    #     parser.print_help()


if __name__ == '__main__':
    main()
