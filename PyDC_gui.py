#!/usr/bin/python3
#This file is responsible for creating the graphical interface.

import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QClipboard
from PyDC_backend import DCTranslator

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
		self.ui.subSubSpecies.currentIndexChanged.connect( self.subSubSpeciesSelected )
		
		self.speciesSelected( 0 )
		
		self.ui.species.addItems( self.translator.species )
		self.ui.gender.addItems( self.translator.gender )
		
		sys.exit( self.app.exec_() )
	
	def setSubSpeciesList( self, newList ):
		while self.ui.subSpecies.count() > 0:
			self.ui.subSpecies.removeItem( 0 )
			
		if( len( newList ) > 0 ):
			self.ui.subSpecies.setEnabled( True )
			self.ui.subSpecies.addItems( newList )
			#self.subSpeciesSelected( 0 )
		else:
			self.ui.subSpecies.setEnabled( False )
			self.ui.subSubSpecies.setEnabled( False )
	
	def setSubSubSpeciesList( self, newList ):
		while self.ui.subSubSpecies.count() > 0:
			self.ui.subSubSpecies.removeItem( 0 )
				
		if( len( newList ) > 0 ):
			self.ui.subSubSpecies.setEnabled( True )
			self.ui.subSubSpecies.addItems( newList )
			#self.subSubSpeciesSelected( 0 )
		else:
			self.ui.subSubSpecies.setEnabled( False )
			self.ui.subSubSubSpecies.setEnabled( False )
	
	def setSubSubSubSpeciesList( self, newList ):
		while self.ui.subSubSubSpecies.count() > 0:
			self.ui.subSubSubSpecies.removeItem( 0 )
				
		if( len( newList ) > 0 ):
			self.ui.subSubSubSpecies.setEnabled( True )
			self.ui.subSubSubSpecies.addItems( newList )
			#self.subSubSubSpeciesSelected( 0 )
		else:
			self.ui.subSubSubSpecies.setEnabled( False )
	
	def speciesSelected( self, index ):
		self.setSubSpeciesList( self.translator.subSpecies[ index ] )
	
	def subSpeciesSelected( self, index ):
		if( len( self.translator.subSubSpecies ) > 0 ):
			if( len( self.translator.subSubSpecies[ self.ui.species.currentIndex() ] ) > 0 ):
				self.setSubSubSpeciesList( self.translator.subSubSpecies[ self.ui.species.currentIndex() ][ index ] )
	
	def subSubSpeciesSelected( self, index ):
		if( len( self.translator.subSubSubSpecies ) > 0 ):
			if( len( self.translator.subSubSubSpecies[ self.ui.species.currentIndex() ] ) > 0 ):
				if( len( self.translator.subSubSubSpecies[ self.ui.species.currentIndex() ][ self.ui.subSpecies.currentIndex() ] ) > 0 ):
					self.setSubSubSubSpeciesList( self.translator.subSubSubSpecies[ self.ui.species.currentIndex() ][ self.ui.subSpecies.currentIndex() ][ index ] )
	
	def paste( self ):
		self.ui.DCTextBox.setPlainText( self.clipboard.text() )
	
	def copy( self ):
		self.clipboard.setText( self.ui.DCTextBox.toPlainText() )
		
	def decode( self ):
		self.translator.decode( self.ui.DCTextBox.toPlainText() )
	
	def encode( self ):
		encodedText = self.translator.encode(
			self.ui.spinBox.value(), #DC version
			self.ui.species.currentIndex(),
			self.ui.subSpecies.currentIndex(),
			self.ui.subSubSpecies.currentIndex(),
			self.ui.subSubSubSpecies.currentIndex(),
			self.ui.gender.currentIndex()
		)
		if( encodedText is not None ):
			self.ui.DCTextBox.setPlainText( encodedText )

main = gui()
