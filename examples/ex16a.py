import ex16

p1 = ex16.Person(name='Ramesh', age=33, city='Chennai')
p1.print_info()
print(dir(p1))
p1._Person__age = 2000
p1.print_info()
