#Decoration Function
print("\t\t\tDecoration function")
def decorate(func):
    def func2(B,C):
        A=B+C
        D=C-B
        Q= func(A,D)
    return func2
@decorate
def add(B,C):
    D=B*5
    print(D)
(add(4,5))
    
print("\t\t\tMeta class")
#Metaclass
class MyMetaClass(type):
    def __new__(cls,name,base,dct):
        dct['meta_attribute'] = 'This is a meta attribute'
        return super().__new__(cls,base,name,dct)
class MyClass(metaclass=MyMetaClass):
    class_attribute = 'This is a class attribute'
    
    def __init__(self, value):
        self.instance_attribute = value

my_object = MyClass("Hello!")
print(MyClass.meta_attribute)  
print(my_object.class_attribute)  
print(my_object.instance_attribute) 
