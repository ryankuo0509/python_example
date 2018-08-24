class ClassExample(object):
  def __init__(self):
    print ("Hello Python!")

  def __del__(self):
    print ("Goodbye Python!")

  def __str__(self):
    return "This is ClassExample"

  def say_hello(self, words):
    print ("Hello,", words)

  def do_nothing(self):
    pass

  def __private_method(self):
    print ("this is for personal only")

  def get_private_method(self):
    self.__private_method()


Obj_Class = ClassExample()
Obj_Class.say_hello("eddie")
print (Obj_Class)

#Obj_Class.__private_method()
Obj_Class.get_private_method()


#1st testing commit&push in github on VS code