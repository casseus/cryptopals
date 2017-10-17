#!/usr/bin/python2
import sys

with open("in", 'r') as inf, open("xor", 'r') as xorf, open("out", 'r') as outf:
    i = inf.readline().strip()
    x = xorf.readline().strip()
    o = outf.readline().strip()
    if len(i) != len(x):
        sys.exit("incorrect length")

    ret = ''.join(chr(ord(a) ^ ord(b)) for a,b in zip(i.decode("hex"), x.decode("hex")))
    if ret != o.decode("hex"):
        print str(ret.encode("hex")) + " != " + o
        sys.exit("xor failed")

    print "SOLVED"

inf.close()
xorf.close()
outf.close()
