import re

s = 'the python and the python and the perl scripting'

#m = re.match('pythoN',s , re.IGNORECASE)
#m = re.search('pythoN',s , re.IGNORECASE)
#m = re.search('P.*N',s , re.IGNORECASE)  #greedy matches till end
#m = re.search('P.*?N',s , re.IGNORECASE) #least match minimum match

#m = re.findall('P.*N',s , re.IGNORECASE)

for m in re.finditer('python',s , re.IGNORECASE):
    print m.group()
    print m.span()

if m:
    print "got a match"
    print m.group()
    print m.start()
    print m.end()
    print m.span()
else:
    print "failed to match"

print m
