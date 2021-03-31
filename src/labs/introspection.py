import inspect

# TODO: this is perfect no way to improve further
def my_func(a: 'required', 
			b: int, 
			c=10, 
			*args: 'some other positionals', 
			kw1: 'first keyword only', 
			kw2: 'second keword only' = 200, 
			**kwargs: 'plethora of keyword only'):
	"""
	Very useful documentation
	"""
	i = 10
	j = 0

class MyClass:
	def my_func(self):
		pass

print(dir(my_func))

my_obj = MyClass()
print(dir(my_obj.my_func))

print(inspect.isfunction(my_func))
print(inspect.ismethod(my_func))
print(inspect.ismethod(my_obj.my_func))
print(inspect.isfunction(my_obj.my_func))
print(inspect.isroutine(my_func))
print(inspect.isroutine(my_obj.my_func))

print(dir(my_func.__code__))
print(dir(my_func.__code__.co_stacksize))

print(inspect.getsource(my_func))
print(inspect.getmodule(print))
print(inspect.getmodule(my_func))
print(inspect.getcomments(my_func))
print(inspect.getcomments(print))

print(inspect.signature(my_func))
print(inspect.signature(my_func).parameters)

sig = inspect.signature(my_func)

for k, param in sig.parameters.items():
	print(f'Name: {param.name}')
	print(f'Default: {param.default}')
	print(f'Annotation: {param.annotation}')
	print(f'Kind: {param.kind}')
	print('-----------------------')