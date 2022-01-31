l = 45

def function2():
    m= 23
    global l
    l = 32
    print(l)
function2()
print(l) 

def func1():
    l =89
    def func2():
        p = 45
        print(l)


func1()
          