#!/usr/bin/env python
import fileinput
import re
start_table_pattern = re.compile("^COPY (\w+) \(([\w, ]+)\) FROM stdin;")
table_name = None
fields = None
insert_mode = False

for line in fileinput.input():
    if insert_mode:
        if line == "\\.\n":
            insert_mode = False
            continue
        values = [ v == '\\N' and 'NULL' or "'%s'" % v \
                   for v in line[:-1].replace("'", "''").split("\t") ]
        print "INSERT INTO %s (%s) VALUES (%s);" \
            % (table_name, fields, ", ".join(values))
    else:
        start_table = start_table_pattern.match(line)
        if start_table:
            table_name = start_table.group(1)
            fields = start_table.group(2)
            insert_mode = True
            continue
        print line,
        
