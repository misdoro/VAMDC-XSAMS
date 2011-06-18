#!/usr/bin/env python
import sys
import os
from subprocess import Popen, PIPE
from cases_meta import *

try:
    version_string = sys.argv[1]
except:
    print 'usage is %s <version string>' % sys.argv[0]
    sys.exit(1)

filename = 'tex/allcases-%s.tex' % version_string
output = open(filename, 'w')
for case_prefix in cases:
    print case_prefix,':', case_descriptions[case_prefix]
    os.system('./QNdesc2LaTeX.py %s' % case_prefix)
    (stdout, stderr) = Popen(["./QNdesc2LaTeX.py", case_prefix],
                    stdout=PIPE).communicate()

    print >>output, r'\section*{%s: %s}' % (case_descriptions[case_prefix],
                                            case_prefix)
    print >>output, stdout
    print >>output, '\n\n'
output.close()

