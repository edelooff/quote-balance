import os

QUOTES = {"'": 'SINGLE', '"': 'DOUBLE'}


def check_file_balance(filename):
    """Yields tuple of line number and quote imbalance for each occurrance."""
    with open(filename) as fp:
        for lineno, line in enumerate(fp, 1):
            imbalance = [text for char, text in QUOTES.items()
                         if line.count(char) % 2]
            if imbalance:
                yield lineno, imbalance


def tree_walker(top, file_exts, recursive=True):
    """Generator for files to check."""
    for root, dirs, files in os.walk(top):
        for name in files:
            if name.rpartition('.')[-1] in file_exts:
                yield os.path.join(root, name)
        if not recursive:
            raise StopIteration
