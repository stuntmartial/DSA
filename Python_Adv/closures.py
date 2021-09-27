def func(n1,n2):
    n1=n1;n2=n2

    def func2():
        print(n1,n2)

    return func2

a=func(10,20)
a()
