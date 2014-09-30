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
    T.pd()
    for i in range(720/angle):
        liste.append(telemetry(T,boxelist))
        T.left(angle)
    return liste
def tournesur2(T, angle) :
    liste = []
    T.right(90)    
    for i in range (180/angle):         
        liste.append(telemetry(T,boxelist))        
        T.left(angle)
    return liste

def sortie() :
    for k in range(10) : 
        if k == 0:
            liste=[]        
            liste=tourne(T, 2)
            liste = [float(x) for x in liste]
            m=[]
            for j in range(0, 180):
                m.append(average(liste[j:j+4]))
            imax = m.index(max(m))
            T.right(360-imax*2)            
            T.pd()
        else:
            liste=[]
            liste=tournesur2(T, 2)
            liste = [float(x) for x in liste]
            m=[]
            for j in range(0, 90):
                m.append(average(liste[j:j+4]))
            imax = m.index(max(m))
            T.right(180-imax*2)            
            T.pd()
        """imin = min(liste)"""
        for a in range(10):
            if telemetry(T , boxelist) > 25:
                T.fd(0)
                T.fd(10)
    return None

######### main ########
turtle.clearscreen()
T = turtle.Turtle()
T.tracer(2,1)
T.penup()
boxelist = [ new_box(0,0,580) ]
boxelist = boxelist+[ new_box(110*cos(1+i*2*pi/15),110*sin(1+i*2*pi/15),random.randint(10,40)) for i in range(12)]
boxelist = boxelist+[ new_box(190*cos(3+i*2*pi/15),190*sin(3+i*2*pi/15),random.randint(10,40)) for i in range(12)]


sortie()

#T.pd()
#for i in range(360):
 #   T.right(1)
  #  x=telemetry(T,boxelist)
  # T.fd(x)
  #T.bk(x)

"""print liste"""


"""print liste2
plt.plot(liste)
plt.show(liste)"""
"""print telemetry(T,boxelist)"""
raw_input()
