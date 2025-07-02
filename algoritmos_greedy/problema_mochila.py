'''
Se busca maximizar el valor que se puede llevar en una mochila con objetos de 
distintos pesos. 
Este caso busca la manera de llenar una mochila que puede cargar un peso “p” con 
objetos que tienen un cierto peso, y un cierto valor. El objetivo es lograr que 
la mochila lleve la mayor cantidad de valor posible. Entonces, lo que quiero 
optimizar es el valor que hay en la mochila. 
Un detalle importante es que los objetos se pueden fraccionar.
Por lo general, este tipo de ejercicios te dicen que tengo un limite de espacio 
o peso disponible (“P”, que es el peso que carga la mochila) que tengo que llenar
con objetos cosa de maximizar el beneficio que me den esos objetos 
(La relación valor/peso de los objetos)
'''
class Objeto:
    def __init__(self, peso, valor):
        self.peso = peso
        self.valor = valor
        self.proporcion = None
        #cuando se crea el objeto, se le setea la relacion
        self.relacion = valor / peso

def problema_mochila(peso_maximo, objetos):
    # ordeno los objetos por la relacion de mayor a menor
    objetos.sort(key=lambda obj:obj.relacion , reverse=True)
    mochila = []
    peso_acumulado = 0
    indice_objeto = 0

    while peso_acumulado < peso_maximo and indice_objeto < len(objetos):
        if peso_acumulado + objetos[indice_objeto].peso <= peso_maximo:
            peso_acumulado = peso_acumulado + objetos[indice_objeto].peso
            # seteo la proporcion en 1 porque el objeto entra entero en la mochila
            objetos[indice_objeto].proporcion = 1
            mochila.append(objetos[indice_objeto])
        elif peso_acumulado < peso_maximo:
            # el objeto no entra entero en la mochila, por lo tanto la proporcion es la partecita del objeto que entro en la mochila
            objetos[indice_objeto].proporcion = (peso_maximo - peso_acumulado) / objetos[indice_objeto].peso
            peso_acumulado = peso_acumulado + (peso_maximo - peso_acumulado)
            mochila.append(objetos[indice_objeto])
        # luego aumento el indice para ver el objeto siguiente
        indice_objeto = indice_objeto + 1
    
    if peso_acumulado == peso_maximo:
        imprimir_mochila(mochila)
        return
    print("no hay solucion")

def imprimir_mochila(mochila):
    for objeto in mochila:
        print(f"peso: {objeto.peso}, valor: {objeto.valor}, proporcion: {objeto.proporcion}")

objetos = [
    Objeto(1, 330),
    Objeto(8, 80),
    Objeto(13, 100)
]

problema_mochila(2, objetos)