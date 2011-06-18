#!/usr/bin/env python
import sys
import os
from cases_meta import *

for case_prefix in cases:
    command = './load_QNdesc.py txt/%s-desc.txt' % case_prefix
    print command
    os.system(command)

