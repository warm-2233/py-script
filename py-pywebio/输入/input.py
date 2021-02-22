from pywebio.input import input, NUMBER

res = input("input ")

print(res, type(res))

res = input("input NUMBER", type=NUMBER)

print(res, type(res))