
def a(f):
    def ba(*args, **kwargs):
        print("A",f,f.__name__)
        return f(*args, **kwargs)
    print("-a")
    return ba
    
def b(f):
    def baq(*args, **kwargs):
        print("b",f, f.__name__)
        return f(*args, **kwargs)
    print("-b")
    return baq
    

@a
@b
def c():
    print("c",c)
    return 123

print(a(b(c)))
print('*'*100)

print(c())


    
    
