import sys

from PyQt5.QtWidgets import QApplication, QCheckBox

from Application.MainWindow import MainWindow
from Application.Settings import Settings
from Application.StartOfWork import StartOfWork

app = QApplication(sys.argv)
win = MainWindow()
win1 = StartOfWork()
win2 = Settings()
win.show()
win1.show()
win2.show()
sys.exit(app.exec_())