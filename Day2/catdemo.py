import argparse
import fileinput
import sys

parser = argparse.ArgumentParser()
parser.add_argument('filename',nargs='+')
parser.add_argument('-n' , help='adds line number', action='store_true')
parser.add_argument('-o','--output',help='output filename')

args = parser.parse_args()
temp = None


if args.output:
    temp = sys.stdout
    sys.stdout = open(args.output,'w')

#content = open(args.filename).readlines()


for line in fileinput.input(args.filename):
    if args.n:
        print "{:>6} {}".format(fileinput.lineno(),line),
    else:
        print line,

if temp:
    sys.stdout = temp