#!/usr/bin/env python3

__author__  = (
	'Machaku Banga', 'Eusebius Ngemera',
	)
__license__ = 'Apache License, 2.0 (Apache-2.0)'
__version__ = '2012.03.16'

import sys
import re

mamoja=['sifuri','moja','mbili','tatu','nne','tano','sita','saba','nane','tisa']
makumi=['','kumi','ishirini','thelathini','arobaini','hamsini','sitini','sabini','themanini','tisini']
mamia=['','mia moja','mia mbili','mia tatu','mia nne','mia tano','mia sita','mia saba','mia nane','mia tisa']
cheo=['','elfu','milioni','bilioni','trilioni','kuadrilioni','kuintilioni','seksitilioni','septilioni','oktilioni','nonilioni','desilioni','anidesilioni','dodesilioni','tradesilioni','kuatuordesilion','kuindesilioni','seksidesilioni','septendesilioni','oktodesilioni','novemdesilioni','vijintilioni']

class Number:
	
	def __init__(self,number):
		self.number = number
		if self.number is None:
			return ''
		else:
			try:
				int(self.number)
			except TypeError:
				return "Kosa. Hujaingiza inteja."
		
	def get_order(self,number):   # optimise
		order = 0
		while number >= 1000:
			order += 1
			number = number//1000
		return order
		
			
	def get_order_remainder(self,number):
		order = self.get_order(number)
		remainder = number%pow(10,3*order)
		return remainder
		
	def convert_to_words_hundreds(self,number):		# duplicate code here!
		word = ''
		if number < 0:
			number -= number
			word += 'hasi '
		if number <1000:
			if number >= 100:
				hundred = number//100
				hundredr = number%100
				word += mamia[hundred]
				if hundredr:
					ten = hundredr//10
					one = hundredr%10
					if ten:
						word += ' na '+ makumi[ten]
					if one:
						word+=' na '+mamoja[one]
				
			if 100> number >= 10:
				ten = number//10
				one = number%10
				word += makumi[ten]
				if one:
					word +=' na ' +mamoja[one]
			elif number<10:
				word += mamoja[number]
				
		return word
		
	def convert_to_words_order(self,number):	# merge with _r to single proc
		word =''
		order = self.get_order(number)
		hundred = number//pow(10,3*order)
		if order == 1 and hundred >= 100:
			laki = hundred//100
			lakir = hundred%100
			word += 'laki '+ mamoja[laki]
			if lakir:
				word += ' na elfu '+self.convert_to_words_hundreds(lakir)
			return word
		return cheo[order]+' '+self.convert_to_words_hundreds(hundred)
		
	def convert_to_words_order_r(self,number):    # r for reverse
		word =''
		order = self.get_order(number)
		hundred = number//pow(10,3*order)
		if order == 1 and hundred >= 100:
			laki = hundred//100
			lakir = hundred%100
			word += 'laki '+ mamoja[laki]
			if lakir:
				word += ' na '+self.convert_to_words_hundreds(lakir)+' elfu '
			return word
		return self.convert_to_words_hundreds(hundred)+' '+cheo[order]

	def convert_to_digits(self,snumber):
		word=''
		word_l=[]
		digits=list(snumber)
		for i in digits:
			word_l.append(mamoja[int(i)])
		word=' '.join(word_l)
		return word
	
	def get_fraction_digits(self,integer=False):	# better
		try:
			digits =  self.number - self.number//1
			digits = str(digits)[2:]
			if integer and digits !='0':
				digits = int(digits)
		except:
			digits = False
		return digits
	
	def convert_to_words(self):		# exp format not fully supported
		word=''
		fraction = self.get_fraction_digits()
		print '.', fraction
		try:
			number_s=str(self.number)
			number = int(self.number//1)
			print self.number
		except:
			pass
		if number < 0: #number_ls[0][0] == '-':
			self.number = -self.number
			word += 'hasi '
		#number = self.number
		if number < 1000:
			word += self.convert_to_words_hundreds(number)
		else:
			if number%1000:
				terminator =' na '
			else:
				terminator =''
			while number >= 1000:
				order = self.get_order(number)
				digits_in_order = number//pow(10,3*order)
				value_in_order = (digits_in_order * pow(10,3*order))
				next_number = number - value_in_order
				if 0<number%10000<100 and number>=10000 and next_number<100:
					word+=self.convert_to_words_order_r(number)
				else:
					word += self.convert_to_words_order(number)
				number = next_number
				if number:
					word += ','
				if order >= 1 and number:
					word += ' '
			else:
				if terminator:
					word = word[:-2]
					#if number>9:
					word+=terminator
					word += self.convert_to_words_hundreds(number)
		if fraction:
			word+= ' nukta '+self.convert_to_digits(fraction)
		return word

def convert_and_print(a):
	try:
		no = Number(int(a))
	except ValueError:
		try:
			no = Number(float(a))
		except ValueError:
			return
	print (no.convert_to_words())

if __name__ == "__main__":
	try:
		if len(sys.argv) >1:
			for i in range(1,len(sys.argv)):
				convert_and_print(sys.argv[i])
		else:
			while 1:
				no = raw_input()
				if no == '':
					break
				convert_and_print(no)
	except KeyError:
		pass
	
