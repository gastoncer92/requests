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
    for j in direccionamiento:
        if j == '':
            respuesta = requests.get(url)
        else:
            print(url + '/' + j)
            respuesta = requests.get(url + '/' + j)
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


# extraer_correo(url4, excluir=["wix"])
# extraer_correo(url4, excluir=['wix'])
