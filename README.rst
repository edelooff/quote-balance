Quote balancer
##############

Simple Python script to check whether files have balanced quotes.

The script works on a line-by-line basis so will incorrectly mark multi-line
quotes as being in error. I'm happy to accept PRs to fix or improve that.

How to use
==========

.. code-block::

    usage: check-quote-balance [-h] [-e EXT] [-r] target

    positional arguments:
      target             Target to check for balance

    optional arguments:
      -h, --help         show this help message and exit
      -e EXT, --ext EXT  file extension that should be matched for directory
                         searches. This option can be provided multiple times. If
                         no extensions are set, the default checks only "py"
                         extensions
      -r, --recursive    recursively check all files in target directory


The provided target can be either a  single file, or a directory. When the target is a file, only that file will be checked. if the target is a directory, all files in that directory matching the configured extensions will be checked.

By default, directory checks are not performed recursively, checking only files immediately contained. Recursive checks are possible with the use of an additional option.