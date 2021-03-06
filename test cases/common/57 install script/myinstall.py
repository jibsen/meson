#!/usr/bin/env python3

import os
import sys

prefix = os.environ['MESON_INSTALL_DESTDIR_PREFIX']

dirname = os.path.join(prefix, sys.argv[1])

os.makedirs(dirname)
with open(os.path.join(dirname, sys.argv[2]), 'w') as f:
    f.write('')
