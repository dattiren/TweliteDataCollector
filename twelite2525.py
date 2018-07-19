from __future__ import print_function
import csv
import serial
from time import sleep
import time
from datetime import datetime

devices = '/dev/tty.usbserial-MWVK5L2'
ser = serial.Serial(devices, 115200)
num=0
while True:
    now = datetime.now()
    with open('/Users/ren/Desktop/demo.csv' ,'a') as f:
        writer = csv.writer(f, lineterminator='\n')
        value = ser.readline().rstrip().decode('utf-8')
        arr = value.split(":")

        if(len(arr) == 13):
            list = ['ed=', 'lq=', 'x=', 'y=', 'z=']
            for i in range(len(list)):
                value = value.replace(list[i], '')
            (nil, nil2,  rc, lq, ct, ed, num, ba, a1, a2, x, y, z) = value.split(":")
            writer.writerow(lq)
           # (nil, ts, nil2, lq, ct, ed, ba, mn, nil3, a1, a2i, p, x, y, z, nil4) = value.split(";")
           #810F1C1C,810F19CF ,810F1D12 
            # a = [now, ct, lq, ed, ba, x, y, z]
            #a = [lq]
            print(lq)
