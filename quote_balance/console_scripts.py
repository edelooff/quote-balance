import argparse
import os

from . import tree_walker, check_file_balance


def arg_config():
    parser = argparse.ArgumentParser()
    parser.add_argument('target', type=str, help='Target to check for balance')
    parser.add_argument(
        '-e', '--ext',
        action='append',
        dest='file_exts',
        help=(
            'file extension that should be matched for directory searches. '
            'This option can be provided multiple times. If no extensions '
            'are set, the default checks only "py" extensions'),
        metavar='EXT')
    parser.add_argument(
        '-r', '--recursive',
        action='store_true',
        help='recursively check all files in target directory')
    return parser.parse_args()


def check_file(filename):
    """Checks a single file and reports imbalanced quotes."""
    for line, imbalance in check_file_balance(filename):
        print '{name}:{line} {imbalance} quotes are imbalanced'.format(
            name=filename, line=line, imbalance=' and '.join(imbalance))


def check_directory(directory, file_exts, recursive):
    """Check all matching files in the directory, recursive or not."""
    for filename in tree_walker(directory, file_exts, recursive=recursive):
        check_file(filename)


def main():
    args = arg_config()
    target = args.target
    if os.path.isfile(target):
        return check_file(target)
    file_exts = set(args.file_exts) if args.file_exts is not None else {'py'}
    return check_directory(target, file_exts, args.recursive)
