import multiprocessing
from os import getpid
item = 'catch22'

def worker():
    global item
    p_name = multiprocessing.current_process().name
    print "{} :{}".format(p_name, getpid())
    item += p_name

def main():

    for i in range(5):
        p = multiprocessing.Process(target=worker)
        p.start()

    for p in multiprocessing.active_childern():
        p.join()

    print item
    print "main process ends: {}".format(getpid())

if __name__ == '__main__':
    main()
