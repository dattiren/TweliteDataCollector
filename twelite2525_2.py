from __future__ import print_function
import csv
import serial
from time import sleep
import time
from datetime import datetime

devices = ['/dev/ttyUSB0', '/dev/ttyUSB1']
#ser1 = serial.Serial(devices[0], 115200)
ser2 = serial.Serial(devices[1], 115200)
#ser3 = serial.Serial(devices[2], 115200)
#ser4 = serial.Serial(devices[3], 115200)
num=0
childId1 = "810F19B1";
childId2 = "810F19CF";
childId3 = "810F1D12";
#childId4 = "ed=810F19B1";
start = time.time()

def output(filename, ser):
        now = datetime.now()
        while True:
            value = ser.readline().rstrip().decode('utf-8')
            arr = value.split(":")
            if(len(arr) == 13):
                list = ['ed=', 'lq=', 'ba=','x=','y=', 'z=']
                for i in range(len(list)):
                    value=value.replace(list[i], '')
                (nil, nil2,  rc, lq, ct, ed, num, ba, a1, a2, x, y, z) = value.split(":")
                # (nil, ts, nil2, lq, ct, ed, ba, mn, nil3, a1, a2i, p, x, y, z, nil4) = value.split(";")
                if(ed == childId1):
                    with open(filename + "center.csv", 'a') as f:
                        writer = csv.writer(f, lineterminator='\n')
                        ts = round(time.time() - start, 2)
                        a = [ts, lq, ba, x, y, z]
                        writer.writerow(a)
                        print(a)
                elif(ed == childId2):
                    with open(filename + "right.csv", 'a') as f:
                        writer2 = csv.writer(f, lineterminator='\n')
                        ts2 = round(time.time() - start, 2)
                        a2 = [ts2, lq, ba, x, y, z]
                        writer2.writerow(a2)
                        print(a2)
                elif(ed == childId3):
                    with open(filename + "left.csv", 'a') as f:
                        writer3 = csv.writer(f, lineterminator='\n')
                        ts3=round(time.time() - start, 2)
                        a3 = [ts3, lq, ba, x, y, z]
                        writer3.writerow(a3)
                        print(a3)
#            elif(ed == childId4):
#                with open(filename + childId4 + ".csv", 'a') as f:
#                    writer = csv.writer(f, lineterminator='\n')
#                    a = [now, ct, lq, ed, x, y, z]
#                    writer.writerow(a)
#                    print(a)


if __name__ == '__main__':
    #output("/home/pi/Desktop/", ser1)
    output("/home/pi/Desktop/", ser2)
#    output("/home/pi/Desktop/", ser3)
#    output("/Users/ren/Desktop/TweliteTest/twelite_front_R/", ser4)
    # /Users/ren/Desktop/TweliteTest/%s.csv

