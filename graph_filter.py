import numpy as np
import scipy.signal
import pandas as pd
import matplotlib.pyplot as plt
import feature_quantity as fq


#2525が一つのとき
#data = pd.read_csv("/Users/ren/Desktop/sleep_2ndtime/sleep_test3.csv", names=('sec', 'lq'))
# data2 = pd.read_csv("/Users/ren/Desktop/three_top_right3.csv", names=('sec', 'lq', 'ba', 'x', 'y', 'z'))
# data3 = pd.read_csv("/Users/ren/Desktop/three_top_left3.csv", names=('sec', 'lq', 'ba', 'x', 'y', 'z'))
# print(data)

#def lpf(data, plt):


data = pd.read_csv("/Users/ren/Desktop/sleep_20180831.csv", names=('sec', 'lq', 'ba', 'x', 'y', 'z'))
#plt.plot(range(0, len(data)), data['lq'])
data_np = np.asarray(data["y"])
#print(data["z"])
data2 = []
data3 = []
filter_output = 0
num = len(data_np)
print(num)
n = 0
#for i in range(0, num, 10):
#   data2.append(data_np[i:i+10])
#for j in range(len(data2)):
#   data3.append(fq.calc_variance(data2[j]))
#for k in range(len(data_np)):
    #a = 0.9
    #ローパスフィルタ
    #lowpass_value=round(a * filter_output + (1-a) * data_np[k], 2)
    #重力加速度成分除去(ハイパスフィルタ)
    #highpass_value=data_np[i]-lowpass_value
#    data2.append(data_np[i])
#    data2.append(lowpass_value)
    #filter_output = data2[i]
  #  if i == 9:
  #      data3.append(fq.calc_mean(data2))
data2 = fq.calc_maverage(data_np)
print(data2)
plt.plot(range(0, len(data2)), data2)
#plt.plot(range(0, len(data)),data['z'])
plt.xlabel('sec/5(s)')
plt.ylabel('acceleration(m/s^2')
plt.xlim([0, 1000])
#plt.ylim([0, 5])
plt.legend()
plt.show()




#data2 = pd.DataFrame(data_np)
#lpf(data, plt)

# #2525が３つのとき
# data = pd.read_csv("/Users/ren/Desktop/sleep_2ndtime/left3.csv", names=('sec', 'x', 'y', 'z'))
# print(data)
# plt.plot(range(0, len(data)),data['x'])
# plt.plot(range(0, len(data)),data['y'])
# plt.plot(range(0, len(data)),data['z'])
# plt.xlabel('sec/10(s)')
# plt.ylabel('acceleration(m/s^2)')
# plt.legend()
# plt.show()
# print(data)

