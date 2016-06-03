raiseme = lambda n: n**2 if n>5 else n**3
print raiseme(5)

power = lambda x, n=0: x ** n
print power(5,4)


print {i for i in range(1,11)}

print {i : bin(i) for i in range(1,11)}

g =  (i for i in range(1,11))
for item in g:
     print item