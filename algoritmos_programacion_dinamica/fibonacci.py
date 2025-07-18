def resolver_fibonacci(nro):
    # creo el conjunto solucion donde se guardan las soluciones parciales
    fibonacci = []
    
    # caso base, fibonacci de 0 o 1
    if nro <= 1:
        return nro
    
    else:
        for i in range(nro+1):
            if i <= 1:
                fibonacci.append(i)
            else:
                fibonacci.append(fibonacci[i-1] + fibonacci[i-2])
        
        #como ya sali del for, devuelvo el fibo q ya se guardo en las soluciones parciales
        return fibonacci[nro]
    
print(resolver_fibonacci(0))
print(resolver_fibonacci(1))
print(resolver_fibonacci(2))
print(resolver_fibonacci(3))
print(resolver_fibonacci(4))
print(resolver_fibonacci(5))
print(resolver_fibonacci(6))