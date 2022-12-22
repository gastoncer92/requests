from PyQt5.QtWidgets import QApplication

from funciones import *
from gui import *


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

        # lista de urls
        lista_de_urls = ListaDeCorreos(urls, direccionamiento, excluir, patron)
        lista_de_correos = []
        # print(lista_de_urls)
        # print(lista_de_urls)
        for i in lista_de_urls:
            print(i)
            list_email = extraer(i, excluir, patron)
            for correo in list_email:
                if correo not in lista_de_correos:
                    lista_de_correos.append(correo)
        print('lista_de_correos: {}'.format(lista_de_correos))
        for correo in lista_de_correos:
            textoPlanoCorreo= textoPlanoCorreo+','+correo
        self.plainTextEdit_2.setPlainText(textoPlanoCorreo[1:])


app = QApplication([])
gui = MainWindow()
gui.show()
app.exec_()
