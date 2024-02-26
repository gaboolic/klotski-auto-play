import time
import uuid
import cv2
import numpy as np
# from tensorflow import keras
import tensorflow.python.keras as keras

import uiautomator2 as u2


def get_point(index, split_count):
    width = 2400
    height = 1080

    # 107 21
    # 13 2
    # 15 2
    # 132 21
    # 左边120 右边147 下面黑条21
    # 小图236 113
    # 小图236 114
    start_x = 120
    start_y = 23
    end_x = 132
    end_y = 21

    roi_width = width - start_x - end_x
    roi_height = height - start_y - end_y

    one_w = (roi_width) // split_count
    one_h = (roi_height) // split_count

    # 计算中心点的比例
    row = index // split_count  # 行数
    col = index % split_count  # 列数

    center_x = start_x + col * one_w + one_w // 2
    center_y = start_y + row * one_h + one_h // 2

    print("center_x,center_y")
    print(center_x,center_y)
    ratio_x = (center_x) / width
    ratio_y = (center_y) / height

    return ratio_x, ratio_y


print("start connect")
d = u2.connect()  # connect to device
print("end connect")
print(d.info)
print(d.serial)  # BEWOOZNBYLFYQWHA



ratio_x, ratio_y = get_point(28,9)
print(ratio_x,ratio_y)
d.click(ratio_x,ratio_y)
