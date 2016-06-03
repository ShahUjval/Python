from pprint import pprint as pp

class Person(object):
    def __init__(self,name,gen):
        self.__name = name
        self.gen = gen

    def __get_info(self):
        print "name : {}".format(self.__name)
        print "Gender : {}".format(self.gen)

if __name__ == '__main__':
    p = Person(gen='female',name='Pam')
    #p.__get_info()
    #p.get_info()
    print p.gen
    #print p.__name
    p._Person__get_info()
    pp(dir(p))