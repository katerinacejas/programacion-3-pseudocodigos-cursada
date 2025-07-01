'''
encontrar la forma de devolver un vuelto de valor v con monedas de denominaciones 
d1, d2, ..., dn con una cantidad infinita de monedas de cada denominaci´on. 
Por ejemplo, queremos devolver $1.83 y disponemos de monedas de 
1, 5, 10, 25, 50 centavos y 1 peso. La forma mas sencilla e intuitiva de hacerlo 
es una moneda de 1 peso, una moneda de 50 centavos, una moneda de 25 centavos, 
una moneda de 5 centavos y tres monedas de 1 centavo.

Se busca minimizar la cantidad de monedas utilizadas para pagar. 
'''

# asumo que recibo el listado de monedas ordenadas de mayor a menor
# conjunto de candidatos: la lista de monedas
# funcion seleccion: la moneda mas grande
# funcion de factibilidad: si al sumar la moneda no se supera el monto_a_pagar
# objetivo: minimizar la cantidad de monedas
def problema_cambio(monto_a_pagar, monedas):
    solucion = []
    sumatoria = 0
    indice_moneda = 0
    
    while sumatoria < monto_a_pagar and indice_moneda < len(monedas):
        if sumatoria + monedas[indice_moneda] <= monto_a_pagar:
            sumatoria = sumatoria + monedas[indice_moneda]
            solucion.append(monedas[indice_moneda])
        else:
            indice_moneda = indice_moneda + 1
    
    if sumatoria == monto_a_pagar:
        print("hay solucion")
        print(f"las monedas a utilizar listadas son: {solucion}")
        return
    print("no hay solucion")

monto_a_pagar = 10
monedas = [11, 6, 2, 1]
problema_cambio(monto_a_pagar, monedas)