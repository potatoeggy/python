import sys
from PySide2.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget
from PySide2.QtCore import Qt, Slot

class MainWindow(QWidget):
	def __init__(self):
	 super().__init__()

if __name__ == "__main__":
	app = QApplication(sys.argv)

	main = MainWindow()
	main.show()
	sys.exit(app.exec_())