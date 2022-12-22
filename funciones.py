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


def extraer_correo3(url, direccionamiento=[], excluir=[]):
    registro = []
    if direccionamiento == '':
        respuesta = requests.get(url)
    else:
        for j in direccionamiento:
            respuesta = requests.get(url + '\\' + j)
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
    correos = []
    # ver si direccionamiento y exluir tienen contenido
    if direccionamiento != [''] and excluir != ['']:
        ## tienen ambos contenido

        ## prepraro una lista vacia en la que iran todos los correos
        todasLasUrl = []

        ## meto en la lista todasLasUrl las url originales
        for i in urls:
            todasLasUrl.append(i)
        ## reorro las direcciones para agregarla a las urls administradas
        for t in direccionamiento:
            ## recorro las url y les agrego nuevas url con las direcciones extras
            for i in urls:
                todasLasUrl.append(i + '/' + t)
        print(todasLasUrl)
    else:
        pass

        """
        ## recorro la lista de urls administrada
        for i in urls:
            ## Ver si existe la url administrada
            if existeUrl(i):
                ## determino si en la url esta adentro algunas de las excepciones
                ## si es verdadero no hago nada, si es falso lo agrego a una lista nueva
                if excluir not in i:
                    ## si no esta dentro la agrego a la lista de correos
                    correos.append(i)
                else:
                    ## sino paso
                    pass
                ## recorro la lista de direcciones
                for j in direccionamiento: # ['contact']
                    url=i+'\'j
            else:
                pass
"""

        ## agrego a la url la direccion
        ## determino si en la url esta adentro algunas de las excepciones
        ## si es verdadero no hago nada, si es falso lo agrego a una lista nueva

        # for i in urls:
        #     respuesta = hay_direccionamiento_y_excluir(i, direccionamiento, excluir, patron)
        #     print("----------------------------")
        #     print(respuesta)
        #     print("----------------------------")
        #     return respuesta

    # ver si direccionamiento o exluir estan vacios
    # elif direccionamiento == [''] and excluir == ['']:
    #     print("no hay direccionamiento ni excluir!")

    # direccionamiento y exluir estan vacios
    # else:
    #     print("no hay direccionamiento o no hay excluir!!")
    #     if direccionamiento == ['']:
    #         print("no hay direccionamiento")
    #     else:
    #         print("no hay excluir")


def extraer_correo4(urls=[''], direccionamiento=[''], excluir=[''], patron=r'[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}'):
    # print("url:{}\nredireccionamiento: {}\nexcluir: {}".format(url, direccionamiento, excluir))

    if direccionamiento != [''] and excluir != ['']:
        print("hay direccionamiento y hay excluir")
        for i in urls:
            respuesta = hay_direccionamiento_y_excluir(i, direccionamiento, excluir, patron)
            print("----------------------------")
            print(respuesta)
            print("----------------------------")
            return respuesta


    elif direccionamiento == [''] and excluir == ['']:
        print("no hay direccionamiento ni excluir!")

    else:
        print("no hay direccionamiento o no hay excluir!!")
        if direccionamiento == ['']:
            print("no hay direccionamiento")
        else:
            print("no hay excluir")


def hay_direccionamiento_y_excluir(url, direc, exclu, patron):
    registro = []
    for j in direc:
        respuesta = requests.get(url + '/' + j)
        if '200' in str(respuesta):
            print("es correcto")
            extracto = re.findall(patron, respuesta.text)
            for index, i in enumerate(extracto):
                for exc in exclu:
                    if exc in i:
                        print("{} tiene {}".format(i, exc))
                    else:
                        print("{} no tiene {}".format(i, exc))
                        registro.append(i)

            return registro
        else:
            print("presenta error")
            return None
