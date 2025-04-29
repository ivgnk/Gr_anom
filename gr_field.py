"""
https://heybro.ai
расчет гравитационного поля внутри и снаружи шара:
"""
import sys

import numpy as np
import matplotlib.pyplot as plt
import inspect
from pgreek_symbols import up_gr_symb

# Константы
G = 6.67430e-11  # гравитационная постоянная, м^3/(кг·с^2)
M = 5.972e24     # масса Земли, кг
R = 6_371_000      # радиус Земли, м
GM=G*M
R3=R**3

nxi = 101  # число значений по x
nyi = 51  # число значений по y
centeri=(0, 0, -100) # центр шара, метры
xmini = -1000 # миним по Х, метры
xmaxi = 1000 # максим по Х, метры
ymini = 50 # миним по Y, метры
ymaxi = 2550 # максим по Y, метры

"""
Для вычисления гравитационного поля g(r):
Внутри шара (радиус r≤R):
g(r)=GM(r)/r**2
 
где M(r) — масса внутри радиуса r:
M(r)=M(r**3/R**3)
 
Снаружи шара (радиус r≥R):
g(r)=GM/r**2
"""

def gravity_field(r):
    if r <= R:
        # Внутри шара
        if r<1e-5:
            g = 0
        else:
            M_r = M * (r / R)**3
            g = G * M_r / r**2
    else:
        # Снаружи шара
        g = G * M / r**2
    return g

def gravity_field2(r):
    if r <= R:
        # Внутри шара
        if r<1e-5:
            g = 0
        else:
            # M_r = M * (r / R)**3
            # g = G * M_r / r**2
           g = GM*r/R3
    else:
        # Снаружи шара
        g = GM / r**2
    return g


def tst_gravity_field():
    # Пример использования
    distance = 10_000_000 #e7  # расстояние от центра, м
    g_value = gravity_field(distance)
    print(f"Гравитационное поле на расстоянии {distance} м от центра Земли: {g_value} м/с^2")
    g_value = gravity_field2(distance)
    print(f"Гравитационное поле на расстоянии {distance} м от центра Земли: {g_value} м/с^2")
    #-------------------
    radius=np.arange(0,distance,1000)
    dg=np.empty_like(radius)
    for i, radi in enumerate(radius):
        print(i, radi)
        dg_=gravity_field2(radi)
        print(dg_)
        dg[i]=dg_
    # dg = [gravity_field(r) for r in radius]
    # перевод в км
    rad_km=radius/1000
    plt.plot(rad_km, dg)
    plt.xlabel('Расстояние от центра Земли, км')
    plt.grid();  plt.show()




if __name__=="__main__":
    # tst_gravity_field()
    tst_gravity_field()

