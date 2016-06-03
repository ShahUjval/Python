class Demo(object):
    lang = 'python'
    def __init__(self, pm):
        self.package_manager = pm

    def get_package_manager(self):
        return self.package_manager

        #print "i am in constructor : {}".format(self)

    def __del__(self):
        print "getting destroyed : {}".format(self)

if __name__ == '__main__':
    d = Demo('pypi')
    print d.get_package_manager()
    print d.lang