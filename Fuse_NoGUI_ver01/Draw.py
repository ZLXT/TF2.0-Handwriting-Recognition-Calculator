from cv2 import cv2
import numpy as np

mouse_down = False
circle_color = (0,0,255)
circle_radius = 6
last_point = (0,0)

img = np.ones((512,1024,3),np.uint8)
img[:] = (255,255,255)

def Draw_Circle(event,x,y,flags,param):
    global img
    global mouse_down
    global last_point

    if event == cv2.EVENT_LBUTTONDOWN:
        mouse_down = True
        cv2.circle(img,(x,y),int(circle_radius/2),circle_color,-1)
        last_point = (x,y)
    elif event == cv2.EVENT_LBUTTONUP:
        mouse_down = False
    elif event == cv2.EVENT_MOUSEMOVE:
        if mouse_down:
            cv2.line(img,pt1=last_point,pt2=(x,y),color=circle_color,thickness=circle_radius)
            last_point = (x,y)

#============================================
#建立窗口并返回图像
def Create_Window():
    cv2.namedWindow('Draw_Window')
    cv2.setMouseCallback('Draw_Window',Draw_Circle)

    while (True):
        cv2.imshow('Draw_Window',img)
        if cv2.waitKey(1) == ord('q'):
            break

    cv2.destroyAllWindows()
    return img
#cv2.imwrite("OpenCV_Paint.jpg",img)