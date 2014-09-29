# -*- coding: utf-8 -*-
"""
Telemetry
"""

from sympy.geometry import Polygon,Line,Point,intersection
from sympy import N
import turtle
import random
from math import *
import numpy as np
import matplotlib.pyplot as plt

def new_box(x,y,c):
    V = turtle.Turtle()
    V.hideturtle(); V.penup()
    V.setpos(x-c/2,y-c/2); V.setheading(0) ; V.pendown();
    for i in range(4):
        V.fd(c)
        V.left(90)
    return Polygon(Point(x-c/2,y-c/2),Point(x-c/2,y+c/2),Point(x+c/2,y+c/2),Point(x+c/2,y-c/2))

def telemetry(T,boxelist):
    a = radians(T.heading())
    P1,P2 = Point(T.xcor(),T.ycor()) , Point(T.xcor()+cos(a),T.ycor()+sin(a))
    P12 = P2 - P1
    intr = [N(P12.dot(p-P1)) for r in boxelist for p in intersection(Line(P1,P2),r) ]
    intr = [d for d in intr if d >= 0]
    #print intr
    return None if intr==[] else (min(intr)+np.random.normal(0,10))

def tourne(T, angle) :
    liste = []    
    for i in range(2*360/angle):  
        liste.append(telemetry(T,boxelist))        
        T.left(angle)
    return liste

def sortie(liste) :
    liste = [float(x) for x in liste]   
    m=[]
    for i in range(0, 100):   
        m.append(average(liste[i:i+9]))
    return m
        
            
######### main ########
turtle.clearscreen()
T = turtle.Turtle()
T .tracer(2,1)
T.penup()


boxelist = [ new_box(0,0,580) ]
boxelist = boxelist+[ new_box(150*cos(1+i*2*pi/15),150*sin(1+i*2*pi/15),random.randint(10,40)) for i in range(12)]
boxelist = boxelist+[ new_box(190*cos(3+i*2*pi/15),190*sin(3+i*2*pi/15),random.randint(10,40)) for i in range(12)]

liste = tourne(T, 5)
"""print liste"""
liste2 = sortie(liste)
i = liste2.index(max(liste2))
T.setheading(i*5)
T.forward(100)
T.fd(100)
"""print liste2
plt.plot(liste)
plt.show(liste)"""

"""print telemetry(T,boxelist)"""
raw_input()