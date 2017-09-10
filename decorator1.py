def my_decorator(some_func):
	def wrapper():
		print "Inside my_decorator function"

		num = 10
		if num ==10:
			print "Yes"
		else:
			print "No"

		some_func()
		print "After calling the function"
	return wrapper

if __name__ == "__main__":
	my_decorator()
