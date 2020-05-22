#引入包
import Draw
from cv2 import cv2
import Vertical_Projection as vp
import Change_Size as cs
import Use_Model as um
import Calculator as cal
#===================================
#绘制图像
draw_picture = Draw.Create_Window()
#===================================
#将图像进行分割为单个
cut_picture = vp.Vertical_Projection(draw_picture)
#===================================
#将图片改为28*28像素大小
pic_input = cs.Change_Size(cut_picture)
#===================================
#加载模型并使用模型进行预测
output_lab = um.Use_Model(pic_input)
#===================================
#输出图片和对应的标签，用于可视化检验

for i in range(0,len(pic_input)):
    cv2.namedWindow(output_lab[i], 0)
    cv2.resizeWindow(output_lab[i], 200, 200)
    cv2.imshow(output_lab[i],pic_input[i])
    #cv2.moveWindow(output_lab[i],100,100)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

#=================================
#计算识别结果并进行显示
result = cal.Calculator(output_lab)

cal.Show_Result(result)