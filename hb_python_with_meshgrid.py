"""
Расчет для сетки полученной numpy.meshgrid поэлементно, а не векторным способом
The calculation for the grid obtained by numpy.meshgrid is piecemeal, not vector-based
"""
import numpy as np
import matplotlib.pyplot as plt

lst=list(range(2001))
# Создаем сетку
x = np.array(lst)
y = np.array(lst)
X, Y = np.meshgrid(x, y)

# Создаем массив для результатов
F = np.empty_like(X)

# Проходим по всем элементам поэлементно
for i in range(X.shape[0]):
    for j in range(X.shape[1]):
        # Выполняем нужную операцию с X[i, j] и Y[i, j]
        F[i, j] = X[i, j] + Y[i, j]  # пример: сложение элементов

print(F)

n_iso = 15 # num isolines
fig =plt.figure(figsize=(10,8))
curves1 = plt.contourf(X, Y, F, n_iso)
curves3 = plt.contour(X, Y, F, n_iso, colors='k')

fig.colorbar(curves1)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('My function')
plt.show()
