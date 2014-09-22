# -*- coding: utf-8 -*-
"""
Created on Mon Sep 22 11:10:54 2014

@author: personne
"""

import nxt

b = nxt.find_one_brick()
m_left = nxt.Motor(b, nxt.PORT_B)
m_right = nxt.Motor(b, nxt.PORT_C)

sonar = nxt.sensor.Ultrasonic(b,nxt.PORT_1)

T = []

def terminer() :
    m_left.run(0)
    m_right.run(0)
    print "extinction des moteurs"
    exit(0)


def principal() :
    tmp = 500
    x = sonar.get_sample
    while(tmp > 1) :  
        tmp = tmp - 1
        m_left.run(80)
        m_right.run(-80)
        T.append(x())
        if x() < 20:
            print T
            terminer()
    print T
    terminer()
     
    



try:
    principal()
except KeyboardInterrupt:
    terminer()