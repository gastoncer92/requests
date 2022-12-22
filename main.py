import pyperclip as pc
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
        self.pushButton_2.clicked.connect(self.copiar)

    def copiar(self):
        texto = self.plainTextEdit_2.toPlainText()
        pc.copy(texto)
        self.statusbar.showMessage("texto copiado!", 3000)

    def extraer(self):
        # limpiar plainTextEdit_2
        self.plainTextEdit_2.clear()

        # preparar listas de urls
        urls = self.plainTextEdit.toPlainText().strip().replace('\n', ',').split(',')
        # preparar listas de exluir y direcciones
        excluir = self.lineEdit.text().strip().split(',')
        print(excluir)
        print(excluir)
        # preparar listas de direcciones
        direccionamiento = self.lineEdit_2.text().strip().split(',')

        # preparo variable de la lista de correos en str
        textoPlanoCorreo = ""
        # preparo variable de la cantidad de correos para statusbar

        # determino patros para filtrar los correos
        patron = r'[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}'
        # lista de urls
        lista_de_urls = ListaDeCorreos(urls, direccionamiento, excluir, patron)
        lista_de_correos = []
        for i in lista_de_urls:
            list_email = extraer(i, excluir, patron)

            if list_email is not None:
                for correo in list_email:
                    if correo not in lista_de_correos:
                        lista_de_correos.append(correo)
                for correo in lista_de_correos:
                    textoPlanoCorreo = textoPlanoCorreo + ',' + correo
                self.plainTextEdit_2.setPlainText(textoPlanoCorreo[1:])
                self.statusbar.showMessage(
                    "Se obtuvieron {} correos de {} paginas web".format(len(lista_de_correos), len(lista_de_urls)))

            else:
                pass

    def extraer2(self):
        # limpiar plainTextEdit_2
        self.plainTextEdit_2.clear()

        # preparar listas de urls
        urls = self.plainTextEdit.toPlainText().strip().replace('\n', ',').split(',')
        # preparar listas de exluir y direcciones
        excluir = self.lineEdit.text().strip().split(',')
        print(excluir)
        print(excluir)
        # preparar listas de direcciones
        direccionamiento = self.lineEdit_2.text().strip().split(',')

        # preparo variable de la lista de correos en str
        textoPlanoCorreo = ""
        # preparo variable de la cantidad de correos para statusbar

        # determino patros para filtrar los correos
        patron = r'[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}'
        # lista de urls
        lista_de_urls = ListaDeCorreos2(urls, direccionamiento, excluir, patron)
        lista_de_correos = []
        print("excluir: {}".format(excluir))
        if excluir == [''] and direccionamiento != ['']:
            print("no hay excluir")
            for i in lista_de_urls:
                list_email = extraer_sin_excluir(i, patron)
                if list_email is not None:
                    for correo in list_email:
                        if correo not in lista_de_correos:
                            lista_de_correos.append(correo)
                    for correo in lista_de_correos:
                        textoPlanoCorreo = textoPlanoCorreo + ',' + correo
                    self.plainTextEdit_2.setPlainText(textoPlanoCorreo[1:])
                    self.statusbar.showMessage(
                        "Se obtuvieron {} correos de {} paginas web".format(len(lista_de_correos), len(lista_de_urls)))
                else:
                    pass

        elif excluir == [''] and direccionamiento == ['']:
            print("no hay NADA!")
            for i in lista_de_urls:
                list_email = extraer_sin_direccionamiento(i, excluir, patron)
                print(list_email)
                if list_email is not None:
                    for correo in list_email:
                        print(correo)
                        if correo not in lista_de_correos:
                            lista_de_correos.append(correo)
                    for correo in lista_de_correos:
                        textoPlanoCorreo = textoPlanoCorreo + ', ' + correo
                        self.plainTextEdit_2.setPlainText(textoPlanoCorreo[1:])
                        self.statusbar.showMessage(
                            "Se obtuvieron {} correos de {} paginas web".format(len(lista_de_correos),
                                                                                len(lista_de_urls)))

                else:
                    pass



        else:
            for i in lista_de_urls:
                list_email = extraer(i, excluir, patron)
                if list_email is not None:
                    for correo in list_email:
                        if correo not in lista_de_correos:
                            lista_de_correos.append(correo)
                    for correo in lista_de_correos:
                        textoPlanoCorreo = textoPlanoCorreo + ',' + correo
                    self.plainTextEdit_2.setPlainText(textoPlanoCorreo[1:])
                    self.statusbar.showMessage(
                        "Se obtuvieron {} correos de {} paginas web".format(len(lista_de_correos), len(lista_de_urls)))
                else:
                    pass

        # if excluir == [''] and direccionamiento == ['']:
        #     print('OOOOOOOOO')
        # elif excluir == [''] and direccionamiento != ['']:
        #     print('LLLLLLLLLLLLLLLLLLLLLLLLLLLLLL')
        #
        # elif excluir == [''] and direccionamiento != ['']:
        #     print('HHHHHHHHHHHHHHHHHH')
        # else:
        #     print('¿¿¿¿¿¿')


app = QApplication([])
gui = MainWindow()
gui.show()
app.exec_()
