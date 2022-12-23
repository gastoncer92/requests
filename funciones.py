import re

import requests

url4 = 'https://www.vinosylicores.co.uk'  # /contact
patron1 = r'[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}'

def existeUrl(url):
    if '200' in str(requests.get(url)):
        return True
    else:
        return False
def ListaDeCorreos(urls=[''], direccionamiento=['']):
    """
    Retorna una lista de correos extridos de la lista de urls administrada

    :param urls: list
    :param direccionamiento: list
    :return: list
    """
    ## preparo una lista vacía en la que iran todos los correos
    todasLasUrl = []
    # ver si direccionamiento y excluir tienen contenido
    for i in urls:
        todasLasUrl.append(i)
    if direccionamiento != ['']:
        for t in direccionamiento:
            ## recorro las url y les agrego nuevas url con las direcciones extras
            for i in urls:
                todasLasUrl.append(i + '/' + t)
    else:
        pass
    return todasLasUrl
def extraer_correos_unicos(lista_de_urls, patron):  # lista_de_urls,patron
    # registroReverso = []
    lista_de_correos = []
    lista_unica_de_correos = []
    for i in lista_de_urls:
        response = requests.get(i)
        if existeUrl(i):
            extraido = re.findall(patron, response.text)
            for j in extraido:
                if j not in lista_unica_de_correos:
                    lista_unica_de_correos.append(j)
                # else:
                #     pass
                # lista_de_correos.append(j)
        # else:
        #     pass
    return lista_unica_de_correos
def LimpiarExcluidos(lista_de_correos: list, lista_a_excluir: list):
    total = []

    for j in lista_a_excluir:
        for i in lista_de_correos:
            if j in i:
                total.append(i)
    lista_nueva = list(set(lista_de_correos).difference(set(total)))
    return lista_nueva