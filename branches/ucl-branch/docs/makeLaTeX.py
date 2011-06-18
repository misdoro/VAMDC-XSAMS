#!/usr/bin/env python
import sys
import os
from datetime import date
from subprocess import Popen, PIPE

try:
    case_prefix = sys.argv[1]
except:
    print 'usage is %s <case prefix>' % sys.argv[0]
    sys.exit(1)

os.system('./QNdesc2LaTeX.py %s' % case_prefix)
(stdout, stderr) = Popen(["./QNdesc2LaTeX.py", case_prefix],
                stdout=PIPE).communicate()

today = date.today()
str_date = today.strftime("%d %B %Y")   # e.g. 17 June 2011

#sys.exit(0)
output = open('test.tex', 'w')
print >>output, r'\documentclass[a4paper]{article} \pagestyle{plain}'
print >>output, r'\setlength\parindent{0ex}'
print >>output, r'\usepackage{amssymb,amsmath}'

print >>output, r"\title{The `Case-By-Case' Schema for Molecular States" \
                r" in XSAMS}"
print >>output, r'\author{Christian Hill\thanks{Email' \
                r' christian.hill@ucl.ac.uk}' \
                r' and Jonathan Tennyson\\ University College London}'
print >>output, r'\date{%s}' % str_date
print >>output
print >>output, r'\begin{document}'
print >>output
#print >>output, r'\maketitle'
#print >>output, r'\pagebreak'
print >>output, r'\section*{%s}' % case_prefix
print >>output, stdout

print >>output, r'\end{document}'

output.close()
