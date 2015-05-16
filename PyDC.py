#!/usr/bin/python3
#This file can be used by itself from the command line or as the back-end for the GUI.

class DCTranslator:
	def decode( self, coded ):
		"Accepts a single string as the argument. Processes it. Returns true if processing worked or false if there was an error."
		if( type( coded ) is not str ):
			return False
		
		print( coded )
		return True
	
	def encode( self ):
		"Accepts several arguments. Processes them into a string. Invalid arguments are ignored."
		return ""

translator = DCTranslator()
translator.decode( "" )
print( translator.encode() )
