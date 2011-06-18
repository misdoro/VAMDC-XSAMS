#!/usr/bin/env python
# QNdesc2LaTeX.py

import sys
import MySQLdb

# MySQL username and password is read in from hitrandb_configs.py,
# somewhere on the $PYTHONPATH (probably in $HOME/research/pyHAWKS/)
from hitrandb_configs import *

try:
    case_prefix = sys.argv[1]
except:
    print 'usage is %s <case prefix>' % sys.argv[0]
    sys.exit(1)

conn = MySQLdb.connect(host="localhost", user=username,
     db=dbname, passwd=password)
cursor = conn.cursor()

command = 'SELECT id, caseID, name, LaTeXname, LaTeXattributes,' \
         ' LaTeXdescription, LaTeXrestrictions FROM QNdesc WHERE' \
         ' case_prefix = \'%s\' ORDER BY id' % case_prefix
cursor.execute(command)

for row in cursor.fetchall():
    name, LaTeXname, attributes, description, restrictions = row[2:]
    print r'\fbox{'
    print r'\parbox{12cm}{'
    print r'\subsection*{%s}' % LaTeXname
    print r'\subsubsection*{\underline{Element}}'
    print r'\texttt{<%s:%s>}' % (case_prefix, name)
    print r'\subsubsection*{\underline{Attributes}}'
    print '%s.' % attributes
    print r'\subsubsection*{\underline{Description}}'
    print '%s is %s.' % (LaTeXname, description)
    print r'\subsubsection*{\underline{Restrictions}}'
    print r'\begin{itemize}'
    for restriction in restrictions.split('; '):
        print r'\item %s.' % restriction
    print r'\end{itemize}'
    print r'}'
    print r'}'
    print r'\vspace{0.5cm}'

