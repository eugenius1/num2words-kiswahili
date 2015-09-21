from num2words_sw import Number

test_args = [-1234567.89, -3, -0.25, -0.005, 0 , 0.1, 3.14, 901,
	 2015, 10099, 99000, 101000, 1000001, 100000017, 117000000,
	103050709]

for n in test_args:
    res = Number(n).convert_to_words()
    print n, res
    if res[-1] == ' ':
		print '^......Terminating space'
