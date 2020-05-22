#引入包
import  os
from cv2 import cv2
import numpy as np
import tensorflow as tf
from tensorflow import float32
from PIL import Image 
#np.set_printoptions(threshold=np.inf)

#====================================
#建立窗口，绘制算式输入
mouse_down = False
circle_color = (0,0,255)
circle_radius = 6
last_point = (0,0)

def Draw_Circle(event,x,y,flags,param):
    global draw
    global mouse_down
    global last_point

    if event == cv2.EVENT_LBUTTONDOWN:
        mouse_down = True
        cv2.circle(draw,(x,y),int(circle_radius/2),circle_color,-1)
        last_point = (x,y)
    elif event == cv2.EVENT_LBUTTONUP:
        mouse_down = False
    elif event == cv2.EVENT_MOUSEMOVE:
        if mouse_down:
            cv2.line(draw,pt1=last_point,pt2=(x,y),color=circle_color,thickness=circle_radius)
            last_point = (x,y)

draw = np.ones((512,1024,3),np.uint8)
draw[:] = (255,255,255)

cv2.namedWindow('Draw')
cv2.setMouseCallback('Draw',Draw_Circle)

while (True):
    cv2.imshow('Draw',draw)
    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()
#绘制的图像储存于draw中

#======================================
#垂直投影法对图像进行处理
picture = []#得到的处理结果储存于picture列表中
GrayImage=cv2.cvtColor(draw,cv2.COLOR_BGR2GRAY) #转为灰度图
ret,thresh=cv2.threshold(GrayImage,130,255,cv2.THRESH_BINARY)#二值化处理
(thresh_h,thresh_w)= thresh.shape
#--------------------------
#进行纵向垂直投影
hang = np.zeros(thresh_h)
for j in range(0,thresh_h):
    for i in range(0,thresh_w):
        if  thresh[j,i] != 255:
            hang[j] += 1

flip_flop = False
white = 0
black = 0
line_poin = []
for i in range(0,thresh_h):
    if hang[i] > 0:
        if flip_flop == False:
            line_poin.append(white)
            white = 0
            flip_flop = True
        black += 1
    else:
        if flip_flop == True:
            line_poin.append(black)
            black = 0
            flip_flop = False
        white += 1

num_line = len(line_poin)/2#算式的行数(不为空白的个数)
line_poin.append(thresh_h-sum(line_poin))#黑块和白块的长度

img_line = tf.convert_to_tensor(thresh)#转换为tf变量
picture_line = tf.split(img_line,num_or_size_splits = line_poin,axis=0)#将不为空白的部分取出
#-----------------------------
#列垂直投影
for i in range(0,int(num_line)):
    image = picture_line[2*i+1].numpy()
    (image_h,image_w) = image.shape

    lie = np.zeros(image_w)
    for i in range(0,image_w):
        for j in range(0,image_h):
            if  image[j,i] != 255:
                lie[i] += 1

    flip_flop = False
    white = 0
    black = 0
    lie_poin = []
    for i in range(0,image_w):
        if lie[i] > 0:
            if flip_flop == False:
                lie_poin.append(white)
                white = 0
                flip_flop = True
            black += 1
        else:
            if flip_flop == True:
                lie_poin.append(black)
                black = 0
                flip_flop = False
            white += 1

    num_lie = len(lie_poin)/2
    lie_poin.append(image_w-sum(lie_poin))
    img_lie = tf.convert_to_tensor(image)

    picture_lie = tf.split(img_lie,num_or_size_splits = lie_poin,axis=1)

#=============================================
#对图片进行预处理增加长宽,防止改变大小时产生过大的形变
    for i in range(0,int(num_lie)):
        (h,w) = picture_lie[2*i+1].get_shape()
        if h > w:
            num =(h-w)//2
            front = tf.fill([h,num],255)
            front = tf.cast(front,dtype=float32)
            behind = tf.fill([h,num],255)
            behind = tf.cast(behind,dtype=float32)
            im = tf.cast(picture_lie[2*i+1],dtype=float32)
            im = tf.concat([front,im],axis=1)
            im = tf.concat([im,behind],axis=1)
            im = im.numpy()
            picture.append(im)

        else:
            num =(w-h)//2
            front = tf.fill([num,w],255)
            front = tf.cast(front,dtype=float32)
            behind = tf.fill([num,w],255)
            behind = tf.cast(behind,dtype=float32)
            im = tf.cast(picture_lie[2*i+1],dtype=float32)
            im = tf.concat([front,im],axis=0)
            im = tf.concat([im,behind],axis=0)
            im = im.numpy()
            picture.append(im)

#====================================
#保存图片
pic_input = []
for i in range(0,len(picture)):
    src = cv2.resize(picture[i], (28, 28), interpolation=cv2.INTER_CUBIC)
    src = abs(255-src)#将图片黑白反转
    pic_input.append(src)
    num = i + 0
    cv2.imwrite(str(num)+".jpg",pic_input[i])
