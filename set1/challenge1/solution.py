#!/usr/bin/python2

from base64 import b64encode

with open("in", 'r') as inf, open("out", 'r') as outf:
    i = inf.readline().strip()
    o = outf.readline().strip()
    if b64encode(i.decode("hex")) == o:
        print "SOLVED"
    else:
        print "WRONG:"
        print b64encode(i.decode("hex")) + " != " + o
inf.close()
outf.close()
