
class A:
    def ab(self):
        print("ab--")
        return "a"
        


class B(A):

    A = A
    def ab(self):
        print("abc---")
        return "b"


b = B()

print(b)
print(b.ab())

print("===================")

print(b.A.ab(b))
