#!/bin/sh
cat $1 | sed -e "s/xsams\/$2/xsams\/$3/g" > temp.file
mv temp.file $1
