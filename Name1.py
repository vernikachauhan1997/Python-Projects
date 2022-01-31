def funcA(num1,num2):
    return num1 - num2

def funcB(num1,num2):
    return num1 + num2

if __name__=='__main__' : #Whatever we will write inside this main function that will not automatically execute while importing into another file to use.
    print(funcA(15,6))
    print(funcB(10,16))
    print(__name__)
    