#!/usr/bin/env python
# load_QNdesc.py
# load the quantum number descriptions for a 'case' into the MySQL table
# QNdesc from a text file

import sys
import MySQLdb

# MySQL username and password is read in from hitrandb_configs.py,
# somewhere on the $PYTHONPATH (probably in $HOME/research/pyHAWKS/)
from hitrandb_configs import *

try:
    text_name = sys.argv[1]
except:
    print 'usage is $s <text filename>' % sys.argv[0]
    sys.exit(1)

conn = MySQLdb.connect(host="localhost", user=username,
                       db=dbname, passwd=password)
cursor = conn.cursor()

textfile = open(text_name, 'r')
header = textfile.readline()
s_caseID, case_prefix = header.split()
caseID = int(s_caseID)

lines=[]
for line in textfile.readlines():
    line = line.strip()
    if not line or line[0] == '#':
        continue
    lines.append(line)
if len(lines) % 12:
    print len(lines)
    print 'invalid format: each quantum number should have the four entries:'
    print 'name, attributes, description, restriction and each entry has'
    print 'three lines in text, HTML and LaTeX'
    sys.exit(1)

# don't resolve '\t' etc when reading in text:
command = 'SET SESSION sql_mode=NO_BACKSLASH_ESCAPES'
cursor.execute(command)

command = 'DELETE FROM QNdesc WHERE caseID=%d' % caseID
cursor.execute(command)

nqn = len(lines)/12
print 'there are %d quantum numbers described for %s' % (nqn, case_prefix)
s_case_prefix = "'%s'" % case_prefix
for il in range(nqn):
    print '--'
    qn_lines = lines[il*12:il*12+12]
    s_qn_lines = []
    for qn_line in qn_lines:
        if '"' in qn_line:
            print 'double-quote character, \'"\', forbidden'
            sys.exit(1)
        if qn_line != '\N':
            s_qn_lines.append(r'"%s"' % qn_line)
        else:
            s_qn_lines.append(r'\N')
    command = 'INSERT INTO QNdesc (caseID, case_prefix, name, HTMLname,' \
             ' LaTeXname, attributes, HTMLattributes, LaTeXattributes,' \
             ' description, HTMLdescription, LaTeXdescription,' \
             ' restrictions, HTMLrestrictions, LaTeXrestrictions) SELECT' \
             ' %d, %s, %s' % (caseID, s_case_prefix, ', '.join(s_qn_lines))
    #print command
    #print '%s:%s' % (case_prefix, s_qn_lines[0])
    cursor.execute(command)


