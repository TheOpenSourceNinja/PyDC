#!/usr/bin/python3
#This file is the back-end for the GUI and CLI programs.

class DCTranslator:
	def decode( self, coded ):
		"Accepts a single string as the argument. Processes it. Returns true if processing worked or false if there was an error."
		if( type( coded ) is not str ):
			return False
		
		coded = coded.strip()
		
		print( coded )
		return True
	
	def encode( self, version ):
		"Accepts several arguments. Processes them into a string. Invalid arguments are ignored."
		
		result = "DC"
		if( version == 2 ):
			result += str( version )
		elif( version > 2 ):
			result += str( version )
		
		return result
