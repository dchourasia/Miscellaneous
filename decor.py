def caps(func):
	def inner(a, b):
		print(a, b, 'from decor')
		return 'myHi'
	return inner

@caps
def hi(a, b):
	print('get lost')
	return 'hi'

#decorate = caps(hi)	
#print(decorate())
# decorators are nothing but overloading the function with another function, so now even if you call hi(), it will invoke caps()
# no code written in hi() will be executed unless you explicitely invoke it from caps()
#it is a shortcut of passing the function to other function and then overloading its steps
print(hi(1, 2))