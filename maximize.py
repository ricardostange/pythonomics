# Desenvolvido em Python 3

import matplotlib.pyplot as plt



# Estima a derivada da função no ponto
def numeric_derivative(func, middle, delta = 10**-6): 
    return (func(middle+delta)-func(middle-delta))/(2*delta)


# Encontra o máximo de uma função côncava (método da bisseção)
def biss(func, x_min, x_max, epsilon = 10**(-10)):
    while(abs(x_min-x_max) > epsilon):
        middle = (x_min + x_max)/2
        d = numeric_derivative(func, middle)
        if(d < 0):
            x_max = middle
        else:
            x_min = middle
    return (x_min+x_max)/2

def utility(x, y, alpha = 0.5):
    assert x >= 0 and y >= 0
    return (x**alpha)*(y**(1-alpha))

def transform_utility(p, q, m, alpha = 0.5): # Retorna uma função utilidade que depende somente de x
    return lambda x : utility(x, (m-p*x)/q, alpha)



def solve_utility_max(p, q, m, alpha = 0.5):
    assert p != 0 and q != 0
    util = transform_utility(p, q, m, alpha) # util se torna uma função de uma variável
    x_min = 0
    x_max = m/p

    x = biss(util, x_min, x_max)

    y = (m-p*x)/q
    return (x, y)

def algebraic_solve(p, q, m, alpha = 0.5):
    return (alpha*m/p, (1-alpha)*m/q)


# Calcula e imprime exemplo, e compara com solução algébrica para determinar o erro
def solve_and_print(p, q, m, alpha = 0.5):
    (x, y) = solve_utility_max(p, q, m, alpha)
    print('px = ' + str(p) + ' py = ' + str(q) + ' m = ' + str(m) + ' a = ' + str(alpha) + '  => (x*, y*) = ' + str((round(x, 5),round(y, 5))))
    (xa, ya) = algebraic_solve(p, q, m, alpha)
    print('Erro médio: ' + str((abs(xa-x)+ abs(ya-y))/2))
def test():
    solve_and_print(1, 1, 10)
    solve_and_print(3, 4, 10, 0.6)
    

test()
