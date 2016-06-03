def demo(*args):
    print args

demo()
demo('pypi')
demo(1,2,3,4,5)
l = [1,2,3,4]
demo(l)
demo(*l)  #passing the content fo the argument

t = 'Ujju' , 28
print t
print "I am {} , {} years old".format(*t)


def demo(a,b,*args):
    print a
    print b
    print args

demo(1,2)