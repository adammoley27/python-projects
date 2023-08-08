class Parent:
    pass


class Child(Parent):
    pass

class Childson(Child):
    pass

class Grandson(Childson):
    pass

# Checking these are subclasses - true
print(issubclass( Child, Parent))
print(issubclass(Childson, Child))

# checking these are subclasses - false
print(issubclass( Parent, Child))
print(issubclass(Child, Childson))


print(issubclass(Childson, Parent))

# Grand
print(issubclass(Grandson, Parent))