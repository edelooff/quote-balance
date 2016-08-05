import os
from setuptools import setup, find_packages


def contents(filename):
    here = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(here, filename)) as fp:
        return fp.read()


setup(
    name='quote_balance',
    version='0.1',
    packages=find_packages(),
    author='Elmer de Looff',
    author_email='elmer.delooff@gmail.com',
    description='Tools for checking balanced quotes in source files',
    long_description=contents('README.rst'),
    url='http://variable-scope.com',
    keywords='quote balance checker',
    classifiers=[
        'Development Status :: 3 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python'],
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'check-quote-balance = quote_balance.console_scripts:main']}
)
