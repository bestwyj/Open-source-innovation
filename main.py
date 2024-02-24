import cv2
import random
import numpy as np

im = cv2.imread('dragon.png')
im0 = im.copy()
h,w,c = im.shape
print(h,w,c)

B = 90

temp=im[132:132+B,0:B]
'''
cv2.imshow('image', im)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''

value = [
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1]
]
name='Killing the Azure Dragon'
score = 0

def drawpic():
    global im
    for i in range(3):
        for j in range(3):
            X=h//2-135+i*B
            Y=w//2-135+j*B
            if value[i][j] == 1:
                im[X:X+B,Y:Y+B] = temp

    for i in range(3):
        for j in range(3):
            X=h//2-135+i*B
            Y=w//2-135+j*B
            cv2.rectangle(im, (Y,X), (Y+B,X+B), (0,255,0), 3)
    
    # 绘制血条
def drawddl():
    cv2.rectangle(im, (10,10), (10+score, 30), (0, 0, 255), -1)
    cv2.rectangle(im, (10,10), (110, 30), (255, 255, 0), 3)

#mouse callback function
def catch(event,x,y,flags,param):
    global score
    if score >= 100:
        return
    if event==cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(im,(x,y),40,(0,0,255),-1)
        # 计算分数
        for i in range(3):
            for j in range(3):
                Y=h//2-135+i*B
                X=w//2-135+j*B
                # print(X, Y)
                if X<x and x<X+B and Y<y and y<Y+B:
                    if value[i][j] == 1:
                        score += 10
                    else:
                        score -= 5
                    break
        print(score)
        #score += 10
        score = min(100, max(0, score))
        drawddl()
        
        cv2.imshow(name, im)
# 将窗口与回调函数绑定

cv2.namedWindow(name)
cv2.setMouseCallback(name,catch)
while(1):
    im = im0.copy()
    for i in range(3):
        for j in range(3):
            value[i][j] = random.randint(0, 1)
    drawpic()
    drawddl()
    cv2.imshow(name, np.zeros((h,w,c),np.uint8))
    cv2.imshow(name, im)
    key = cv2.waitKey(600)
    if score >= 100:
        im = im0.copy()
        drawddl()
        cv2.putText(im,'You Win',(10,220), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 4,(0,175,255),10)
        cv2.imshow(name, np.zeros((h,w,c),np.uint8))
        cv2.imshow(name, im)
        while True:
            if cv2.waitKey(1)!=-1 or cv2.getWindowProperty(name, cv2.WND_PROP_VISIBLE)<1:
                break
        break
    if key&0xFF==27 or cv2.getWindowProperty(name, cv2.WND_PROP_VISIBLE)<1:
        break
cv2.destroyAllWindows()
