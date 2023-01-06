def print_array(array):
	print(array)

def main():
	line_break = "-------------------------------------------\n"
	fruits = ['apple', 'banana', 'cherry']
	more = ['var1', 'var2', 'var3']
	print(fruits)
	print(more)
	print()
	
	x = fruits.pop(0)
	
	print(x)
	print(fruits)
	print(more)
	
	print()
	
	more.insert(0, x)
	
	print(fruits)
	print(more)
	
	print(line_break)
	text1 = [" ", " ", " " ," ", "one", "two"]
	print(text1)
	print()
	while text1[0] == " ":
		text1.pop(0)
	    
	print(text1)
	print(line_break)
	# VVV can't use this method. If used, any change to any one of the
	# lines in it will apply to all.
	array = [['1', '2', '3']]*4
	print_array(array)
	print('.')
	array[0][1] = '-'
	print_array(array)
	
	

main()