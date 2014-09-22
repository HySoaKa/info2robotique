# -*- coding: utf-8 -*-
"""
Created on Mon Sep 22 08:52:54 2014

@author: personne
"""

import nxt, thread, time

b = nxt.find_one_brick()
mleft = nxt.Motor(b, nxt.PORT_B)
mright = nxt.Motor(b, nxt.PORT_C)

lux = nxt.sensor.Color20(b,nxt.PORT_3)



def terminer():
    print "extinction des moteurs"
    mleft.run(0)
    mright.run(0)
    exit(0)

def principal():
    tmp=100
    while (tmp>1):
        x=lux.get_reflected_light(nxt.sensor.Type.COLORNONE)
        print x        
        tmp = tmp - 1
        if x < 10:
            mleft.run(100)
            mright.run(100)
            time.sleep(0.1)
            mleft.brake()
            mright.brake()
            time.sleep(0.1)
        else: 
            mleft.turn(100, 80) ; time.sleep(0.1); mleft.brake()
            x=lux.get_reflected_light(nxt.sensor.Type.COLORNONE)
            if x > 10:
                mleft.turn(-100, 80) ; time.sleep(0.1); mleft.brake()
                mright.turn(100, 80) ; time.sleep(0.1); mright.brake()
            
    terminer()

try:
    principal()
except KeyboardInterrupt:
    terminer()            
            