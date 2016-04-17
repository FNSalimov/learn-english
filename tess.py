
def foo():
	global a
	a += 1
	print(a)

a = 5
print(a)
foo()
print(a)