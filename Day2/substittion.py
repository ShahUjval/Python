import re
import fileinput
s = "daemon:x:2:2:daemon:/sbin:/sbin/nologin"
counter = 0

def fixstar(m):
    global counter
    counter += 1
    return '*' if counter == 3 else m.group()

#s2 = re.sub('[AEIOU]','*',s,flags=re.I)
#s2 = re.sub(':',fixstar,s,flags=re.I)

for line in fileinput.input('D:\passwd.txt',backup='.bak', inplace=True):
    counter = 0
    s2 = re.sub(':',fixstar,line,flags=re.I)
    print s2,
