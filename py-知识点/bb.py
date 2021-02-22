
def a(s):
	print("a")
	print(s)
	def b():
		print("b")
		return s
	return b



b = a(2)

print(b)

print(b())