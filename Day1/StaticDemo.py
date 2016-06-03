class Connection(object):
    counter = 0
    max = 5

    def __init__(self):
        Connection.Check4limit()
        Connection.counter += 1
        print "create connections : {}".format(Connection.counter)

    @staticmethod
    def Check4limit():
        if Connection.max == Connection.counter:
            raise Exception('reached maximum allowable limit : {}'.format(Connection.counter))

        return True

    #print Check4limit
    #Check4limit = staticmethod(Check4limit())
    #print Check4limit


if __name__ == '__main__':
    for i in range(10):
        Connection()