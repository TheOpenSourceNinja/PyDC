#!/usr/bin/python3
#This file can be used from the command line

from PyDC_backend import DCTranslator

translator = DCTranslator()
decodeResult = translator.decode( "DC2.Dw Gm L- W T Phwaplt Sks,wl,bh Cja-\bz,v~ Bfl A- Fr N? M--- O H++ $~ F+~ R* Ac++ J+ S---! U- I---# V-- Q---! Tc++[c++] E+" )
print( decodeResult )
#print( translator.encode( 2 ) )
