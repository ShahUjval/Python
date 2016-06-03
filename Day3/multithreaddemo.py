import threading
from time import sleep
from random import random
import logging as log

fmt = "%(threadName)s: %(message)s"
log.basicConfig(level=log.DEBUG,format=fmt)

def task(delay,lock):
    t_id = threading.currentThread().ident
    t_name = threading.currentThread().getName()

    log.debug('waits for the lock')
    with lock:
        log.debug('acquired the lock')
        sleep(delay)
        print "{} waited for :{}".format(t_name,delay)
        log.debug('release the lock')

def main():
    #lock = threading.Lock()
    lock = threading.Semaphore(1)
    for i in range(5):
        t = threading.Thread(target=task , args=(random(),lock))
        t.start()

        for t in threading.enumerate():
            if t is not threading.currentThread():
                t.join()

        #print "main threads ends........"

if __name__ == '__main__':
    main()