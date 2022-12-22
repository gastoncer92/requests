from PyQt5.QtWidgets import QApplication

from gui import *
from funciones import *


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        # self.pushButton.clicked.connect(self.extraer)
        self.pushButton.clicked.connect(self.extraer2)
        self.plainTextEdit.setPlainText('https://www.vinosylicores.co.uk')
        self.lineEdit_2.setText("contact")  # direccionamiento
        self.lineEdit.setText(".wix")

    def extraer2(self):
        # limpiar plainTextEdit_2
        self.plainTextEdit_2.clear()

        # preparar listas de urls
        urls = self.plainTextEdit.toPlainText().strip().replace('\n', ',').split(',')
        # preparar listas de exluir y direcciones
        excluir = self.lineEdit.text().strip().split(',')
        # preparar listas de direcciones
        direccionamiento = self.lineEdit_2.text().strip().split(',')

        # preparo variable de la lista de correos en str
        textoPlanoCorreo = ""
        # preparo variable de la cantidad de correos para statusbar
        cantidad_de_correos = 0

        # determino patros para filtrar los correos
        patron = r'[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}'

        # lista de correos
        correos = ListaDeCorreos(urls, direccionamiento, excluir, patron)

        # for i in correos:
##            resultado = extraer_correo4(i, direccionamiento, excluir)
            # cantidad_de_correos += len(correos)
            # for j in correos:
            #     textoPlanoCorreo = textoPlanoCorreo + j + ','
        # self.plainTextEdit_2.setPlainText(textoPlanoCorreo)
        # self.statusbar.showMessage('un total de {} correos encontrados'.format(cantidad_de_correos), 5000)
    # def extraer(self):
    #     # limpiar plainTextEdit_2
    #     self.plainTextEdit_2.clear()
    #
    #     # preparar listas de urls
    #     urls = self.plainTextEdit.toPlainText().strip().replace('\n', ',').split(',')
    #     # preparar listas de exluir y direcciones
    #     excluir = self.lineEdit.text().strip().split(',')
    #     # preparar listas de direcciones
    #     direccionamiento = self.lineEdit_2.text().strip().split(',')
    #
    #     # preparo variable de la lista de correos en str
    #     textoPlanoCorreo = ""
    #     # preparo variable de la cantidad de correos para statusbar
    #     cantidad_de_correos = 0
    #
    #     # determino patros para filtrar los correos
    #     patron = r'[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}'
    #
    #     # lista de correos
    #     correos = ListaDeCorreos(urls, direccionamiento, excluir, patron)
    #
    #     for i in correos:
    #         # resultado = extraer_correo4(i, direccionamiento, excluir)
    #         cantidad_de_correos += len(correos)
    #         for j in correos:
    #             textoPlanoCorreo = textoPlanoCorreo + j + ','
    #     self.plainTextEdit_2.setPlainText(textoPlanoCorreo)
    #     self.statusbar.showMessage('un total de {} correos encontrados'.format(cantidad_de_correos), 5000)


app = QApplication([])
gui = MainWindow()
gui.show()
app.exec_()
