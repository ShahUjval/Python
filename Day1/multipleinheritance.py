class Prime(object):
    def pprint(self):
        print "pprint from the class prime"

class Alpha(Prime):
    def pprint(self):
        print "pprint from the class alpha"

class Beta(object):
    def pprint(self):
        print "pprint from the class Beta"

class Charlie(Beta , Alpha):
    def pprint(self):
        #super(Charlie,self).pprint()
        super(Alpha,self).pprint()

if __name__ == '__main__':
    Charlie().pprint()
    help(Charlie)