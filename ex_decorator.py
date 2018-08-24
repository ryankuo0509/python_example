# ------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------
#
# decorator by function call
#
# "logged" is a function to decorator other function that input aru is a function, MUST has return function "with_logging".
# "with_logging" function internal to execute the decorated fucntion "func"  and return the value

def logged(func): 
    def with_logging(*args, **kwargs): 
        print (func.__name__ + " was called")
        return func(*args, **kwargs) 
    return with_logging

# define the function was decorated    
@logged 
def funA(x): 
    print ("funA internal")
    return x + x * x

# Call
print ("[Decorator by Function Call] -------- ")
print ("Call funcA(3):{:d}".format(funA(3)))

# Result
#   funA was called
#   Call funcA(3):12

# ------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------
#
#   decorator by class
#
print ("\n\n")
print ("[Decorator by Class] -------- ")

class entryExit(object):
    def __init__(self, func): 
        print ("__init__ (S)... assign self.func = func")
        self.func = func 
        print ("__init__ (E)")

    def __call__(self, *args): 
        print ("__call__ (S)... execute the decorated function [{:s}] and return value"  .format(self.func.__name__)) 
        ret = self.func(*args) 
        print ("__call__ (E)", self.func.__name__) 
        return ret

# define the function was decorated           
@entryExit 
def funA_decorated(str): 
    print ("funA inside")
    return ("Hello World..." + str)

print ("The example start")
print (funA_decorated("RyanKuo"))


# ------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------
#
#   Where can the decorator be used?
#   extern lib function for debug
#
print ("\n\n")
print ("[Decorator for debug example] -------- ")

def benchmark(func):
    """
    Decorator for  time consume
    """
    import time
    def wrapper(*args, **kwargs):
        t = time.perf_counter()
        res = func(*args, **kwargs)
        print ("Benchmark__"+func.__name__+" take time:", time.perf_counter()-t)
        return res
    return wrapper

def logging(func):
    """
    Decorator for logging
    """
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        print ("Logging__"+func.__name__+"____", args, kwargs)
        return res
    return wrapper

def counter(func):
    """
    Decorator for counting call times
    """
    def wrapper(*args, **kwargs):
        wrapper.count = wrapper.count + 1
        res = func(*args, **kwargs)
        print ("Counter__"+"{:s}__ has been used: {:d} times".format(func.__name__, wrapper.count))
        return res
    wrapper.count = 0
    return wrapper

    
@counter
@benchmark
@logging
def proc_str(string):
    return str(reversed(string))

print ("print reverse str@1st: {:s}" .format(proc_str("Able was I ere I saw Elba")))
print ("\n")
print ("print reverse str@2nd: {:s}" .format(proc_str("A man, a plan, a canoe, pasta, heros, rajahs, a coloratura, maps, snipe, percale, macaroni, a gag, a banana bag, a tan, a tag, a banana bag again (or a camel), a crepe, pins, Spam, a rut, a Rolo, cash, a jar, sore hats, a peon, a canal: Panama!")))






































