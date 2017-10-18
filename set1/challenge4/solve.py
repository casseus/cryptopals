#!/usr/bin/python

with open("4.txt", 'r') as inf, open("out.txt", 'w') as outf:
    myList = list()
    for line in inf.readlines():
        i = line.strip().decode("hex")
        # weighted system: if single xor then for most part the upper nibble will be differ by only 1 bit at either 1 or 2.
        # With that assumption shift and count to see if 75% of characters are only off by at most 3 in upper nibble
        # 75 percent is used because the result from Challenge 3 yielded 79 percent.
        # Note this solutions assumes the sentence is beginning with a letter.
        count = 1
        base = ord(i[0]) >> 4
        for x in range(1, len(i)):
            val = ord(i[x]) >> 4
            if abs(base - val) <= 3:
                count += 1

        if ((count*1.0 / len(i)*1.0)*100 >= 75 ):
            myList.append(i)

    # find most occuring byte. must occur at least 12 percent. Number derived from challenge 3 where o occurs 12 percent of time
    etaoin = [ord('e'),ord('t'),ord('a'),ord('o'),ord('i'),ord('n'),]
    for res in myList:
        for l in etaoin:
            occur = dict()
            for x in range(0, len(res)):
                val = l ^ ord(res[x])
                if val in occur:
                    occur[val] += 1
                else:
                    occur[val] = 1

            for key, value in occur.iteritems():
                if (value*1.0 / len(res))*100 >= 12:
                    ans = ""
                    for x in range(0, len(res)):
                        ans += chr(key ^ ord(res[x]))
                    outf.write(res.encode("hex"))
                    outf.write(" : key {} = ".format(hex(key)))
                    outf.write(ans)
                    outf.write("\n")

inf.close()
outf.close()
