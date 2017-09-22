from __future__ import print_function
import csv
import serial
from time import sleep
import time
from datetime import datetime

# devices = '/dev/tty.usbserial-MW8UKP5'
devices = 'your device port'
ser = serial.Serial(devices, 115200)
while True:
    now = datetime.now()
    with open("twelite2525.csv" ,'a') as f:   #ファイル名の設定
        writer = csv.writer(f, lineterminator='\n')
        value = ser.readline().rstrip()
        arr = value.split(":")
        if(len(arr) == 13):
            (nil, nil2,  rc, lq, ct, ed, num, ba, a1, a2, x, y, z) = value.split(":")
            if(ed == "ed=810F0646"):
                a = [now, ed, x, y, z]
                writer.writerow(a)   #csvへの書き込み
