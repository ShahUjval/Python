class Box(object):
    def __init__(self,size):
        self.size = size

    def __add__(self,other):
        return Box(self.size + other.size)

    def __str__(self):
        return "[{} size={}]".format(self.__class__.__name__,self.size)

b1 = Box(10)
b2 = Box(20)
b3 = b1 + b2
print b3