import time
import uuid
import cv2
import numpy as np
from recognition import img2arr
from klotski import klotski
# from tensorflow import keras
import tensorflow.python.keras as keras

import uiautomator2 as u2
# d = u2.connect() # connect to device
# d = u2.connect_wifi('192.168.1.3') # connect to device
# print(d.info)
# print(d.serial) #BEWOOZNBYLFYQWHA
# # d.screenshot("home.jpg")
# d.click(0.178, 0.49)

# 读取图像
# image = cv2.imread('errgameimg/number_2880c950-3305-4b17-afd1-5b09acbf620f.jpg')
image = cv2.imread('errgameimg/number_0dca5179-233c-453b-9689-3bf6a0c8084f.jpg')
image = cv2.imread('game2.jpg')
numbers = img2arr.img2arr(image)
print(numbers)