def myfunc1():
    x="John"
    def myfunc2():
        x="hello"
    myfunc2()
    return x
print(myfunc1())    