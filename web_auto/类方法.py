'''
Python有3种方法，静态方法（staticmethod），类方法（classmethod）和实例方法。下面用代码举例。

对于一般的函数foo(x)，它跟类和类的实例没有任何关系，直接调用foo(x)即可。
'''

def foo(x):
    print("running foo(%s)" % x)

foo("test")

'''
在类A里面的实例方法foo(self, x)，第一个参数是self，我们需要有一个A的实例，才可以调用这个函数。
'''

class A:
    def foo(self, x):
        print("running foo(%s, %s)" % (self, x))

# A.foo(x) 这样会报错
a = A()
a.foo("test")
'''
当我们需要和类直接进行交互，而不需要和实例进行交互时，类方法是最好的选择。
类方法与实例方法类似，但是传递的不是类的实例，而是类本身，第一个参数是cls。
我们可以用类的实例调用类方法，也可以直接用类名来调用。 
'''


class A:
    class_attr = "attr"

    def __init__(self):
        pass

    @classmethod
    def class_foo(cls):
        print("running class_foo(%s)" % (cls.class_attr))


a = A()
a.class_foo()
A.class_foo()

'''
静态方法类似普通方法，参数里面不用self。
这些方法和类相关，但是又不需要类和实例中的任何信息、属性等等。如果把这些方法写到类外面，
这样就把和类相关的代码分散到类外，使得之后对于代码的理解和维护都是巨大的障碍。
而静态方法就是用来解决这一类问题的。
'''

log_enabled = True


class A:
    class_attr = "attr"

    def __init__(self):
        pass

    @staticmethod
    def static_foo():
        if log_enabled:
            print("log is enabled")
        else:
            print("log is disabled")


A.static_foo()