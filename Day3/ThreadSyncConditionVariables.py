import threading
from time import sleep
from random import random
import logging as log
from Queue import Queue    #message queue

fmt = "%(threadName)s: %(message)s"
log.basicConfig(level=log.DEBUG,format=fmt)

def task(delay, lock , q):
    log.debug('waits for the notifications : %s' % delay)
    with lock:
        lock.wait()   # wait and notifyall
        log.debug('resumed the execution')
        q.put(delay + delay)
        q.join()
        log.debug('quits')

def main():

    ca = threading.Condition()
    q = Queue()

    for i in range(5):
        t = threading.Thread(target=task , args=(random(),ca,q))
        t.start()

    sleep(2)

    with ca:
        ca.notifyAll()   #notifyall

    for i in range(5):
        print q.get()
        q.task_done()


    print "main thread ends....."


if __name__ == '__main__':
    main()