class Person:
   def __init__(sel,name,age):
      sel.name=name
      sel.age= age
   def myfunc(sel):
      print("Hi!"+sel.name+". and her age is" + str(sel.age))

p=Person("Jyothi Prasana",18)
p.myfunc()


