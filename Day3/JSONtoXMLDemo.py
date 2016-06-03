from xml.etree.ElementTree import Element , SubElement , ElementTree
from json import load
from pprint import pprint as pp

class JSON2XML(object):

    def __init__(self,json_file,xml_file):
        self.json_file = json_file
        self.xml_file = xml_file
        self.__do_parse()

    def __do_parse(self):
        params = ['size','mtime']
        content = load(open(self.json_file))
        root_tag = Element('directories')

        for dir_name in content:
            dir_tag = SubElement(root_tag,'directory',attrib={'name' : dir_name})

            for file_name in content.get(dir_name):
                size , mtime = content.get(dir_name).get(file_name)
                values = {'size' : str(size) , 'mtime' : mtime}

                file_tag = SubElement(dir_tag,'file',atrib=values)
                file_tag.text = file_name

        doc = ElementTree(root_tag)
        doc.write(self.xml_file)

if __name__ == '__main__':
    JSON2XML('tmp.json','abc.xml')