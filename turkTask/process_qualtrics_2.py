# Create the csv needed for R importing
from __future__ import division

import sys

args = sys.argv

print "Args provided:" + str(args)

filename = args[1]
fi = open(filename, 'r')
fo = open(filename + ".R.csv", 'w')

adjectives_file = args[2]
adjectives = [adj_line.rstrip() for adj_line in open(adjectives_file, 'r').readlines()]
print adjectives

header = fi.readline().rstrip().split("\t")
for i in range(len(header)):
    print "Col ", i, header[i]
print header
print "\n*******************************************************************\n"
fi.readline()
fi.readline()
for line in fi:
    print "LINE: ", line

    fields = line.rstrip().split('\t')
    if len(fields) == 101 and fields[0] != "":
        print "len(fields) = ", len(fields)
        question_responses = fields[0:20]
        turker = fields[20]
        lower_bounds = fields[21::4]
        two_devs = fields[22::4]
        means = fields[23::4]
        upper_bounds = fields[24::4]
        assert (len(lower_bounds) == len(means) == len(upper_bounds) == len(two_devs) == len(adjectives)) == True
        for i in range(len(adjectives)):
            adj = adjectives[i]
            resp = float(question_responses[i])
            mu = float(means[i])
            sigma = float(two_devs[i]) / 2
            respDev = abs((resp - mu) / sigma)
            print "resp:", resp
            print "mu: ", mu
            print "sigma: ", sigma
            print "LB: ", lower_bounds[i]
            print "UB: ", upper_bounds[i]
            to_write = [turker, adj, resp, mu, sigma, respDev]
            # fo.write()

    # for f in fields:
    #     print f


fo.close()
