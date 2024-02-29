import time
import uuid
import cv2
import numpy as np
# from tensorflow import keras
import tensorflow.python.keras as keras

import uiautomator2 as u2



print("start connect")
d = u2.connect()  # connect to device
print("end connect")
print(d.info)
print(d.serial)  # BEWOOZNBYLFYQWHA

sx1, sy1 = 500, 500
sx2, sy2 = 600, 600
ex1, ey1 = 500, 500
ex2, ey2 = 600, 600
d().gesture((sx1, sy1), (sx2, sy2), (ex1, ey1), (ex2, ey2))
