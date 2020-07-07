
# Given a non-empty string like "Code" return a string like "CCoCodCode".
# 
# 
# string_splosion('Code') → 'CCoCodCode'
# string_splosion('abc') → 'aababc'
# string_splosion('ab') → 'aab'


def string_splosion(str):
	mystring = ""
	for i in range(len(str)):
		mystring = mystring + str[:i+1]
	return mystring



string_splosion("Kasim")


"KKaKasKasiKasim"
strings = string_splosion("Kasim")
print(strings)
