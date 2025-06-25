def branch_bound(raiz):
    env = inicializar_estructura_nodos_vivos()
    env.add(raiz)

    cota = inicializar_cota(raiz)

    mejor_solucion = None

    while env != None:
        nodo = env.pop()
        if no_se_puede_podar(nodo, cota):
            for hijo in generar_hijos(nodo):
                if no_se_puede_podar(hijo, cota):
                    if es_solucion(hijo) and es_mejor_solucion(mejor_solucion, hijo):
                        mejor_solucion = hijo
                    else:
                        env.add(hijo)
                    actualizar_cota(cota, hijo)
                    
    return mejor_solucion                