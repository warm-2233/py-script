
# 函数装饰器

def dec(f):
    def w(*args, **kwargs):
        print("f.__name__", f.__name__)
        s = f()
        return s
    return w


@dec
def a():
    print("a-----------fun")
    return "233"
def b():
    print("b-----------fun")
    return "111"
print(a())
print("---------------")
print(a())

print("=============================")

dec(b)()