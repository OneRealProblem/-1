import math
import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return np.sin(2*x)


print("Число точек разбиения:")
tr = int(input())
print("Способ выбора оснащения:")
print("1 - левые")
print("2 - средние")
print("3 - правые")
svo = int(input())

a = 0
b = np.pi
x = np.arange(a, b, 0.01)

xk = []
seredina = []
yk = []
dlina = (b-a)/tr #длина одного отрезка
summ = 0

if svo == 1:
    othod = -0.5*dlina #возвращаемся к левому краю
    m = "левые"
elif svo == 3:
    othod = 0.5*dlina #идём вперёд к правому краю
    m = "правые"
else:
    othod = 0
    m = "средние"

for i in range(0,tr):
    xk.append(a+i*dlina)
    seredina.append(a + (i + 0.5)*dlina) #середины отрезков
xk.append(b) #точек разбиения больше, чем отрезков

for i in seredina:
    yk.append(f(i + othod))
    summ +=f(i+othod)
    
summ *= dlina #вынесли длину отрезков за знак суммы для меньших потерь при вычислениях

plt.plot(x, f(x),'r')
plt.bar(seredina, yk, width = dlina,edgecolor="k")
plt.xlabel(r'$x$')
plt.ylabel(r'$f(x)$')
plt.title("Точек разбиения: " + str(tr) + ". Оснащение: " + m + ". I = " + str((summ)),fontsize=10 )
plt.grid(True)
plt.savefig("tr"+str(tr)+"svo"+str(svo)+".png")
plt.show()
