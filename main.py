import time as time
import numpy as np
import random
import math
import matplotlib.pyplot as plt


# Task 1
def create_array():
    return [(random.randint(1, 1000)) for i in range(10**6)]


def compare(a, b):

    # Python algorithm
    array_res = []
    start_time = time.perf_counter()
    for i in range(10**6):
        array_res.append(a[i] * b[i])
    total_time_py = time.perf_counter() - start_time

    # NumPy algorithm
    start_time = time.perf_counter()
    array_res = np.multiply(a, b)
    total_time_np = time.perf_counter() - start_time

    print(f'Python time: {total_time_py}\nNumPy time: {total_time_np}')
    print(f"NumPy's performance was {100 - math.floor(total_time_np/total_time_py*100)}% faster")


array_one = create_array()
array_two = create_array()
compare(array_one, array_two)


# Task 2
consumption_arr = []
time_arr = []
position_arr = []

with open('data1.csv', 'r') as f:
    for line in f:
        res = line.split(';')
        time_arr.append(res[0])
        position_arr.append(res[3])
        consumption_arr.append(res[15])
    f.close()

for arr in (time_arr, position_arr, consumption_arr):
    arr.pop(0)

time = np.array(time_arr, float)
consumption = np.array(consumption_arr, float)
position = np.array(position_arr, float)

plt.title('Положение дросселя и расход воздуха в течении времени')
plt.xlabel('Время')
plt.ylabel(f'Положение дросселя и расход воздуха (кг/ч)')
plt.plot(np.array(time), np.array(position))
plt.plot(np.array(time), np.array(consumption))
plt.show()

plt.title('График корреляции')
plt.xlabel('Положение дросселя')
plt.ylabel('Расход воздуха (кг/ч)')
plt.plot(position, consumption, 'o')
plt.show()


# Task 3
x = np.linspace(np.pi*(-1), np.pi, 100)

y = np.zeros(len(x), float)
for i in range(len(x)):
    y[i] = math.sin(x[i]) * math.cos(x[i])

z = np.zeros(len(x), float)
for i in range(len(x)):
    z[i] = math.sin(x[i])

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.plot(x, y, z)
plt.show()
