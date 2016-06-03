import sys
import traceback
debug = True

def safe_float(args):
    try:
        Value = None
        Value = float(args[0]) / 0
    except ValueError , e:
        print e
    except (IndexError , KeyError) , e :
        print e
    except:
        if debug:
            print sys.exc_type
            tb = sys.exc_info()[-1]
            traceback.print_tb(tb)
        else:
            print "internal script error"

    finally:
        print 'i am in finally block'
        return Value

print safe_float([123])