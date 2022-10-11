#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        result1 = fct(*args)
        return result1
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return None
