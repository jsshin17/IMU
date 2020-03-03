import pandas as pd
from matplotlib import pyplot as plt

filename = []
csv_file = []
sensor0 = []
sensor1 = []
sensor2 = []
sensor3 = []
point = []
num = int(input("Enter the number of csv files(n>1) : "))
for i in range(num):
    temp_name = input("Enter the csv file name : ")
    filename.append(temp_name)
    temp_file = pd.read_csv("C:\\Users\\Shin Jisu\\Desktop\\"+filename[i], names=['num', 'time', 'sensor', 'AccelX', 'AccelY', 'AccelZ', 'GyroX', 'GyroY', 'GyroZ', 'MagX', 'MagY', 'MagZ'])
    csv_file.append(temp_file)
    sensor0.insert(i, csv_file[i][csv_file[i].sensor == '100-0'])
    sensor1.insert(i, csv_file[i][csv_file[i].sensor == '100-1'])
    sensor2.insert(i, csv_file[i][csv_file[i].sensor == '100-2'])
    sensor3.insert(i, csv_file[i][csv_file[i].sensor == '100-3'])
    temp_point = csv_file[i][csv_file[i].num == 0]
    point.append(temp_point.index)

fig0, axes0 = plt.subplots(num, 3, figsize=(14, 2*num))
for i in range(num):
    axes0[i, 0].plot(sensor0[i][['AccelX']], 'y-', Label='AccelX') #이 부분에서 기존에는 axes0[0].plot 과 같은식으로 하였으나 여러 파일을 받아 그래프를 그릴때 오류가 생겨 이와 같은 식으로 바꿈. 대신 파일을 한개만 받을때는 오류가 뜸.
    axes0[i, 0].plot(sensor0[i][['AccelY']], 'g-', Label='AccelY')
    axes0[i, 0].plot(sensor0[i][['AccelZ']], 'b-', Label='AccelZ')
    axes0[i, 0].legend(loc='upper left')
    for j in range(len(point[i])):
        axes0[i, 0].axvline(x=point[i][j], color= 'r', linestyle = '-', linewidth = 2)
    axes0[i, 1].plot(sensor0[i][['GyroX']], 'y-', Label='GyroX')
    axes0[i, 1].plot(sensor0[i][['GyroY']], 'g-', Label='GyroY')
    axes0[i, 1].plot(sensor0[i][['GyroZ']], 'b-', Label='GyroZ')
    axes0[i, 1].legend(loc='upper left')
    for j in range(len(point[i])):
        axes0[i, 1].axvline(x=point[i][j], color= 'r', linestyle = '-', linewidth = 2)
    axes0[i, 2].plot(sensor0[i][['MagX']], 'y-', Label='MagX')
    axes0[i, 2].plot(sensor0[i][['MagY']], 'g-', Label='MagY')
    axes0[i, 2].plot(sensor0[i][['MagZ']], 'b-', Label='MagZ')
    axes0[i, 2].legend(loc='upper left')
    for j in range(len(point[i])):
        axes0[i, 2].axvline(x=point[i][j], color= 'r', linestyle = '-', linewidth = 2)

fig1, axes1 = plt.subplots(num, 3, figsize=(14, 2*num))
for i in range(num):
    axes1[i, 0].plot(sensor1[i][['AccelX']], 'y-', Label='AccelX')
    axes1[i, 0].plot(sensor1[i][['AccelY']], 'g-', Label='AccelY')
    axes1[i, 0].plot(sensor1[i][['AccelZ']], 'b-', Label='AccelZ')
    axes1[i, 0].legend(loc='upper left')
    for j in range(len(point[i])):
        axes1[i, 0].axvline(x=point[i][j], color= 'r', linestyle = '-', linewidth = 2)
    axes1[i, 1].plot(sensor1[i][['GyroX']], 'y-', Label='GyroX')
    axes1[i, 1].plot(sensor1[i][['GyroY']], 'g-', Label='GyroY')
    axes1[i, 1].plot(sensor1[i][['GyroZ']], 'b-', Label='GyroZ')
    axes1[i, 1].legend(loc='upper left')
    for j in range(len(point[i])):
        axes1[i, 1].axvline(x=point[i][j], color= 'r', linestyle = '-', linewidth = 2)
    axes1[i, 2].plot(sensor1[i][['MagX']], 'y-', Label='MagX')
    axes1[i, 2].plot(sensor1[i][['MagY']], 'g-', Label='MagY')
    axes1[i, 2].plot(sensor1[i][['MagZ']], 'b-', Label='MagZ')
    axes1[i, 2].legend(loc='upper left')
    for j in range(len(point[i])):
        axes1[i, 2].axvline(x=point[i][j], color= 'r', linestyle = '-', linewidth = 2)

fig2, axes2 = plt.subplots(num, 3, figsize=(14, 2*num))
for i in range(num):
    axes2[i, 0].plot(sensor2[i][['AccelX']], 'y-', Label='AccelX')
    axes2[i, 0].plot(sensor2[i][['AccelY']], 'g-', Label='AccelY')
    axes2[i, 0].plot(sensor2[i][['AccelZ']], 'b-', Label='AccelZ')
    axes2[i, 0].legend(loc='upper left')
    for j in range(len(point[i])):
        axes2[i, 0].axvline(x=point[i][j], color= 'r', linestyle = '-', linewidth = 2)
    axes2[i, 1].plot(sensor2[i][['GyroX']], 'y-', Label='GyroX')
    axes2[i, 1].plot(sensor2[i][['GyroY']], 'g-', Label='GyroY')
    axes2[i, 1].plot(sensor2[i][['GyroZ']], 'b-', Label='GyroZ')
    axes2[i, 1].legend(loc='upper left')
    for j in range(len(point[i])):
        axes2[i, 1].axvline(x=point[i][j], color= 'r', linestyle = '-', linewidth = 2)
    axes2[i, 2].plot(sensor2[i][['MagX']], 'y-', Label='MagX')
    axes2[i, 2].plot(sensor2[i][['MagY']], 'g-', Label='MagY')
    axes2[i, 2].plot(sensor2[i][['MagZ']], 'b-', Label='MagZ')
    axes2[i, 2].legend(loc='upper left')
    for j in range(len(point[i])):
        axes2[i, 2].axvline(x=point[i][j], color= 'r', linestyle = '-', linewidth = 2)

fig3, axes3 = plt.subplots(num, 3, figsize=(14, 2*num))
for i in range(num):
    axes3[i, 0].plot(sensor3[i][['AccelX']], 'm-', Label='AccelX')
    axes3[i, 0].plot(sensor3[i][['AccelY']], 'g-', Label='AccelY')
    axes3[i, 0].plot(sensor3[i][['AccelZ']], 'b-', Label='AccelZ')
    axes3[i, 0].legend(loc='upper left')
    for j in range(len(point[i])):
        axes3[i, 0].axvline(x=point[i][j], color= 'r', linestyle = '-', linewidth = 2)
    axes3[i, 1].plot(sensor3[i][['GyroX']], 'm-', Label='GyroX')
    axes3[i, 1].plot(sensor3[i][['GyroY']], 'g-', Label='GyroY')
    axes3[i, 1].plot(sensor3[i][['GyroZ']], 'b-', Label='GyroZ')
    axes3[i, 1].legend(loc='upper left')
    for j in range(len(point[i])):
        axes3[i, 1].axvline(x=point[i][j], color= 'r', linestyle = '-', linewidth = 2)
    axes3[i, 2].plot(sensor3[i][['MagX']], 'm-', Label='MagX')
    axes3[i, 2].plot(sensor3[i][['MagY']], 'g-', Label='MagY')
    axes3[i, 2].plot(sensor3[i][['MagZ']], 'b-', Label='MagZ')
    axes3[i, 2].legend(loc='upper left')
    for j in range(len(point[i])):
        axes3[i, 2].axvline(x=point[i][j], color= 'r', linestyle = '-', linewidth = 2)
plt.show()

