#!/usr/bin/env python
import fileinput
import re

mode = "clone"
start_table_pattern = re.compile("^COPY (\w+) \(([\w, ]+)\) FROM stdin;")
for line in fileinput.input():
    if mode == "clone":
        start_table = start_table_pattern.match(line)
        if start_table:
            table_name = start_table.group(1)
            fields = start_table.group(2)
            mode = "insert"
            continue
        print line,
    else:
        if line == "\\.\n":
            mode = "clone"
            continue
        values = [ v == '\\N' and 'NULL' or "'%s'" % v for v in line[:-1].split("\t") ]
        print "INSERT INTO %s (%s) VALUES (%s);" % (table_name, fields, ", ".join(values))
        
