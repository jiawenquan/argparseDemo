#!/usr/bin/env python3
# -*- coding=utf-8 -*-

import os
from setuptools import setup, find_packages

# 这里对不同的打包方式做适配
if os.path.exists("requirements.txt"):
    with open('requirements.txt') as f:
        requirements = f.read().splitlines()  # 按行分割 并返回数组
elif os.path.exists(find_packages()[0] + ".egg-info/requires.txt"):
    with open(find_packages()[0] + ".egg-info/requires.txt") as f:
        requirements = f.read().splitlines()  # 按行分割 并返回数组
else:
    requirements = []

with open('README.rst', "rb") as f:  # 读取详情介绍
    long_description = f.read()  # 长描述

setup(
    name="argparsedemo",  # 包名
    version='1.0.1',  # 版本
    description="argparse简单的测试 加减乘除命令",
    long_description="argparse简单的测试 加减乘除命令",
    author="贾文权",
    author_email="1173551915@qq.com",
    url="https://github.com/jiawenquan/argparseDemo",
    packages=find_packages(),  # 要打包的项目文件夹，如果参数为空表示打包全部
    include_package_data=True,  # 自动打包文件夹内所有数据
    install_requires=requirements,  # # 安装依赖的其他包
    license="MIT",  # 程序的授权信息 协议
    zip_safe=True,  # 设定项目包为安全，不用每次都检测其安全性,作用未知
    # 程序的所属分类列表
    classifiers=[
        'Development Status :: 1 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: Chinese',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',

    ],
    test_suite="tests",  # 单元测试工具

    entry_points={
        'console_scripts': ['argparsedemo=argparseDemo.command_line:main']
    }
)
