# Desenvolvido em Python 3

import matplotlib.pyplot as plt



# Estima a derivada da função no ponto
def numeric_derivative(func, middle, delta = 0.00001): 
    return (func(middle+delta)-func(middle))/delta


# Encontra o máximo de uma função côncava (método da bisseção)
def biss(func, x_min, x_max, epsilon = 0.0001):
    while(abs(x_min-x_max) < epsilon):
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



'''
def show_changing(p, q, m, alpha = 0.5):
    price_changing = [solve_utility_max(m*i/1000, q, m, alpha) for i in range(1, 1000)] # Preço variando com 999 pontos
    plt.plot(price_changing)
    plt.show()
'''

    







    








