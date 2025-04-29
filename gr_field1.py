"""
https://heybro.ai
расчет гравитационного поля внутри и снаружи шара:
"""
import numpy as np
import matplotlib.pyplot as plt
import inspect
from greek_symbols import up_gr_symb

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
    """
    Вычисление гравитационного поля при задании центра шара (center) и
    точки вычисления (point) с помощью координат
    """
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



# Примеры работы с классами в Python
nxi = 2001  # число значений по x
nyi = 2001  # число значений по y
centeri=(0, 0, 0) # центр шара, метры
xmini = -1000 # миним по Х, метры
xmaxi = 1000 # максим по Х, метры
ymini = 10 # миним по Y, метры
ymaxi = 2000 # максим по Y, метры

# https://pythonru.com/primery/primery-raboty-s-klassami-v-python
class Grav_sphere():
    """
    Построение диаграммы: как меняется гравитационное поле на профиле по мере
    удаления от шарообразного источника
    """
    sphere_count:int = 0
    Calced: bool = False
    name='Гравитационное поле шара при разных удалениях'

    def __init__(self, nx=nxi, ny=nyi, center=centeri,
                 xmin=xmini, xmax=xmaxi,
                 ymin=ymini, ymax=ymaxi):
        """
        Инициализация объекта
        """
        print(f"\nFunction = {inspect.currentframe().f_code.co_name}")  # Вывод имени функции
        self.nx = nx
        self.ny = ny
        self.center=center
        self.xmin = xmin
        self.xmax = xmax
        self.ymin = ymin
        self.ymax = ymax
        self.F = None
        Grav_sphere.sphere_count += 1
        Grav_sphere.Calced = False

    def print_ini_param(self):
        """
        Проверочный вывод для __init__
        """
        print(f"\nFunction = {inspect.currentframe().f_code.co_name}")  # Вывод имени функции
        print(f'{self.nx=}')
        print(f'{self.ny=}')
        print(f'{self.center=}')
        print(f'{self.xmin=}')
        print(f'{self.xmax=}')
        print(f'{self.ymin=}')
        print(f'{self.ymax=}')
        print(f'{Grav_sphere.sphere_count=}')

    def make_coo(self):
        """
        Задание координат для расчетов
        """
        print(f"\nFunction = {inspect.currentframe().f_code.co_name}")  # Вывод имени функции
        zer=np.zeros(self.nx)
        ons=np.ones(self.nx)
        self.x = np.linspace(self.xmin, self.xmax, self.nx) # х-координаты
        self.y = np.linspace(self.ymin, self.ymax, self.ny) # сдвиг по y-координате
        self.res=np.column_stack([self.x,ons, zer])
        self.xn, self.yn = np.meshgrid(self.x, self.y)
        Grav_sphere.Calced = True

    def calc_fld(self):
        """
        Непосредственно расчет гравитационного поля шара
        на основе gravity_field_vector(center, point)
        """
        self.F = np.empty_like(self.xn)
        print(f"\nFunction = {inspect.currentframe().f_code.co_name}")  # Вывод имени функции
        for i in range(self.xn.shape[0]):
            for j in range(self.xn.shape[1]):
                # тест - диагональные полосы
                # self.F[i, j] = self.xn[i, j] + self.yn[i, j]
                pass
        # gravity_field_vector(center, point):

    def cntrl_calc(self):
        """
        Перед визуализацией контроль вычисления
        """
        if not Grav_sphere.Calced or self.F is None: self.calc_fld()

    def visu_fld(self):
        """
        Визуализация рассчитанного гравитационного поля шара
        """
        print(f"\nFunction = {inspect.currentframe().f_code.co_name}")  # Вывод имени функции
        self.cntrl_calc()

        n_iso = 15  # num isolines
        fig =plt.figure(figsize=(10,8))
        curves1 = plt.contourf(self.xn, self.yn, self.F, n_iso)
        curves3 = plt.contour(self.xn, self.yn, self.F, n_iso, colors='k')

        cbar=plt.colorbar(curves1)
        cbar.ax.set_title(up_gr_symb[3]+'G,\nмГал') # ,fontsize=8

        plt.xlabel('X, м'); plt.ylabel('У, м')
        plt.title(Grav_sphere.name)
        plt.show()

if __name__=="__main__":
    # tst_gravity_field()
    # tst_gravity_field_vector()
    # big_tst()
    gr1=Grav_sphere()
    gr1.print_ini_param()
    gr1.make_coo()
    gr1.visu_fld()
