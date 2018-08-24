
# by  %
print("int:%d float:%.2f string:%s" % (1, 99.3, 'Justin'))

# by {} and .format()
import math
print("PI = {.pi}" .format(math))
print("{:.2f}".format(3.1415926))

print("11(Dec):{:d}".format(11))
print("11(Hex):{:x}".format(11))
print("11(Hex):{:#x}".format(11))


# example
print("Web site:{name}, Address:{url}".format(name="Rookie", url="www.runoob.com"))

# Set parameter by diction (**)
diction = {"name": "Rookie", "url": "www.runoob.com"}
print("Web site:{name}, Address:{url}".format(**diction))
 
# Set parameter by list index 
my_list = ['Rookie', 'www.runoob.com']
print("Web site:{0[0]}, Address:{0[1]}".format(my_list))  