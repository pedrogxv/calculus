def lagrange(x, points):
    result = 0
    n = len(points)

    for i in range(n):
        term = points[i][1]

        for j in range(n):
            if i != j:
                term *= (x - points[j][0]) / (points[i][0] - points[j][0])
        result += term

    return result

def newton(x, points, coeficients):
    n = len(points)
    result = coeficients[0]
    for i in range(1, n):
        term = coeficients[i]
        for j in range(
                i):
            term *= (
                x - points[j][0]
            )
        result += term
    return result

def diferencas(nos):
    total_nos = len(nos)
    tabela_diferencas = [[0] * total_nos for _ in range(total_nos)]
    
    for linha in range(total_nos):
        tabela_diferencas[linha][0] = nos[linha][1]

    for coluna in range(1, total_nos):
        for linha in range(total_nos - coluna):
            numerador = tabela_diferencas[linha + 1][coluna - 1] - tabela_diferencas[linha][coluna - 1]
            denominador = nos[linha + coluna][0] - nos[linha][0]
            tabela_diferencas[linha][coluna] = numerador / denominador
    
    return [tabela_diferencas[0][coluna] for coluna in range(total_nos)]

ex1 = [(-1, 1), (0, 3), (1, 1), (2, 1)]
ex1_x = 1.5

result_ex_1_diferencas = diferencas(ex1)
result_ex_1_newton = newton(ex1_x, ex1, result_ex_1_diferencas)
result_ex_1_lagrange = lagrange(ex1_x, ex1)

print(f"O valor interpolado utilizando NEWTON no exercicio 1 para x = {ex1_x} é {result_ex_1_newton}.")
print(f"O valor interpolado utilizando LAGRANGE no exercicio 1 para x = {ex1_x} é {result_ex_1_lagrange}.")

ex2 = [(1, 800), (3, 1310), (5, 2090), (7, 2340), (13, 3180)]
ex2_x = 10

result_ex_2_diferencas = diferencas(ex2)
result_ex_2_newton = newton(ex2_x, ex2, result_ex_2_diferencas)
result_ex_2_lagrange = lagrange(ex2_x, ex2)

print(f"O valor interpolado utilizando NEWTON no exercicio 2 para x = {ex2_x} é {result_ex_2_newton}.")
print(f"O valor interpolado utilizando LAGRANGE no exercicio 2 para x = {ex2_x} é {result_ex_2_lagrange}.")

ex3 = [(11, 2.397895), (12, 2.484907), (13, 2.564949), (14, 2.639057), (15, 2.708050)]
ex3_x = 12.3

result_ex_3_diferencas = diferencas(ex3)
result_ex_3_newton = newton(ex3_x, ex3, result_ex_3_diferencas)
result_ex_3_lagrange = lagrange(ex3_x, ex3)

print(f"O valor interpolado utilizando NEWTON no exercicio 3 para x = {ex3_x} é {result_ex_3_newton}.")
print(f"O valor interpolado utilizando LAGRANGE no exercicio 3 para x = {ex3_x} é {result_ex_3_lagrange}.")
