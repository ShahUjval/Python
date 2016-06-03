class RangeError(Exception):
    def __str__(self):
        return "{}: {}\n{}".format(self.__class__.__name__,self.args[0],self.args[1])

def check4limit(value):
    if not 0.3 <= value <= 0.7:
        err_msg = "Value far too high : {}".format(value)
        remedy = "value should be with in 0.3 and 0.7"
        raise RangeError(err_msg , remedy)

try:
    check4limit(0.9)
except RangeError , e:
    print e