from setuptools import setup

import ALPACA

VERSION = ALPACA.__version__

setup(
  name = 'ALPACA',
  packages = ['ALPACA'],
  version = VERSION,
  description = 'Standalone Last (Meta)Genomic Assembler Standing.',
  author = 'Inês Mendes',
  author_email = 'cimendes@medicina.ulisboa.pt',
  url = 'https://github.com/cimendes/alpaca', 
  keywords = ['de novo assembly', 'benchmark', 'draft genome quality'],
  install_requires = ['numpy>=1.14.0','plotly>=1.12.9', 'pandas>=0.22.0'],
  python_requires = '>=3.4',
  include_package_data = True,
  entry_points={'console_scripts': ["alpaca.py = ALPACA.alpaca:main",
                                    "alpaca = ALPACA.alpaca:main"]
                }
)