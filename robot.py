#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      a.bykanov
#
# Created:     07.10.2019
# Copyright:   (c) a.bykanov 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
# u=0.3
# v=2
# l0=0.5
# x0=0.3
# y0=0.1
# d=0.4
# w=0.5
import math
u=0.3
v=2
l0=0.5
x0=0.3
y0=0.1
d=0.31
w=0.11
a=(l0-x0)*v
b=v*y0
c=u*y0
sqr=math.sqrt(a**2+b**2)
fi=math.asin(a/sqr)
alfa=math.acos(c/sqr)+fi
t=y0/(v*math.sin(alfa))
xobj=x0+u*t
xrob=(l0+v*math.cos(alfa)*t)
yrob=v*math.sin(alfa)*t
y=(xrob-l0)*math.tan(alfa)
print('u=',u,'m/s')
print('v=',v,'m/s')
print('x0=',x0)
print('y0=',y0)
print('l0=',l0)
print('alfa=',alfa*180/3.14,'degree')
print('t=',t,'seconds')
print('------------object coordinates-----------')
print('xobj=',xobj,';yobj=',y0)
print('xrob=',xrob,';yrob=',yrob)
print('y(xrob)=',y)
print()

i=0.001
j=0.001
# print('x \ y',end=' ')
# while j<w:
#    print('y0=',round(j,2),end='   ')
#    j+=0.05
# print()
j=0.01
while i<d:
    print('x0=',round(i,2),end=' ')
    while j<w:
        a=(l0-i)*v
        b=v*j
        c=u*j
        sqr=math.sqrt(a**2+b**2)
        fi=math.asin(a/sqr)
        alfa=math.acos(c/sqr)+fi
        t=j/(v*math.sin(alfa))
        xobj=i+u*t
        yobj=j
        xrob=(l0+v*math.cos(alfa)*t)
        yrob=v*math.sin(alfa)*t
        deltax=abs(xobj-xrob)/xobj*100
        deltay=abs(yobj-yrob)/xobj*100
        j+=0.01
    


   
    i+=0.01
    j=0.01
print()
print('xobj - ',xobj,'yobj - ',yobj) 
print('xrob - ',xrob,'yrob - ', yrob)


# print(deltax,';',deltay)
