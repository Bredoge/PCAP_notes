def def_para(name = "illy"):	#	domyślny parametr
	print(f"the name is {name}")

def is_odd(num):
	if(num%2 == 1):
		return True	#	zwracanie wartości
	else:
		return False

def pass_to_f(name):	#	odbieranie przekazywanej funkcjii
	the_num = 43
	print(f"hello {name}")
	if(is_odd(the_num)):
		print(f"{the_num} is odd")
	def_para()


def say_hello(): #	najprościej funkcja
	print("hello world !!")
	pass_to_f("Jane")	#	przekazwyanie zmiennej do funkcji

say_hello()

#	czytaj z dołu do góry