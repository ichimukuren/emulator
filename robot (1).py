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

import math
u=300
v=2000
l0=500
x0=100
y0=100
d=0.4
w=0.5
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

i=0.05
j=0.05
print('x \ y',end=' ')
while j<w:
    print('y0=',round(j,3),end='   ')
    j+=0.05
print()
j=0.05
while i<d:
    print('x0=',round(i,3),end=' ')
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
        j+=0.05
        print(deltax,';',deltay,end=' ')
    print()
    i+=0.05
    j=0.05

