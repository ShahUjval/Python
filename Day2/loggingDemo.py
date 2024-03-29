import logging

fmt_str = "%(asctime)s:%(name)s:%(levelname)s:%(process)s:%(message)s"

logger = logging.getLogger()

logger.setLevel(level=logging.DEBUG)

fmt = logging.Formatter(fmt_str)

fh = logging.FileHandler('access.log')

fh.setFormatter(fmt)

sh = logging.StreamHandler()
sh.setFormatter(fmt)

logger.addHandler(fh)

logger.debug('a sample log message')

