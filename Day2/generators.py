def demo():
    print "before 1"
    yield 100
    print "after 1"

    print "before 2"
    yield 101
    print "after 2"

g = demo()
value = g.next()
print value
print '-'*30
value = g.next()
print value

print '-'*30
value = g.next()
print value




