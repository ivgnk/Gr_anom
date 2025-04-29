"""
Построение диаграммы: как меняется гравитационное поле [на профиле?] по мере
удаления от шарообразного источника
D:\Genik\My\GUEST\GPP
"""

import numpy as np
from math import pi, sqrt
import matplotlib.pyplot as plt

def input_data():
    """
    x0 - начальная точка х0
    xc - x центра шара
    dx - шаг между точками
    n - число точек расчета
    sig - плотность
    r - радиус шара
    h - глубина центра шара
    g - гравитационная постоянная
    """
    x0=-400 # метры
    xc=0 # метры
    dx=1 # метры
    n=801
    sig=1 #  г/см**3
    r = 10 # метры
    h = 100 # метры
    grc = 6.67430
    return x0, xc, dx, n, sig, r, h, grc

def input_data_si():
    x0=-400 # метры
    xc=0 # метры
    dx=1 # метры
    n=801
    sig=1000 #  кг/м**3
    r = 10 # метры
    h = 100 # метры
    grc = 6.67430e-11  # гравитационная постоянная, м^3/(кг·с^2)
    return x0, xc, dx, n, sig, r, h, grc


def calc_sharik(x0, xc, dx, n, sig, r, h, grc):
    """
    x0 - начальная точка х0
    xc - x центра шара
    dx - шаг между точками
    n - число точек расчета
    sig - плотность
    r - радиус шара
    h - глубина центра шара
    """
    nt=[0]*n
    xt=[0]*n
    dg=[0]*n
    m = 4 / 3 * pi * r * r * r * sig #   масса шара
    x = x0
    h2=h ** 2
    for k in range(n):
        r=sqrt((x-xc)**2 + h2)
        nt[k]=k
        xt[k]=x
        dg[k]=grc*m*h/(r*r*r)
        x=x+dx
    return xt, dg # x координата, аномальное поле

def visu_sharik():
    x0, xc, dx, n, sig, r, h, grc = input_data()
    xt, dg = calc_sharik(x0, xc, dx, n, sig, r, h, grc)
    x0, xc, dx, n, sig, r, h, grc = input_data_si()
    xt_si, dg_si = calc_sharik(x0, xc, dx, n, sig, r, h, grc)

    plt.figure(figsize=(12,5))
    plt.suptitle('Аномальное поле шара')
    plt.subplot(1, 2, 1)
    plt.title('ini')
    plt.plot(xt, dg)
    plt.grid()

    dg_si1=np.array(dg_si)*(10**5)*1000
    plt.subplot(1, 2, 2)
    plt.plot(xt_si, dg_si1)
    plt.title('my')
    plt.grid()
    plt.show()

if __name__=="__main__":
    visu_sharik()
