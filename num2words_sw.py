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
		try:
			float(number)
			if isinstance(number, str):
				try:
					self.number = int(number)
				except ValueError:
					self.number = float(number)
			else:
				if (isinstance(number, float) and number.is_integer()):	# removes .0
					self.number = int(number)
				else:
					self.number = number
		except ValueError:
			print "Kosa. Hujaingiza namba."
			self.number = None
		
	def get_order(self,number):
		order = 0
		while number >= 1000:
			order += 1
			number = number//1000
		return order
		
			
	def get_order_remainder(self,number):
		order = self.get_order(number)
		remainder = number%pow(10,3*order)
		return remainder
		
	def convert_to_words_hundreds(self,number):
		word = ''
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
		
	def convert_to_words_order(self,number):
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
		
	def convert_to_words_order_r(self,number):    # reverse
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
	
	def get_fraction_digits(self,integer=False):
		if isinstance(self.number, int) or (isinstance(self.number, float) and self.number.is_integer()):
			return False
		number_s=str(self.number)
		try:
			number_ls = re.split('[.]',number_s)
			digits = number_ls[1]
		except:
			digits = False
		return digits
		
	def convert_to_words(self):
		if self.number == None:
			return None
		word=''
		fraction = self.get_fraction_digits()
		number = abs(int(self.number))
		if self.number < 0:
			word += 'hasi '
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
					word+=terminator
					word += self.convert_to_words_hundreds(number)
		if fraction:
			word+= ' nukta '+self.convert_to_digits(fraction)
		return word

if __name__ == "__main__":
	try:
		for i in range(1,len(sys.argv)):
			print Number(sys.argv[i]).convert_to_words()
	except KeyError:
		pass
	
