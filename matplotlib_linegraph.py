import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#2525が一つのとき
# data = pd.read_csv("/Users/ren/Desktop/sleep_test.csv", names=('sec', 'x', 'y', 'z'))
# print(data)
# plt.plot(range(0, 512),data['x'])
# plt.plot(range(0, 512),data['y'])
# plt.plot(range(0, 512),data['z'])
# plt.xlabel('sec/10(s)')
# plt.ylabel('acceleration(m/s^2)')
# plt.legend()
# plt.show()
# print(data)

#2525が３つのとき
data = pd.read_csv("/Users/ren/Desktop/left.csv", names=('sec', 'x', 'y', 'z'))
print(data)
plt.plot(range(0, 381),data['x'])
plt.plot(range(0, 381),data['y'])
plt.plot(range(0, 381),data['z'])
plt.xlabel('sec/10(s)')
plt.ylabel('acceleration(m/s^2)')
plt.legend()
plt.show()
print(data)
