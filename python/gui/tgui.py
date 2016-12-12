import sys
from PyQt4 import QtGui,QtCore

# def main():
#    app = QtGui.QApplication(sys.argv)
#    w = QtGui.QWidget()
#    #b = QtGui.QLabel(w)
#    #b.setText("Hello World!")
#    #w.setGeometry(100,100,200,50)

#    #w.setWindowTitle('PyQt')
#    w.show()
#    sys.exit(app.exec_())
	
# if __name__ == '__main__':
# 	main()

class Window(QtGui.QMainWindow):
	def __init__(self):
		super(Window, self).__init__()
		self.setGeometry(50,50,500,300)
		self.setWindowTitle("Test GUI")
		extractAction = QtGui.QAction("&Quit", self)
		extractAction.setShortcut("Ctrl+Q")
		extractAction.setStatusTip("Leave the app")
		extractAction.triggered.connect(self.closeApplication)
		
		testAction = QtGui.QAction("&Open", self)
		testAction.setShortcut("Ctrl+o")
		testAction.setStatusTip("Open file")

		self.statusBar()
		mainMenu = self.menuBar()
		fileMenu = mainMenu.addMenu('&File')
		fileMenu2 = mainMenu.addMenu('&Test')
		fileMenu.addAction(extractAction)
		fileMenu2.addAction(testAction)


		self.home()

	def home(self):
		btn = QtGui.QPushButton('Quit', self)
		#btn.clicked.connect(QtCore.QCoreApplication.instance().quit)
		btn.clicked.connect(self.closeApplication)
		# what will happen when the btn is clicked^
		btn.resize(100,50)
		btn.move(100,100)
		self.show()

	def closeApplication(self):
		choice = QtGui.QMessageBox.question(self, "Test","Quit or nah?", QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
		if choice == QtGui.QMessageBox.Yes:
			print("Custom close!")
			sys.exit()
		else:
			print("No closing")
def main():
	app = QtGui.QApplication(sys.argv)
	gui = Window()
	sys.exit(app.exec_())


if __name__ == '__main__':
	main()
