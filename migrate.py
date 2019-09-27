#!/bin/env python3
import os
import logging

from typing import List


def root_lib_dir(dev_env: str) -> str:
    return os.path.join(dev_root, 'lib')

def lib_src_dir(dev_root: str, lib_name: str) -> str:
    return os.path.join(root_lib_dir(dev_root), 'lib{}'.format(lib_name))

def root_include_dir(dev_root: str) -> str:
    return os.path.join(dev_root, 'include')

def include_dir(dev_root: str, lib_name: str) -> str:
    return os.path.join(root_include_dir(dev_root), lib_name)

def root_appl_dir(dev_root: str) -> str:
    return os.path.join(dev_root, 'appl')

# dev/appl/baz/include
def appl_include_dir(dev_root: str, appl_name: str) -> str:
    return os.path.join(root_appl_dir(dev_root), appl_name, 'include')

# dev/appl/baz/src
def appl_src_dir(dev_root: str, appl_name: str) -> str:
    return os.path.join(root_appl_dir(dev_root), appl_name, 'src')

def run(cmd: List[str]):
    logging.info('running: %s', cmd)

def main():

    logging.basicConfig(level=logging.INFO)

    input_dev_root = 'dev'
    bazel_dev_root = 'dev-bazel'

    # determine the library names from the include sub directories
    library_names = os.listdir(root_include_dir(input_dev_root))
    appl_names = os.listdir(os)

    # check that we can find the source code for these libraries
    for library_name in library_names:
        libsrc = lib_src_dir(library_name)
        if not os.path.exists(libsrc):

    logging.info('looking for bazel dev_root=%s...', output_dir)
    if not os.path.exists(output_dir):
        logging.info('%s not found', output_dir)
        os.makedirs(output_dir)

    run(['git', 'mv', os.path.join(output_dir, '*')])

main()
