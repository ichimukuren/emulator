#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import numpy as np
import math
import random
import time

current_milli_time = lambda: int(round(time.time() * 1000))

def get_rect(w=100,h=50):
    point_one = (random.randint(0,400-w),random.randint(0,500-h))
    point_two = (point_one[0] + w,point_one[1]+h)
    return point_one, point_two

def new_line(line):
    global output,x1,x2,robot_point,catch_point,goal,line_speed,robot_speed,cnt_start
    goal = False
    output = line.copy()
    robot_point = (500,500)
    x1,x2 = get_rect()
    cnt = get_center(x1,x2)
    cnt_start = cnt
    catch_point = get_catch_point(cnt[0],500,cnt[1],line_speed,robot_speed)
    
def clear_detect(last_rect):
    global x1,x2,output
    output = line.copy()
    x1,x2 = last_rect
    
def refresh_line(x,y,robot):
    global x1,x2,output,center,robot_point,angle,catch_point,cnt_start
    output = line.copy()
    
    x1,x2 = x,y
    
    catch_point =  get_catch_point(cnt_start[0],500,cnt_start[1],line_speed,robot_speed)
    robot_point = robot
    center = ((x[0]+y[0])//2,(x[1]+y[1])//2)

#получение координаты точки встречи коробки и робота
def get_catch_point(x0,l0,y0,u,v):
#     b = 2*y0
#     a = (l0-x0)*v
    
#     ab = math.sqrt(a**2 + b**2)
#     x = y0/math.tan( math.acos(b/ab) + math.asin(a/ab))

    a=(l0-x0)*v
    b=v*y0
    c=u*y0
    sqr=math.sqrt(a**2+b**2)
    fi=math.asin(a/sqr)
    alfa=math.acos(c/sqr)+fi
    t=y0/(v*math.sin(alfa))
    xobj=x0+u*t
    yobj=y0
    xrob=(l0+v*math.cos(alfa)*t)
    yrob=v*math.sin(alfa)*t
    y=(xrob-l0)*math.tan(alfa)
    print(f"xobj {int(xobj)} yobj {int(yobj)} xrob {int(xrob)} yrob {int(yrob)} Y(XRob) {y}")
    return (int(xrob),int(y0))
  
        
def get_center(x,y):
    return ((x[0]+y[0])//2,(x[1]+y[1])//2)
    
    
def distf(a,b):
    return math.sqrt(math.pow(a[0]-b[0],2)+math.pow(a[1]-b[1],2))
    


# In[2]:


fourcc = cv2.VideoWriter_fourcc(*'MP4V') 
v_out = None


line = np.zeros((500,1200,3))
line[:,398:400] = (255,255,255) 

# положение робота
robot_point = (500,500)

angle = 0

#скорости конвейера и робота
line_speed = 30
robot_speed = 200

#координаты левого верхнего и правого нижнего угла коробки для отрисовки
x1,x2 = get_rect()

#центр коробки x,y
center = get_center(x1,x2)
cnt_start = center

#ожидаемая координата встречи робота и коробки
catch_point = get_catch_point(x0=center[0],l0=500,y0 = center[1],u=line_speed,v=robot_speed)

cv2.namedWindow('image')
cv2.createTrackbar('Line Speed', 'image', line_speed, 500,lambda x : x)


output = line.copy()

last_time = current_milli_time()

detected = False
goal = False
 
while True:
    line_speed = cv2.getTrackbarPos('Line Speed', 'image')
    key = cv2.waitKey(1)
    last_rect = x1,x2
    
    
    cv2.putText(output, "g - new box; d - detection", (500,20), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 1)
    cv2.circle(output, (int(robot_point[0]),int(robot_point[1])), 10,(0,0,255),15)
    cv2.rectangle(output, x1, x2, (0, 255, 255), 3)
    
    if detected:
       
        center = get_center(x1,x2)

        cv2.circle(output, center, 10,(0,255,0),3)
        cv2.circle(output, catch_point, 10,(0,255,0),3)
    
        if (current_milli_time()-last_time)>=100:
            
            
           
            if not goal:
                x1 = x1[0]+line_speed//10,x1[1]
                x2 = x2[0]+line_speed//10,x2[1]
                angle = - 180 - (math.atan2(robot_point[1] - catch_point[1], robot_point[0] - catch_point[0]) * 180/math.pi)
                robot_point = int(robot_point[0])+ (robot_speed//10) * math.cos(angle *math.pi/180),int(robot_point[1])- (robot_speed//10) * math.sin(angle*math.pi/180)

            if distf(robot_point,catch_point)<15:
                goal = True
                
            
            refresh_line(x1,x2,robot_point)
            last_time = current_milli_time()
            
            

            
#     if v_out is None:
#         v_out = cv2.VideoWriter('test {}.mp4'.format(time.time()/1000),fourcc, 60.0, (1200,500),3)
#     v_out.write(np.uint8(output))
    cv2.imshow("image",output)
    
    
    if key == ord('g'):
        new_line(line)
        detected = False
    if key == ord('d'):
        if detected:
            clear_detect(last_rect)
            detected = False
        else: 
            detected = True
        
    if key == ord('q'):
#         v_out.release()
        break 
        
cv2.destroyAllWindows()


# In[3]:


v_out.release()


# In[ ]:




