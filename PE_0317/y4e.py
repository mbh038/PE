#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 21:33:27 2017

@author: mbh
"""

from math import sin, cos, sqrt, pi
from scipy import integrate
import time

g = 9.81         #  m/s^2
v_init = 20          # m/s
h0 = 100        #  m

def quadratic(a, b, c):
    x1 = (-b + sqrt(b * b - 4 * a * c)) / (2 * a)
    x2 = (-b - sqrt(b * b - 4 * a * c)) / (2 * a)
    return x1, x2


def get_trajectory_points( α, h0, v_init, g ) :

    v0 = [  v_init * cos(α*pi/180), v_init * sin(α*pi/180)   ]
    a, b, c = -g/2 , v0[1], h0
    t_total = max(quadratic(a,b,c))   
    x_max = t_total * v0[0]
    t_mid = -b/(2*a)
    y_max = a* t_mid**2 + b*t_mid + c
    x_mid = v0[0] * t_mid

    return x_mid , y_max , x_max


def my_solution(max_angle, min_angle, step ) :

    yM, xM = 0, 0
    ratio = -1/step

    for alpha in range( int(max_angle*ratio) , int(min_angle*ratio), int(step*ratio) ) :
        alpha = alpha/ratio
        x_mid , y_max , x_max = get_trajectory_points( alpha, h0, v_init, g )
        if y_max > yM :        yM = y_max
        if x_max > xM :     xM = x_max

    print('\ny_max = ', yM, '       x_max = ', xM)    

    print('---'*30)
    yM =  120.38735983690111
    a = -yM/(xM)**2
    G = lambda y : pi*(y - yM)/a
    I = integrate.quad(G, 0, yM)
        
    print('\nVolume calculated with scipy.integrate.quad paraboloid of rotation   = ',  I ,'          ', round(I[0], 4 ) )

    print('---'*30)
    V = (pi/2)*yM * xM**2

    print('\nVolume calculated with formula of paraboloid of rotation  = ', V , round(V , 4) )

    print('---'*30)
    H = lambda y :  pi*  ( ((2*v_init**2)/g)  * ( ( v_init**2/(2*g) + h0 ) - y  )  )
    J = integrate.quad( H , 0, yM )
    # https://de.wikipedia.org/wiki/Wurfparabel#Einh.C3.BCllende_Wurfparabel
    print('\nVolume calculated with Envelope of the throwing parabola with common initial velocity : \n'
          'J = ', J, '             ANSWER  =  ',  round(J[0], 4) )


    return round(V, 4)

t=time.clock()
my_solution(22.5, 22.3, -0.001 )      #   ANSWER  =   1856532.8455
print(time.clock()-t)