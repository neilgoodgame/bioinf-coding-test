"""TODO: module doc..."""

import os
from setuptools import find_packages, setup

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='bertha-commons',
    version='1.5.0',
    author='Duncan Gordon,Michael Mueller,Ernesto Ocampo,Kenan McGrath',
    author_email='duncan.gorden@genomicsenglang.co.uk,michael.mueller@genomicsengland.co.uk,ernesto.ocampo@genomicsengland.co.uk,kenan.mcgrath@genomicsengland.co.uk',
    url='https://github.com/genomicsengland/bertha',
    description='Packages used across the various systems: the central workflow definition, '
                'a library for grabbing app and logging configuration files and '
                'a wrapper for file locations.',
    license='Internal GEL use only',  # example license
    classifiers=[
        'Environment :: Other Environment',
        'Intended Audience :: Other Audience',
        'License :: Other/Proprietary License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Scientific/Engineering',
    ],
    packages=find_packages(),
    include_package_data=True,

    install_requires=[
        # test requirements
        'pytest'
    ],
    setup_requires=[
        'pytest-runner'
    ]
)
