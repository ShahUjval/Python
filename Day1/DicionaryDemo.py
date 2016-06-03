from time import ctime
from collections import defaultdict
from os import listdir,stat
from os.path import isfile,join
from pprint import pprint as pp

from json import dump,dumps

class DirectoryListing(object):

    def __init__(self,dname):
        self.dname = dname
        self.content = defaultdict(dict)
        self.__read_dir()

    def __read_dir(self):
        for fname in listdir(self.dname):
            abs_path = join(self.dname,fname)

            if isfile(abs_path):
                file_stat = stat(abs_path)
                size, mtime = file_stat.st_size , file_stat.st_mtime
                self.content[self.dname][fname] = size,ctime(mtime)

    def __del__(self):
        print "getting destroyed : {}".format(self)

class DirectoryList2JSON(DirectoryListing):

    def __init__(self,dname):
        super(DirectoryList2JSON,self).__init__(dname)

    def to_json(self, json_file=None):
        if json_file:
            dumps(self.content, open(json_file,'w'), indent=4)
        else:
            return dumps(self.content, indent=4)

if __name__ == '__main__':
    #d = DirectoryListing('D:\Amex')
    #pp(dict(d.content))
    d = DirectoryList2JSON('D:\Amex')
    pp(dict(d.content))
    print d.to_json('tmp.json')
