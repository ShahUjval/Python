class Person(object):
    def __init__(self,name,gen):
        self.name = name
        self.gen = gen

    def get_info(self):
        print "name : {}".format(self.name)
        print "Gender : {}".format(self.gen)

class Employee(Person):
    def __init__(self,name,gen,eid,dept,desg):
        self.eid = eid
        self.dept = dept
        self.desg = desg
        """ calling base class version of __init__ """
        super(Employee, self).__init__(name,gen)

    def get_info(self):
        print "eid : {}".format(self.eid)
        print "department : {}".format(self.dept)
        print "designation : {}".format(self.desg)
        super(Employee, self).get_info()

if __name__ == '__main__':
    #p = Person(gen='female',name='Pam')
    p = Employee('Ujju','Male','e514','MR','Tech Specilist')
    p.get_info()
    print type(p)