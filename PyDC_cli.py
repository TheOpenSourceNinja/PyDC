#!/usr/bin/python3
#This file can be used from the command line

import sys
from PyDC_backend import DCTranslator

translator = DCTranslator()
translator.decode( "" )
print( translator.encode( 2 ) )
