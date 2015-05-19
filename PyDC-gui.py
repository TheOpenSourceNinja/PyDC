#!/usr/bin/python3
#This file is responsible for creating the graphical interface.

import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QClipboard
from PyDC-backend import DCTranslator

class gui:
	def __init__( self ):
		self.translator = DCTranslator()
		self.app = QApplication( [] )
		self.ui = uic.loadUi( "mainWindow.ui" )
		self.ui.show()
		
		self.clipboard = self.app.clipboard()
		
		#connecting signals
		self.ui.pasteButton.clicked.connect( self.paste )
		self.ui.copyButton.clicked.connect( self.copy )
		self.ui.decodeButton.clicked.connect( self.decode )
		self.ui.encodeButton.clicked.connect( self.encode )
		self.ui.species.currentIndexChanged.connect( self.speciesSelected )
		self.ui.subSpecies.currentIndexChanged.connect( self.subSpeciesSelected )
		
		#visibility
		self.ui.subSubSpecies.setEnabled( False )
		
		sys.exit( self.app.exec_() )
	
	def speciesSelected( self, index ):
		print( index )
		
		#Wish I could put a switch statement here
		if( index == 0 ): #Dragons
			self.ui.subSpecies.setEnabled( True )
		elif( index == 1 ): #Humans
			self.ui.subSpecies.setEnabled( True )
		else:
			self.ui.subSpecies.setEnabled( False )
			self.ui.subSubSpecies.setEnabled( False )
	
	def subSpeciesSelected( self, index ):
		print( index )
		
		if( self.ui.species.currentIndex() == 0 ): #Dragons
			if( index == 10 ):
				self.ui.subSubSpecies.setEnabled( True )
			else:
				self.ui.subSubSpecies.setEnabled( False )
		elif( self.ui.species.currentIndex() == 1 ): #Humanoids
			if( index == 2 ):
				self.ui.subSubSpecies.setEnabled( True )
			else:
				self.ui.subSubSpecies.setEnabled( False )
	
	def paste( self ):
		self.ui.DCTextBox.setPlainText( self.clipboard.text() )
	
	def copy( self ):
		self.clipboard.setText( self.ui.DCTextBox.toPlainText() )
		
	def decode( self ):
		self.translator.decode( self.ui.DCTextBox.toPlainText() )
	
	def encode( self ):
		encodedText = self.translator.encode( self.ui.spinBox.value() )
		if( encodedText is not None ):
			self.ui.DCTextBox.setPlainText( encodedText )

main = gui()
