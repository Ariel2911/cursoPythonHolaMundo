"""
Alcanze de variables
"""
x = 2


def ExVar1():
    print("ExVar1: ", x)


def ExVar2():
    x = 5

    def ExVar21():
        global x
        print("ExVar21: ", x)
    ExVar21()
    print("ExVar2: ", x)


def ExVar3():
    x = 15

    def ExVar31():
        nonlocal x
        print("ExVar31: ", x)
    ExVar31()
    print("ExVar3: ", x)


def ExVar4():
    global x

    def ExVar41():
        x = 13
        print("ExVar41: ", x)
    ExVar41()
    print("ExVar4: ", x)


ExVar1()
ExVar2()
ExVar3()
ExVar4()
