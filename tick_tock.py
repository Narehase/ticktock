#tick tock
#2022.01.16 ~ 17
#22.01.06 : All
#22.01.07 : white line plus

import numpy as np
import cv2
import math
import datetime

base = np.zeros([1500,1500,3])

def bizz(base, r = 0):
    r += 270
    for i in range(5):
        i += 300
        rx, ry = 750,750
        
        s = i * math.sin(math.radians(r)) + rx
        c = i * math.cos(math.radians(r)) + ry

        base[int(s),int(c)] = [255,255,255]

    return base


for i in range(360):
    base = bizz(base, i)
    

def pang(base, r = 0):
    r += 270
    for i in range(200):
        rx, ry = 750,750
        
        s = i * math.sin(math.radians(r)) + rx
        c = i * math.cos(math.radians(r)) + ry

        base[int(s),int(c)] = [255,255,255]

    return base

def pang_(base, r = 0):
    r += 270
    for i in range(300):
        rx, ry = 750,750
        
        s = i * math.sin(math.radians(r)) + rx
        c = i * math.cos(math.radians(r)) + ry

        base[int(s),int(c)] = [0,0,255]

    return base

def pangm(base, r = 0):
    r += 270
    for i in range(250):
        rx, ry = 750,750
        
        s = i * math.sin(math.radians(r)) + rx
        c = i * math.cos(math.radians(r)) + ry

        base[int(s),int(c)] = [255,0,0]

    return base


while True:
    for i in range(360):
        now = datetime.datetime.now()
        print(now.minute)
        last = pang(base.copy(),now.hour * 15 * 2)
        last = pang_(last,int(now.second) * 6)
        last = pangm(last,int(now.minute)*6)
        cv2.imshow("pang", last)
        cv2.waitKey(1)
