import re

pattern = r'(^root.*)^oper'

with open('D:\passwd.txt') as fp:
    m = re.search(pattern,fp.read(),re.I | re.MULTILINE | re.DOTALL)
    if m:
        print m.group(1)