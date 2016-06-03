import logging
import glob
from logging.handlers import RotatingFileHandler
from os import stat

fmt_str = "%(asctime)s:%(name)s:%(levelname)s:%(process)s:%(message)s"

log = logging.getLogger()
log.setLevel(logging.DEBUG)


handler = RotatingFileHandler('rollover.log',maxBytes=32,backupCount=4)
handler.setFormatter(logging.Formatter(fmt_str))

log.addHandler(handler)


for i in range(1,25):
    log.debug('dummy log message' + str(i))

for log_file in glob.glob('roll*'):
    print log_file , ':' , stat(log_file).st_size

