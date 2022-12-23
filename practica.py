lista1 = ['f1ffc0b5efe04e9eb9762cd808722520@sentry.wix', 'lodash@4.17', 'react@16.14', 'dom@16.14',
          'contact@vinosylicores.co']
lista2 = ['.wix', '.co']

total=[]

contenido=lista1
for j in lista2:
    for i in lista1:
        if j in i:
            total.append(i)

# print(total)
# print(lista1.remove(total))
lista_nueva=list(set(lista1).difference(total))
print(lista_nueva)
