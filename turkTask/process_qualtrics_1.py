# Removes the columns

import sys

args = sys.argv

print "Args provided:" + str(args)

filename = args[1]
fi = open(filename, 'r').readlines()[:-1]
fo = open(filename + ".proc1.tsv", 'w')

for line in fi:
    fields = line.rstrip().split('\t')
    fo.write('\t'.join(fields[19:]) + "\n")

fo.close()
