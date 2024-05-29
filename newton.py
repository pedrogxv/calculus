def newton(x, y, p_x):
    polinomio = 'd0'

    for i in range(1, len(y)):
        v = ''
        for j in range(i):
            v += f'(x-x{j})'
        polinomio += f'+d{i}{v}'

    diferencas = []

    d = []  # Ds
    d.append(round(float(y[0]), 4))  # O primeiro d é o y0

    for i in range(len(y) - 1):
        r = {'valor': (y[i + 1] - y[i]) / (x[i + 1] - x[i]), 'maximo': x[i + 1], 'minimo': x[i]}
        if i == 0:
            d.append(round(float(r["valor"]), 4))
        diferencas.append(r)
    print(diferencas)

    novas_diferencas = []
    for i in range(len(diferencas) - 1):
        maximo = diferencas[i + 1]['maximo'] if diferencas[i + 1]['maximo'] > diferencas[i]['maximo'] else diferencas[i]['maximo']
        minimo = diferencas[i + 1]['minimo'] if diferencas[i + 1]['minimo'] < diferencas[i]['minimo'] else diferencas[i]['minimo']
        r = {'valor': (diferencas[i + 1]['valor'] - diferencas[i]['valor']) / (maximo - minimo), 'maximo': maximo,
             'minimo': minimo}
        if i == 0:
            d.append(round(float(r["valor"]), 4))
        novas_diferencas.append(r)

    for i in range(len(y)):
        polinomio = polinomio.replace(f'd{i}', f'({d[i]})')

    for i in range(len(x) - 1):
        polinomio = polinomio.replace(f'x{i}', f'({x[i]})')

    p_x = 1 if p_x == '' else p_x

    return {
        'polinomio': polinomio
    }

print(newton([1.4, 1, 1.5], [0.8, 1.8, 2.3], 3.9))