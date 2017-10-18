#!/usr/bin/python

import sys

reXOR = "ICE"

with open("in", 'r') as inf, open("out", 'r') as outf:
    stream = ""
    for line in inf.readlines():    
        stream += line#strip()
    # for some reason the first new line character is used but not the last 
    stream = stream[:-1]
    answer = ""
    for i in xrange(0, len(stream), len(reXOR)):
        s = stream[i:i+len(reXOR)]
        answer += ''.join(chr(ord(a) ^ord(b)) for a,b in zip(s, reXOR))

    solution = ""
    for line in outf.readlines():
        solution += line.strip()

    if answer != solution.decode("hex"):
        errmsg = solution + " !=\n" + answer.encode("hex")
        sys.exit(errmsg)

    print "SOLVED"

inf.close()
outf.close()
