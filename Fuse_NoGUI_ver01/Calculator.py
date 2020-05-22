import numpy as np
from cv2 import cv2

def Calculator(output_lab):
    equation = "".join(list(output_lab))
    result = eval(equation)
    return result

def Show_Result(result):
    img = np.ones([100, 550, 3])
    font = cv2.FONT_HERSHEY_SIMPLEX
    img = cv2.putText(img, str(result), (10, 70), font, 1.5, (255,0,255),3, cv2.LINE_AA)
    cv2.imshow("Result",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()