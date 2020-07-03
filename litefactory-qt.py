import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.main = MainWidget()
		self.setCentralWidget(self.main)
		self.setWindowTitle("LiteFactory Helper Tool")

class MainWidget(QWidget):
	def __init__(self):
		super().__init__()
		self.main = QVBoxLayout()

		self.topPanel = TopPanel() # temporary, should be status bar i think
		self.main.addWidget(self.topPanel)
		self.setLayout(self.main)

class TopPanel(QWidget):
	def __init__(self):
		super().__init__()
		self.main = QHBoxLayout()
		self.quickButtons = [QPushButton("Install LiteFactory"), QPushButton("Uninstall LiteFactory"), QPushButton("Check for updates")]
		self.quickButtons[1].setEnabled(False)
		self.quickButtons[2].setEnabled(False)

		for i in self.quickButtons:
			self.main.addWidget(i)
		self.setLayout(self.main)

if __name__ == "__main__":
	app = QApplication(sys.argv)

	main = MainWindow()
	main.show()
	sys.exit(app.exec_())