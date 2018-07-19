from __future__ import print_function
import csv
import serial
from time import sleep
import time
from datetime import datetime

devices = ['/dev/tty.usbserial-MWVK5MZ', '/dev/tty.usbserial-MWVK7NL', '/dev/tty.usbserial-MWVK5L4', '/dev/tty.usbserial-MWVK5L2']
ser1 = serial.Serial(devices[0], 115200)
ser2 = serial.Serial(devices[1], 115200)
ser3 = serial.Serial(devices[2], 115200)
ser4 = serial.Serial(devices[3], 115200)
num=0
childId1 = "ed=810F1C1C";
childId2 = "ed=810F19CF";
childId3 = "ed=810F1D12";
childId4 = "ed=810F19B1";

def output(filename, ser):
        now = datetime.now()
        value = ser.readline().rstrip()
        arr = value.split(":")
        if(len(arr) == 13):
            (nil, nil2,  rc, lq, ct, ed, num, ba, a1, a2, x, y, z) = value.split(":")
            # (nil, ts, nil2, lq, ct, ed, ba, mn, nil3, a1, a2i, p, x, y, z, nil4) = value.split(";")
            if(ed == childId1):
                with open(filename + childId1 + ".csv", 'a') as f:
                    writer = csv.writer(f, lineterminator='\n')
                    a = [now, ct, lq, ed, x, y, z]
                    writer.writerow(a)
                    print(a)
            elif(ed == childId2):
                with open(filename + childId2 + ".csv", 'a') as f:
                    writer = csv.writer(f, lineterminator='\n')
                    a = [now, ct, lq, ed, x, y, z]
                    writer.writerow(a)
                    print(a)
            elif(ed == childId3):
                with open(filename + childId3 + ".csv", 'a') as f:
                    writer = csv.writer(f, lineterminator='\n')
                    a = [now, ct, lq, ed, x, y, z]
                    writer.writerow(a)
                    print(a)
            elif(ed == childId4):
                with open(filename + childId4 + ".csv", 'a') as f:
                    writer = csv.writer(f, lineterminator='\n')
                    a = [now, ct, lq, ed, x, y, z]
                    writer.writerow(a)
                    print(a)

while True:
    output("/Users/ren/Desktop/TweliteTest/twelite_back_R/",  ser1)
    output("/Users/ren/Desktop/TweliteTest/twelite_front_L/", ser2)
    output("/Users/ren/Desktop/TweliteTest/twelite_back_L/", ser3)
    output("/Users/ren/Desktop/TweliteTest/twelite_front_R/", ser4)
    # /Users/ren/Desktop/TweliteTest/%s.csv

