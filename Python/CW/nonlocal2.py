def foo():
    name="Geeks"
    def bar():
        nonlocal name
        name="GeeksforGeeks"
    bar()
    print(name)
foo()        