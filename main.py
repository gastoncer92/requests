import typing

import pyperclip as pc
from PyQt5.QtWidgets import QApplication, QDockWidget

from funciones import *
from gui import *
from PyQt5.QtCore import QThread
from base import *


# class Hilo(QThread, Ui_MainWindow):
class Hilo(QThread):
    def __init__(self, urls, lista_a_excluir, direccionamiento, patron):
        super(Hilo, self).__init__()
        # self.hilo = Hilo(urls, lista_a_excluir, direccionamiento, patron, exclusiones)
        self.urls_hilo = urls
        self.lista_a_excluir_hilo = lista_a_excluir
        self.direccionamiento_hilo = direccionamiento
        self.patron_hilo = patron
        # self.plainTextEdit_2_hilo = plainTextEdit_2
        # self.exclusiones_hilo = exclusiones

    def run(self):
        urls = self.urls_hilo
        lista_a_excluir = self.lista_a_excluir_hilo
        direccionamiento = self.direccionamiento_hilo
        patron = self.patron_hilo
        # exclusiones = self.exclusiones_hilo
        print('run')
        # lista de urls utilizadas con sus respectivos direccionamientos.
        lista_de_urls = ListaDeCorreos(urls=urls, direccionamiento=direccionamiento)

        # lista unica de correos
        lista_de_correos = extraer_correos_unicos(lista_de_urls, patron)

        # Eliminar los correos que deben ser excluidos
        list_de_correos_sin_excluidos = LimpiarExcluidos(lista_de_correos, lista_a_excluir)

        # meter correos en el resultado
        texto_plano = ''
        for i in list_de_correos_sin_excluidos:
            texto_plano += ', ' + i

        cantidadDeCorreos = CantidadCorreos() + 1
        # print('cantidadDeCorreos: {}'.format(cantidadDeCorreos))
        for i in list_de_correos_sin_excluidos:
            dato = [cantidadDeCorreos, i]
            if not yaExisteCorreo(i):
                CargarProducto(dato)
                cantidadDeCorreos += 1

            # if yaExisteCorreo(i) is False:
            #
            #     CargarProducto(dato)
            #     cantidadDeCorreos += 1
            # else:
            #     pass


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        # self.pushButton.clicked.connect(self.extraer3)
        self.pushButton.clicked.connect(self.generarHilo1)
        # self.plainTextEdit.setPlainText('https://www.vinosylicores.co.uk')
        self.lineEdit_2.setText("contact,contactus,contact-us")  # direccionamiento
        # self.lineEdit.setText(".wix")
        self.pushButton_2.clicked.connect(self.copiar)
        self.cargarCorreos()

    def generarHilo1(self):
        self.plainTextEdit_2.clear()
        # preparar listas de urls
        urls = self.plainTextEdit.toPlainText().strip().replace('\n', ',').split(',')

        # preparar lista de exclusiones
        lista_a_excluir = self.lineEdit.text().strip().split(',')

        # preparar listas de direcciones
        direccionamiento = self.lineEdit_2.text().strip().split(',')
        # determino patros para filtrar los correos
        patron = r'[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}'
        exclusiones = self.lineEdit.text().strip().split(',')
        # plainTextEdit_2 = self.plainTextEdit_2

        # generar hilo
        self.hilo = Hilo(urls, lista_a_excluir, direccionamiento, patron)
        ## def __init__(self, urls, lista_a_excluir, direccionamiento, patron):
        self.hilo.finished.connect(self.al_finalizar)
        # print('hilo {}'.format(type(self.hilo)))
        self.hilo.start()

    def al_finalizar(self):
        # self.plainTextEdit_2.insertPlainText("dddd")
        conn = conexion()
        correos = TodosLosCorreos(conn)
        # print(correos)
        conn.close()
        todos_correos = ''
        for i in range(len(correos)):
            print(correos[i - 1][0])
            todos_correos += correos[i - 1][0] + ', '

        self.plainTextEdit_2.insertPlainText(todos_correos[:-2])

        # self.plainTextEdit_2.setPlainText(correos)

        print('finalizar')

    def copiar(self):
        texto = self.plainTextEdit_2.toPlainText()
        pc.copy(texto)
        self.statusbar.showMessage("texto copiado!", 3000)

    def extraer3(self):
        self.plainTextEdit_2.clear()
        # preparar listas de urls
        urls = self.plainTextEdit.toPlainText().strip().replace('\n', ',').split(',')

        # preparar lista de exclusiones
        lista_a_excluir = self.lineEdit.text().strip().split(',')

        # preparar listas de direcciones
        direccionamiento = self.lineEdit_2.text().strip().split(',')
        # determino patros para filtrar los correos
        patron = r'[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}'
        exclusiones = self.lineEdit.text().strip().split(',')

        # lista de urls utilizadas con sus respectivos direccionamientos.
        lista_de_urls = ListaDeCorreos(urls, direccionamiento)

        # lista unica de correos
        lista_de_correos = extraer_correos_unicos(lista_de_urls, patron)

        # Eliminar los correos que deben ser excluidos
        list_de_correos_sin_excluidos = LimpiarExcluidos(lista_de_correos, lista_a_excluir)

        # meter correos en el resultado
        texto_plano = ''
        for i in list_de_correos_sin_excluidos:
            texto_plano += ', ' + i
        self.plainTextEdit_2.setPlainText(texto_plano[1:])

    def cargarCorreos(self):
        conn = conexion()
        correos = TodosLosCorreos(conn)
        print(correos)
        conn.close()
        todos_correos = ''
        for i in range(len(correos)):
            print(correos[i - 1][0])
            todos_correos += correos[i - 1][0] + ', '

        self.plainTextEdit_2.insertPlainText(todos_correos[:-2])


app = QApplication([])
dbCorreos()
gui = MainWindow()
gui.show()
app.exec_()
