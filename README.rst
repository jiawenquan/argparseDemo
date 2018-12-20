argparseDemo |Build Status|
============================================

.. |Build Status| image:: docs/unknown.png
   :target: https://github.com/jiawenquan/argparseDemo


这是一个 `setuptools <https://github.com/pypa/setuptools>`_ 与 `argparse <https://docs.python.org/3/library/argparse.html>`_ 的使用案例

This is a `setuptools <https://github.com/pypa/setuptools>`_  and `argparse <https://docs.python.org/3/library/argparse.html>`_ use case


Prerequisites
##############

- python 3.6 or 3.*
- windows10 or linux
- pip >= 18.1

Installing
#############
    .. code-block:: bash

        conda create -n argparseDemo_env python=3.6
        activate argparseDemo_env
        (argparseDemoargparseDemo_env) pip install -U setuptools
        (argparseDemo_env) git clone https://github.com/jiawenquan/argparseDemo
        (argparseDemo_env) cd argparseDemo
        (argparseDemo_env) ..\argparseDemo> pip install -e .
        (argparseDemo_env) ..\argparseDemo> python setup.py install


argparseDemo Tests
###################
    .. code-block:: bash

        $ activate argparseDemo_env
        (argparseDemo_env) $ argparsedemo

        (argparseDemo_env) $ argparsedemo add 1 2
        (argparseDemo_env) $ 1 + 2 = 3

        (argparseDemo_env) $ argparsedemo sub 1 2
        (argparseDemo_env) $ 1 - 2 = -1

        (argparseDemo_env) $ argparsedemo mul 1 2
        (argparseDemo_env) $ 1 * 2 = 2

        (argparseDemo_env) $ argparsedemo div 1 2
        (argparseDemo_env) $ 1 / 2 = 0.5




Build a package
##################
- Generate the package file
    .. code-block:: bash

        python setup.py bdist_egg      # *.egg files are generated and easy_install is supported

        python setup.py bdist_wininst  # Generate the *.exe file

        python setup.py sdist          # Generate *.zip/*.tar.gz files to support pip installation

        python setup.py bdist_wheel    # Generate.whl files

- Installation of packaging files
    .. code-block:: bash

        python setup.py install  # The source code installation

        easy_install *.egg     # .egg file installation

        easy_install *.zip/*.tar.gz     # .zip file installation

        pip install *.whl      # .whl file installation




Authors
##########
* **jiawenquan** - *Initial work* - [jiawenquan](https://github.com/jiawenquan)

Versioning
############
`Version: 1.0.1`

Licence
##########

Copyright © 2018 jiawenquan (@Tofull) and contributors
Distributed under the MIT Licence.
