import sys
import time
import math
import serial
import threading
import pandas as pd
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from drawnow import *
from matplotlib.figure import Figure


def click_me_start():
    global key
    key = 1

def click_me_stop():
    global key
    key = 0

#ui 창
def gui():
    global win
    global key
    global scr
    win = tk.Tk()
    win.title("imu_data")
    ttk.Label(win, text="Press the start or stop button").grid(column=1, row=0)
    win.resizable(True, True)
    action_start = ttk.Button(win, text="START", command=click_me_start)
    action_stop = ttk.Button(win, text="STOP", command=click_me_stop)
    action_start.grid(column=0, row=1)
    action_stop.grid(column=2, row=1)
    scr = scrolledtext.ScrolledText(win, width=140, height=50, wrap=tk.WORD)  # tk.WORD or tk.CHAR
    scr.grid(column=0, columnspan=3)
    win.mainloop()

#실시간 그래프
# def figure():
#     plt.title('Sensor data')         #Set the title
#     # plt.grid(True) #Set The grid
#     plt.subplot(311)
#     plt.plot(AccelX, 'r-', label='AccelX') #Set the loine plot
#     plt.plot(AccelY, 'b-', label = 'AccelY')
#     plt.plot(AccelZ, 'g-', label = 'AccelZ')
#     plt.legend(loc = 'upper left')
#     plt.subplot(312)
#     plt.plot(GryoX, 'r-', label='GyroX')  # Set the loine plot
#     plt.plot(GryoY, 'b-', label='GyroY')
#     plt.plot(GryoZ, 'g-', label='GyroZ')
#     plt.legend(loc='upper left')
#     plt.subplot(313)
#     plt.plot(MagX, 'r-', label='MagX')  # Set the loine plot
#     plt.plot(MagY, 'b-', label='MagY')
#     plt.plot(MagZ, 'g-', label='MagZ')
#     plt.legend(loc='upper left')

# 쿼터니안수를 오일러수로 변환
def quat_to_euler(x, y, z, w):
    euler = [0.0, 0.0, 0.0]
    sqx = x * x
    sqy = y * y
    sqz = z * z
    sqw = w * w
    euler[0] = math.asin(-2.0 * (x * z - y * w))
    euler[1] = math.atan2(2.0 * (x * y + z * w), (sqx - sqy - sqz + sqw))
    euler[2] = math.atan2(2.0 * (y * z + x * w), (-sqx - sqy + sqz + sqw))
    return euler

if hasattr(sys, "setdefaultencoding"):
    sys.setdefaultencoding(sys.getfilesystemencoding())

comport_num = input("COM Port : ")
comport_num = 'COM' + comport_num
comport_baudrate = input("Baudrate : ")
ser = serial.Serial(port= comport_num, baudrate= comport_baudrate)
# n = input("Enter the number of IMU :" )

data_from = 1  # 1: sensor  2: rf_receiver
data_format = 1  # 1: euler   2: quaternion
data_index = 0

grad2rad = 3.141592 / 180.0
rad2grad = 180.0 / 3.141592

global key
plt.ion()
cnt=0
i=0
key = 0

data = []

TIME = time.strftime('%m-%d-%H-%M-%S', time.localtime(time.time()))

th_gui = threading.Thread(target=gui)
th_gui.start()
print(th_gui)

while 1:
    line = ser.readline()
    line = line.decode()
    words = line.split(',')  # Fields split
    if (-1 < words[0].find('*')):
        data_from = 1  # sensor data
        data_index = 0
        words[0] = words[0].replace('*', '')
    else:
        if (-1 < words[0].find('-')):
            data_from = 2  # rf_receiver data
            data_index = 1
        else:
            data_from = 0  # unknown format

    if (data_from != 0):
        commoma = words[data_index].find('.')
        if (len(words[data_index][commoma:-1]) == 4):  # 소수부 4자리 판별
            data_format = 2  # quaternion
        else:
            data_format = 1  # euler

        if (data_format == 1):  # euler
            try:
                roll = float(words[data_index]) * grad2rad
                pitch = float(words[data_index + 1]) * grad2rad
                yaw = float(words[data_index + 2]) * grad2rad
                if key == 1:
                    scr.insert(tk.INSERT, time.strftime('%m-%d-%H-%M-%S', time.localtime(time.time())) +', '+ words[0] +', '+ words[4]+', '+words[5]+', '+words[6]+', '+words[7]+', '+words[8]+', '+words[9]+', '+words[10]+', '+words[11]+', '+words[12] +"\n")
                    scr.yview(tk.END)
                    data.append([time.strftime('%m-%d-%H-%M-%S', time.localtime(time.time())), words[0], words[4], words[5], words[6], words[7], words[8], words[9], words[10], words[11], words[12] + "\n"])
                elif key == 0:
                    print("Pause")
                    data_pd = pd.DataFrame(data)
                    data_pd.to_csv("C:\\Users\\Shin Jisu\\Desktop\\" + TIME + ".csv", sep=',', mode='a', header=False)
                    data = []
            except:
                print('.')
        else:  # (data_format==2)quaternion
            try:
                q0 = float(words[data_index])
                q1 = float(words[data_index + 1])
                q2 = float(words[data_index + 2])
                q3 = float(words[data_index + 3])
                Euler = quat_to_euler(q0, q1, q2, q3)
                roll = Euler[1]
                pitch = Euler[0]
                yaw = Euler[2]
                if key == 1:
                    scr.insert(tk.INSERT, time.strftime('%m-%d-%H-%M-%S', time.localtime(time.time())) +', '+ words[0] +', '+words[5]+', '+words[6]+', '+words[7]+', '+words[8]+', '+words[9]+', '+words[10]+', '+words[11]+', '+words[12] +', '+ words[13]+"\n")
                    scr.yview(tk.END)
                    data.append([time.strftime('%m-%d-%H-%M-%S', time.localtime(time.time())), words[0], words[5], words[6], words[7], words[8], words[9], words[10], words[11], words[12], words[13] + "\n"])
                elif key == 0:
                    print("Pause")
                    data_pd = pd.DataFrame(data)
                    data_pd.to_csv("C:\\Users\\Shin Jisu\\Desktop\\"+TIME+".csv", sep=',', mode='a', header=False)
                    data = []
            except:
               print('.')
ser.close