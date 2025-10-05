'''
    determinar si una palabra es capicula, palindromo.
    Una palabra de 1 sola letra, siempre es palindromo
    Una palabra de 2 letras es palindromo unicamente si ambas letras son la misma.
    ejemplo palabras que cumplen: ANA, RECONOCER, B, PP
'''

def palindromo(palabra):
    inicio = 0
    fin = len(palabra) - 1

    # caso base palabra vacia
    if fin < 0:
        print("la palabra esta vacia, no puede ser palindromo")
        return 
    
    # caso base palabra de solo 1 letra
    if fin == 0:
        print(f"La palabra {palabra} es palindromo")
        return 
    
    resolver_palindromo(palabra, inicio, fin)

def resolver_palindromo(palabra, inicio, fin):
    # caso base, inicio y fin son iguales, o  inicio > fin (para las palabras de 2 letras por ejemplo)
    if inicio >= fin:
        print(f"La palabra {palabra} es palindroma")
        return
    # caso 
    if palabra[inicio] == palabra[fin]:
        # analizo la siguiente letra y la anterior a la ultima analizada
        resolver_palindromo(palabra, inicio+1, fin-1)
    else:
        print(f"La palabra {palabra} no es palindroma")
        return

palabra = "ANA"
palindromo(palabra)