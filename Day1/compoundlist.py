mat = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [4,5,6,11]
]

print [c for r in mat if len(r)==3 for c in r if c%2]

ul = sorted(
    [l.split(':')[0] for l in open('D:\passwd.txt') if l.startswith('a')]
)

print enumerate(ul)

for ind , item in enumerate(ul,1):
    print ind , ':' ,item


lol = [l.rstrip().split(':') for l in open('D:\passwd.txt') if l.endswith('bash\n')]
def sortkey(users):
    return int(users[2])
sorted(lol, key=sortkey) #sort based on zeroth element   key will be a callback object

data = sorted(lol,key = lambda record: int(record[2]))
print data[0]
print data[-1]


for user_info in data:
    print "|{:>12} |{:<22}| {}|".format(user_info[2],user_info[0],user_info[-1])




