# -*- coding: utf-8 -*-
import os

name = '_tools_aib3'

version = '0.1.0'

tools = [
]

requires = [
    'mega_logger-0+<1',
    'python-3+<4',
]

tests = {
    'lint': {
        'command': "flake8 python",
        'requires': ['flake8']
    },
    'black': {
        'command': "black python --line-length 120",
        'requires': ['black'],
    },
    'integ': {
        'command': 'pytest -sv --cov=python --cov-report term-missing tests',
        'requires': ['pytest-7+<8', 'pytest_cov-4+<5'],
    }
}

# Set releases to be project tools
config = {
  "release_packages_path": os.environ.get('REZ_TOOLS_RELEASE_PATH'),
}

def commands():
    import os
    import pathlib

    env.PATH.append('{this.root}/bin')
    env.PYTHONPATH.append('{this.root}/python')
    env.MEGALIS_CONFIG_DIRS.append("{this.root}/config")

    # Set OCIO
    ocio_directory = '{}/ocio/'.format(this.root)
    print("ocio_directory", ocio_directory)
    ocio_directory = pathlib.Path(ocio_directory)
    env.OCIO = str(ocio_directory.joinpath('config.ocio'))

    # Find CDL
    cdl_directory = ocio_directory.joinpath('luts/cdls')
    cdl_name = '{}_{}.cdl'.format(os.getenv('SEQ'), os.getenv('SHOT'))
    cdl_filepath = cdl_directory.joinpath(cdl_name)
    cdl_filepath = cdl_filepath if cdl_filepath.exists() else cdl_directory.joinpath('default.cdl')
    env.SHOT_CDL = str(cdl_filepath)


format_version = 2
