from xml.etree.ElementTree import Element,ElementTree,SubElement
from time import ctime


root_tg = Element('directory')
root_tg.attrib['name'] = '/tmp'

f1 = SubElement(root_tg,'file',attrib={'size' : '1234' , 'mtime' : ctime()})
f1.text = '/tmp/passwd1234'
#f1.attrib['size'] = '12345'

doc = ElementTree(root_tg)
doc.write('tmp.xml')

from os import getcwd
getcwd()