a = 100
b = 100
c = b

from sys import getrefcount

print getrefcount(a)

del a , b

print c
print getrefcount(c)

n = 257
m = 257
print id(n)
print id(m)

s = 'ujju shah'
t = 'ujju shah'
print id(s)
print id(t)


l = [1,2,3,4, 'v']  #shallow copy copy by refrence
backup = l

l.pop()

print l
print backup

print id(l)
print id(backup)


#deepcopy
l = [1,2,3,4, 'v']
from copy import deepcopy

backupn = deepcopy(l)

l.pop()

print l
print backupn







