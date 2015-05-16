#!/usr/bin/python3
#This file is responsible for creating the graphical interface.

import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QClipboard
from PyDC import DCTranslator

class gui:
	def __init__( self ):
		self.translator = DCTranslator()
		self.app = QApplication([])
		self.ui = uic.loadUi( "mainWindow.ui" )
		self.ui.show()
		
		self.clipboard = self.app.clipboard()
		
		self.ui.pasteButton.clicked.connect( self.paste )
		self.ui.copyButton.clicked.connect( self.copy )
		
		sys.exit(self.app.exec_())
	
	def paste( self ):
		self.ui.DCTextBox.setPlainText( self.clipboard.text() )
	
	def copy( self ):
		self.clipboard.setText( self.ui.DCTextBox.toPlainText() )

main = gui()
