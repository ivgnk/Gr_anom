"""
https://heybro.ai
расчет гравитационного поля внутри и снаружи шара:
"""
import numpy as np

# Константы
G = 6.67430e-11  # гравитационная постоянная, м^3/(кг·с^2)
M = 5.972e24     # масса Земли, кг
R = 6.371e6      # радиус Земли, м

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
        M_r = M * (r / R)**3
        g = G * M_r / r**2
    else:
        # Снаружи шара
        g = G * M / r**2
    return g

def tst_gravity_field():
    # Пример использования
    distance = 1e7  # расстояние от центра, м
    g_value = gravity_field(distance)
    print(f"Гравитационное поле на расстоянии {distance} м: {g_value} м/с^2")


def gravity_field_vector(center, point):
    x0, y0, z0 = center
    x1, y1, z1 = point

    # Вычисляем вектор от центра шара к точке
    r_vec = np.array([x1 - x0, y1 - y0, z1 - z0])
    r = np.linalg.norm(r_vec)

    if r == 0:
        # Точка совпадает с центром шара
        return np.array([0.0, 0.0, 0.0])

    # Вычисляем массу внутри радиуса r
    if r <= R:
        M_r = M * (r / R) ** 3
        g_scalar = G * M_r / r ** 2
    else:
        g_scalar = G * M / r ** 2

    # Векторное гравитационное поле
    g_vector = -g_scalar * (r_vec / r)
    return g_vector

def tst_gravity_field_vector():
    # Пример использования
    center = (0, 0, 0)
    point = (1e7, 0, 0)  # точка на оси x на расстоянии 10 000 км от центра
    g_field = gravity_field_vector(center, point)
    print(f"Гравитационное поле в точке {point}: {g_field} м/с^2")

if __name__=="__main__":
    tst_gravity_field()
    tst_gravity_field_vector()