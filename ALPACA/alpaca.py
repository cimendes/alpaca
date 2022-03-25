#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Purpose
-------

This is the main script of alpaca.

"""


import os
import sys
import pickle
import shutil
import argparse

try:
    from __init__ import __version__
    from utils import (utils,
                       constants as ct)
    from plot import (completness_plot, 
                      lx_plot,
                      nax_plot,
                      ngx_plot,
                      plot_contig_size,
                      plot_gap_reference,
                      plot_gap_sizes,
                      plot_misassembly,
                      plot_snp)
except:
    from ALPACA import __version__
    from ALPACA.utils import (utils,
                    constants as ct)
    from ALPACA.plot import (completness_plot, 
                            lx_plot,
                            nax_plot,
                            ngx_plot,
                            plot_contig_size,
                            plot_gap_reference,
                            plot_gap_sizes,
                            plot_misassembly,
                            plot_snp)


version = __version__


def main():

    print('\nalpaca version: {0}'.format(version))
    print('Authors: {0}'.format(ct.authors))
    print('Github: {0}'.format(ct.repository))
    print('Contacts: {0}\n'.format(ct.contacts))

    matches = ["--v", "-v", "-version", "--version"]
    if len(sys.argv) > 1 and any(m in sys.argv[1] for m in matches):
        print(version)
        sys.exit(0)

    # Check python version
    #python_version = pv.validate_python_version()



if __name__ == "__main__":

    main()