from timeit import timeit  #profiler faster then

def demo1():
    l = [11,33,44,55,66]
    temp = []
    for i in l:
        temp.append(i*i)

def demo2():
    l = [11,33,44,55,66]
    temp = [i*i for i in l]

code1 = """
l = [11,33,44,55,66]
temp = []
for i in l:
  temp.append(i*i)
"""

code2 = """
l = [11,33,44,55,66]
temp = [i*i for i in l]
"""


#print timeit(code1,number=10000)
#print timeit(code2,number=10000)

print timeit(demo1 , number=1000, setup='from __main__ import demo1')
print timeit(demo2 , number=1000, setup='from __main__ import demo2')