import logging
import multiprocessing

#application wide logger important

base = logging.getLogger('a')
base.setLevel(logging.DEBUG)

fh = logging.FileHandler('a.log')
fh.setFormatter(logging.Formatter('%(asctime)s : %(name)s :%(message)s'))
#base.handlers