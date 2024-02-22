import cv2
import numpy as np
from recognition import img2arr
from klotski import klotski
from tensorflow import keras


# 读取图像
image = cv2.imread('game2.jpg')
numbers = img2arr.img2arr(image)
print(numbers)

steps = klotski.get_path(numbers)
print(steps)

for step in steps:
    index0 = step[0]
    index1 = step[1]

    a = numbers[index0]
    b = numbers[index1]

    click_index = index0
    if a == 8:
        click_index = index1

    numbers[index0] = numbers[index1]
    numbers[index1] = a

    print(click_index)
    print(numbers)

def get_point(index):
    start_x = 120
    start_y = 23
    end_x = 2400
    end_y = 1080

    one_w = 710
    one_h = 344

    # 计算中心点的比例
    row = index // 3  # 行数
    col = index % 3   # 列数

    center_x = start_x + col * one_w + one_w // 2
    center_y = start_y + row * one_h + one_h // 2

    ratio_x = (center_x - start_x) / (end_x - start_x)
    ratio_y = (center_y - start_y) / (end_y - start_y)

    return ratio_x, ratio_y

# # 调用函数并打印结果示例
# index = 1
# ratio_x, ratio_y = get_point(index)
# print(ratio_x, ratio_y)
