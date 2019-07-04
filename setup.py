from setuptools import setup, find_packages
from os import path
import re


def packagefile(*relpath):
    return path.join(path.dirname(__file__), *relpath)


def read(*relpath):
    with open(packagefile(*relpath)) as f:
        return f.read()


def get_version(*relpath):
    match = re.search(
        r'''^__version__ = ['"]([^'"]*)['"]''',
        read(*relpath),
        re.M
    )
    if not match:
        raise RuntimeError('Unable to find version string.')
    return match.group(1)


setup(
    name='embeval',
    version=get_version('src', 'embeval', '__init__.py'),
    description='A framework for embedding evaluation automation and visualization.',
    long_description=read('README.md'),
    url='https://github.com/RubenBranco/embeval',
    author='Ruben Branco',
    author_email='ruben.branco@outlook.pt',
    license='GPLv3',
    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    keywords='',
    install_requires=[
        'pseq',
        'gensim',
    ],
    package_dir={'': 'src'},
    packages=find_packages('src'),
)
