import fileinput
import re

#print fileinput.input(['D:\passwd.txt' , 'D:\passwd.txt'])


def get_file_object(*filenames):
    return   (open(filename) for filename in filenames)

def readlines(*filenames):
    for fp in get_file_object(*filenames):
        for line in fp:
            yield line

def grep_me(pattern, *filenames):
    for line in readlines(*filenames):
        if re.search(pattern,line):
            print line

grep_me('root','D:\passwd.txt' , 'D:\passwdCopy.txt')

