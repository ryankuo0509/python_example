#
# Define
#  
def calc_method(a, b = 1):
  print (a * b)

# Tuple  
def args_method(*args):
  print (args)

# Dictionary  
def kwargs_method(**kwargs):
  print (kwargs)
    
#
# Call
#  
calc_method(4)
calc_method(4, 10)
# input arg can NOT follow define order
calc_method(b = 10, a = 2)

# Call by args, Tuple
args_method(1, 2, 3)

# Call by kwargs, Dictionary that key & value 
kwargs_method(name = "eddie", age = 20)  