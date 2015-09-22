from num2words_sw import Number

def test():
	test_args = [-1234567.89, -3, -0.25, -0.0005, 0 , 0.1,
	 3.141592653589793238, 
	 901, 2015, 10099, 99000, 101000, 1000001, 100000017, 117000000,
	324050709, +5e8,
	'420000000500','mambo']

	for n in test_args:
		res = Number(n).convert_to_words()
		print n, res
		if res and res[-1] == ' ':
			print '^......Terminating space'

if __name__ == "__main__":
	test()
