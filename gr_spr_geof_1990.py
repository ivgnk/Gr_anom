"""
Построение диаграммы: как меняется гравитационное поле на профиле
Шар
Гравиразведка. Справочник геофизика (1990).djvu, 256-257 (129),
"""

import numpy as np
from math import pi, sqrt
import matplotlib.pyplot as plt
import inspect

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
    sig=1000 # 1000 кг/м**3 = 1 г/см**3
    r = 100 # метры
    h = 200 # метры
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

def calc_spr(x0, xc, dx, n, sig, r, h, grc):
    """
    Справочник геофизика. Гравиразведка. с.256-257 (129)
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
    m = (4 / 3) * pi * r**3 * sig #   масса шара
    GM=grc*m
    x = x0
    h2=h ** 2
    for k in range(n):
        nt[k]=k
        xt[k]=x
        r=sqrt((x-xc)**2 + h2)
        dg[k]=GM*h/(r**3)
        x=x+dx
    return xt, dg # x координата, аномальное поле

def visu_spr():
    x0, xc, dx, n, sig, r, h, grc = input_data()
    xts, dgs  = calc_spr(x0, xc, dx, n, sig, r, h, grc)
    plt.figure(figsize=(12,8))
    plt.subplot(1, 2, 1)
    plt.title('Справочник геофизика, м/c**2')
    plt.plot(xts, dgs)
    plt.grid()

    plt.subplot(1, 2, 2)
    plt.title('Справочник геофизика, мГал')
    plt.plot(xts, np.array(dgs)*10**5)
    plt.grid(); plt.show()


def visu_sharik():
    x0, xc, dx, n, sig, r, h, grc = input_data()
    xt, dg = calc_sharik(x0, xc, dx, n, sig, r, h, grc)
    plt.figure(figsize=(12,10))
    plt.suptitle('Аномальное поле шара')
    plt.subplot(2, 2, 1)
    plt.title('ini')
    plt.plot(xt, dg)
    plt.grid()

    dg_mgal = np.array(dg) * (10**5)*10000
    plt.subplot(2, 2, 2)
    plt.plot(xt, dg_mgal)
    plt.title('ini coeff')
    plt.grid()

    xts, dgs = calc_spr(x0, xc, dx, n, sig, r, h, grc)
    plt.subplot(2, 2, 3)
    plt.plot(xts, dgs)
    plt.title('spr')
    plt.grid()

    xts, dgs = calc_spr(x0, xc, dx, n, sig, r, h, grc)
    plt.subplot(2, 2, 4)
    plt.plot(xts, np.array(dgs)*(10**6))
    plt.title('spr coeff')
    plt.grid()
    plt.show()

def tst_spec_case():
    """
    Гравиразведка. Справочник геофизика (1990).djvu
    с.258 (130)
    """
    print(f"\nFunction = {inspect.currentframe().f_code.co_name}")  # Вывод имени функции
    grc = 6.67430e-11  # гравитационная постоянная, м^3/(кг·с^2)
    r = 100 # м
    sigma = 1000 # кг/м**3
    M=(4/3)*pi*r*r*r*sigma
    dzeta=200 # м
    res_si=grc*M/dzeta**2
    res_gr=res_si*10**5
    print(f'{res_si=}  {res_gr=}')

def calc_grc():
    """
    Гравитационная разведка Учебник для техникумов_Грушинский (1988).djvu
    стр.6-7 (7-8)
    """
    print(f"\nFunction = {inspect.currentframe().f_code.co_name}")  # Вывод имени функции
    M=6*10**24
    R=6_371_000.0 # м
    g=9.81
    grc=g*R**2/M
    print(f'{grc=}')

if __name__=="__main__":
    # visu_spr()
    tst_spec_case()
    calc_grc()
    # visu_sharik()


