import csv
import serial
from time import sleep
import time
from datetime import datetime

device = '/dev/tty.usbserial-MWVK5L2'
ser1 = serial.Serial(device, 115200)
num=0
childId = "ed=810F1C1C";


def output(filename, ser):
        now = datetime.now()
        value = ser.readline().rstrip()
        arr = value.split(":")
        if(len(arr) == 13):
            (nil, nil2,  rc, lq, ct, ed, num, ba, a1, a2, x, y, z) = value.split(":")
            # (nil, ts, nil2, lq, ct, ed, ba, mn, nil3, a1, a2i, p, x, y, z, nil4) = value.split(";")
            if(ed == childId):
                with open(filename + childId + ".csv", 'a') as f:
                    writer = csv.writer(f, lineterminator='\n')
                    a = [now, ct, lq, ed, x, y, z]
                    writer.writerow(a)
                    print(a)


while True:
    output("/Users/ren/Desktop/TweliteTest/twelite_back_R/",  ser1)
