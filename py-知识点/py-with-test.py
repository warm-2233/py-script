'''
print("start")


class A:

    def __init__(self):
        pass

    def __enter__(self):
        print("enter")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):

        return True

    def test(self):
        print("test")
        return 1


a = A()

print(a)
print(a.test())

print("="*100)

with A() as a:
    print(a)
    print(a.test())

print("end")
'''





from contextlib import contextmanager

@contextmanager
def test():
    print("enter")

    yield 1
    try:
        print("try")
        1/0
    except ZeroDivisionError:
        print('ZeroDivisionError')




with test() as a:
    print(a)
    pass

