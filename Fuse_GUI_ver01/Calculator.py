import numpy as np
from cv2 import cv2

def Calculator(output_lab):
    equation = ""
    equation = "".join(list(output_lab))
    result = eval(equation)
    return result,equation