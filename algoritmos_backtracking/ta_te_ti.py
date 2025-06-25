def ta_te_ti(estado, nivel, alfa, beta):
    if es_hoja(estado, nivel):
        return resultado(estado, nivel)
    
    if nivel == MAX:
        valor = -infinito
    else: valor = +infinito

    for hoja in hojas(estado):
        if nivel == MAX:
            valor = max(valor, ta_te_ti(hoja, MIN, alfa, beta))
            alfa = max(alfa, valor)
        elif nivel == MIN:
            valor = min(valor, ta_te_ti(hoja, MAX, alfa, beta))
            beta = min(beta, valor)
        if alfa >= beta:
            break
    return valor