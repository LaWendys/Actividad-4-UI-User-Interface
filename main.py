from PySide2.QtWidgets import QApplication
from mainwindow import MainWindow
import sys

#Aplicacion de Qt
app = QApplication()
#Se crea un Boton con la palabra Hola
window = MainWindow()
#Se hace visible el boton
window.show()
#Qt loop
sys.exit(app.exec_())