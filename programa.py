from PyQt5.QtWidgets import QApplication
from gui import *
from main import *


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.extraer)
        self.plainTextEdit.setPlainText('https://www.vinosylicores.co.uk')
        self.lineEdit_2.setText("contact")  # direccionamiento
        self.lineEdit.setText(".wix")

    def extraer(self):
        urls = self.plainTextEdit.toPlainText().replace('\n', ',').split(',')
        excluir = self.lineEdit.text().split(',')
        direccionamiento = self.lineEdit_2.text().split(',')
        print('------')
        print(urls)
        print(excluir)
        print(direccionamiento)
        correos = ""
        cantidad_de_correos = 0
        for i in urls:
            resultado = extraer_correo2(i, direccionamiento, excluir)
            cantidad_de_correos += len(resultado)
            for j in resultado:
                correos = correos + j + ','
        self.plainTextEdit_2.setPlainText(correos)
        self.statusbar.showMessage('un total de {} correos encontrados'.format(cantidad_de_correos), 5000)


app = QApplication([])
gui = MainWindow()
gui.show()
app.exec_()
