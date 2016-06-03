"""
a sample pythom module
"""

from os import listdir

author = 'Ujju'
version = '0.0.1 beta'

def sqrncube(n=0) :
    """
    sqrncube() ,finds the sqr and cube value of n
    :param n:
    :return:
    """
    return  n**2 , n**3

def ls(path='.') :
    """
    ls() ,finds the sqr and cube value of n
    :param n:
    :return:
    """
    for file_name in listdir(path):
        print file_name


def main() :
    print author
    print sqrncube(5)
    ls()

if __name__ == '__main__':
    main()

