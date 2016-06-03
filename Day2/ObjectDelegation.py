"""
delegation
"""

class nginex(object):
    def __init__(self,state):
        self.state = state

    def __getattr__(self, item):
        return self.state

class Server(object):
    def __init__(self):
        self.serve = nginex("on")

    def __setattr__(self, key, value):
        if hasattr(self,'serve'):
            setattr(self.serve,key,value)
        else:
            self.__dict__[key] = value

    def __getattr__(self, item):   #delegates
        #if item == 'state':
            return getattr(self.serve,item)

        #else:

         #   return self.__dict__[item]

if __name__ == '__main__' :
    s= Server()
    s.version = '2.0'   # calls set attribute
    s.state = 'off'
    #print s.state   # calls get attr
    #print s.version
    print s.serve.__dict__
    print s.state
    print s.version
