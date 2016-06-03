from sys import argv
import fileinput
import re

class GrepMe(object):

    def __init__(self):
        self.pattern = argv.pop(1)
        self.__do_match()

    def __do_match(self):
        for line in fileinput.input():
            if re.search(self.pattern,line,re.I):
                print line,

GrepMe()