import re

import requests

url4 = 'https://www.vinosylicores.co.uk'  # /contact
patron1 = r'[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}'


# bueno
def extraer_correo(url, direccionamiento='', excluir=[]):
    registro = []
    if direccionamiento == '':
        respuesta = requests.get(url)
    else:
        respuesta = requests.get(url + '\\' + direccionamiento)
    if '200' in str(respuesta):
        print("es correcto")
        extracto = re.findall(patron1, respuesta.text)
        print(extracto)
        for index, i in enumerate(extracto):
            for exc in excluir:
                if exc in i:
                    print("{} tiene {}".format(i, exc))
                else:
                    print("{} no tiene {}".format(i, exc))
                    registro.append(i)
        print(registro)
    else:
        print("presenta error")


def extraer_correo2(url, direccionamiento=[], excluir=[]):
    registro = []
    # if direccionamiento==['']
    for j in direccionamiento:

        if j == '':
            print("no hay redirrecionamiento")
            respuesta = requests.get(url)
        else:
            print(url + '/' + j)
            respuesta = requests.get(url + '/' + j)
        if '200' in str(respuesta):
            print("es correcto")
            extracto = re.findall(patron1, respuesta.text)
            print(extracto)
            for index, i in enumerate(extracto):
                print('index={}\ni={}'.format(index, i))
                if excluir == ['']:
                    registro.append(i)
                else:
                    # print('----------------')
                    # print('----------------')
                    # print(excluir)
                    # print('----------------')
                    # print('----------------')
                    for exc in excluir:
                        if exc in i:
                            print("{} tiene {}... no lo tengo que guardar".format(i, exc))
                        else:
                            print("{} no tiene {}...lo tengo que guardar".format(i, exc))
                            registro.append(i)
            print(registro)
            return registro

        else:
            print("presenta error")


def extraer(url, excluir, patron):
    #registro:list -donde iran los correos filtrados
    registro = []

    respuesta = requests.get(url)
    if existeUrl(url):
        extracto = re.findall(patron, respuesta.text)
        for index, i in enumerate(extracto):
            for exc in excluir:
                if exc in i:
                    pass
                    # print("{} tiene {}".format(i, exc))
                else:
                    # print("{} no tiene {}".format(i, exc))
                    registro.append(i)
        # print('---------')
        # print(registro)
        # print('---------')
        return registro
    else:
        return None


def existeUrl(url):
    if '200' in str(requests.get(url)):
        return True
    else:
        return False


def ListaDeCorreos(urls=[''], direccionamiento=[''], excluir=[''], patron=r'[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}'):
    """
    Retorna una lista de correos extridos de la lista de urls administrada

    :param urls: list
    :param direccionamiento: list
    :param excluir: list
    :param patron: str
    :return: list
    """
    ## preparo una lista vacía en la que iran todos los correos
    todasLasUrl = []
    # ver si direccionamiento y excluir tienen contenido
    if direccionamiento != [''] and excluir != ['']:
        ## tienen ambos contenido

        ## meto en la lista todasLasUrl las url originales
        for i in urls:
            todasLasUrl.append(i)
        ## recorro las direcciones para agregarla a las urls administradas
        for t in direccionamiento:
            ## recorro las url y les agrego nuevas url con las direcciones extras
            for i in urls:
                todasLasUrl.append(i + '/' + t)

        ## retorno todas las urls preparadas
        return todasLasUrl

    elif direccionamiento == [''] and excluir == ['']:
        # print("no hay direccionamiento ni excluir!")

        for i in urls:
            todasLasUrl.append(i)
        return todasLasUrl
    else:
        # print("no hay direccionamiento o no hay excluir!!")
        if direccionamiento == ['']:
            # print("no hay direccionamiento")

            for i in urls:
                todasLasUrl.append(i)
            return todasLasUrl

        else:
            # print("no hay excluir")
            ## meto en la lista todasLasUrl las url originales
            for i in urls:
                todasLasUrl.append(i)
            ## recorro las direcciones para agregarla a las urls administradas
            for t in direccionamiento:
                ## recorro las url y les agrego nuevas url con las direcciones extras
                for i in urls:
                    todasLasUrl.append(i + '/' + t)

            ## retorno todas las urls preparadas
            return todasLasUrl


