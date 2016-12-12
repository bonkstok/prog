#firstgui
import sys
from PyQt4 import QtGui, QtCore
class demowind(QtGui.QWidget):
	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self, parent)
		self.setGeometry(300,300,200,200)
		self.setWindowTitle('Johnny\'s first gui')
		quit = QtGui.QPushButton('Close', self)
		quit.setGeometry(30,150,50, 50) #left align, height, width btn, height btn
		self.connect(quit, QtCore.SIGNAL('clicked()'), QtGui.qApp,QtCore.SLOT('quit()'))

app = QtGui.QApplication(sys.argv)
dw = demowind()
dw.show()
sys.exit(app.exec_())