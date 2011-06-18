#!/usr/bin/env python
# make_QNdesc.py
# Make an HTML page listing the quantum number descriptions for the case-by-case XML Schemata
# Christian Hill, 5/6/2010
import sys, os
import MySQLdb
from cases_meta import *

# MySQL username and password is read in from hitrandb_configs.py,
# somewhere on the $PYTHONPATH (probably in $HOME/research/pyHAWKS/)
from hitrandb_configs import *

HTMLpathname='/Users/christian/research/schemata/XSAMS/ucl-xsams'

try:
    version_string = sys.argv[1]
except:
    print 'usage is %s <version string>' % sys.argv[0]
    sys.exit(1)

conn = MySQLdb.connect(host="localhost", user=username,
     db=dbname, passwd=password)
cursor = conn.cursor()

def write_HTML_preamble(css_file):
    print >>htmlfile,'<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"'
    print >>htmlfile,'   "http://www.w3.org/TR/xhtml1/xhtml1-strict.dtd">'
    print >>htmlfile,'<html xmlns="http://www.w3.org/1999/xhtml"' \
                     ' xml:lang="en">'
    print >>htmlfile,'<head>'
    print >>htmlfile,'   <meta http-equiv="content-type" content="text/html;' \
                     ' charset=iso-8859-1"/>'
    print >>htmlfile,'   <meta name="author" content="Christian Hill"/>'
    print >>htmlfile,'   <meta name="description" content="VAMDC, University' \
       ' College London, UCL, XML Schema, XSAMS, Case-by-Case, Spectroscopy"/>'
    print >>htmlfile,'   <meta name="robots" content="noindex, nofollow"/>'
    print >>htmlfile,'   <title>Case-by-Case XML Schemata - Quantum Number' \
                     ' Descriptions</title>'
    print >>htmlfile,'   <link rel="stylesheet" href="%s" type="text/css"' \
                     ' media="screen"/>' % css_file
    print >>htmlfile,'</head>'
    print >>htmlfile,'<body>'

def write_XML_preamble():
    print >>xmlfile,'<?xml version="1.0" encoding="UTF-8"?>'
    print >>xmlfile,'<vr:capability xmlns:vr=' \
                    '"http://www.ivoa.net/xml/VOResource/v1.0"' 
    print >>xmlfile,'   standardID="ivo://vamdc/std/TAP-XSAMS"' \
                    ' xsi:type="tx:TapXsamsCapability"'
    print >>xmlfile,'   xmlns:tx="http://vamdc.eu/schema/capability' \
                    '/TAP-XSAMS/20100609"'
    print >>xmlfile,'   xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"'
    print >>xmlfile,'   xsi:schemaLocation="http://www.ivoa.net/xml/' \
                    'VOResource/v1.0'
    print >>xmlfile,'   http://www.ivoa.net/xml/VOResource/v1.0'
    print >>xmlfile,'   http://vamdc.eu/schema/capability/TAP-XSAMS/20100609' \
                    ' TAP-XSAMS-20100609.xsd">'

def write_HTML_file(htmlfile, css_file):
    write_HTML_preamble(css_file)

    print >>htmlfile,'<div id="container">'
    print >>htmlfile,'   <h2 class="pagetitle">%s</h2>'\
            % case_descriptions[case_prefix]
    print >>htmlfile,'   <div id="content">'

    print >>htmlfile,'<ul>'
    print >>htmlfile,'  <li>case prefix: %s</li>' % case_prefix
    print >>htmlfile,'  <li>case ID: %s</li>' % caseIDs[case_prefix]
    print >>htmlfile,'</ul>'

    print >>xmlfile,'   <case name="%s" href="http://xsams.svn.sourceforge'\
        '.net/viewvc/xsams/branches/vamdc-working/cases/%s.xsd">'\
                % (case_prefix, case_prefix)
    print >>xmlfile,'      <title>%s</title>' % case_descriptions[case_prefix]

    command = 'SELECT name, HTMLname, attributes, HTMLattributes,' \
              ' description, HTMLdescription, restrictions, HTMLrestrictions' \
              ' FROM QNdesc WHERE case_prefix="%s" ORDER BY id' % case_prefix
    cursor.execute(command)
    for row in cursor.fetchall():

        name, HTMLname, attributes, HTMLattributes, description,\
            HTMLdescription, restrictions, HTMLrestrictions = row
        if HTMLname is None:
            HTMLname=name

        print >>htmlfile,'<div class="QN">'
        print >>htmlfile,'<h4>%s</h4>' % HTMLname
        print >>htmlfile,'<h5>XML Element</h5>'
        print >>htmlfile,'<p><tt>%s:%s</tt></p>' % (case_prefix,name)
        print >>htmlfile,'<h5>Description</h5>'
        print >>htmlfile,'<p>%s is %s.</p>' % (HTMLname,HTMLdescription)
        print >>htmlfile,'<h5>Attributes</h5>'
        print >>htmlfile,'<p>%s</p>' % (HTMLattributes)
        print >>htmlfile,'<h5>Restrictions</h5>'
        print >>htmlfile,'<p>%s</p>' % (HTMLrestrictions)
        print >>htmlfile,'</div>'

        print >>xmlfile,'      <qn name="%s" tag="%s:%s">%s</qn>'\
            % (name, case_prefix, name, description)

    print >>htmlfile,'</div>'
    print >>htmlfile,'   </div>'
    print >>htmlfile,'</body>'
    print >>htmlfile,'</html>'

# XML quantum number description file    
XMLfilename='%s/docs/xml/cases-%s.xml' % (HTMLpathname, version_string)
xmlfile=open(XMLfilename,'w')
write_XML_preamble()

for case_prefix in cases:
    HTMLfilename = '%s/docs/html/%s-%s.html' % (HTMLpathname, case_prefix,
                                                version_string)
    htmlfile = open(HTMLfilename, 'w')
    write_HTML_file(htmlfile, css_file='layout2.css') 
    htmlfile.close()

    print >>xmlfile,'   </case>'
conn.close()

print >>xmlfile,'</vr:capability>'
xmlfile.close()

# finally, write a menu page:
HTMLfilename='%s/docs/html/QNdesc.html' % HTMLpathname
htmlfile=open(HTMLfilename,'w')
write_HTML_preamble('layout2.css')
print >>htmlfile,'<div id="container">'
print >>htmlfile,'   <h2 class="pagetitle">Case-by-Case Quantum Number' \
                 ' Descriptions</h2>'
print >>htmlfile,'   <div id="content">'

print >>htmlfile,'<ol>'
for case_prefix in cases:
    print >>htmlfile,'  <li><a href="%s-%s.html">%s: %s</li>'\
        % (case_prefix, version_string, case_prefix,
           case_descriptions[case_prefix])
print >>htmlfile,'</ol>'
print >>htmlfile,'</div>'
print >>htmlfile,'</div>'
print >>htmlfile,'</body>\n</html>'
