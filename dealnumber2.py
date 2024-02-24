import time
import uuid
import cv2
import numpy as np
from recognition import img2arr
from klotski import klotski
# from tensorflow import keras
import tensorflow.python.keras as keras

import uiautomator2 as u2


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


d = u2.connect() # connect to device
print(d.info)
print(d.serial) #BEWOOZNBYLFYQWHA


def do_flow():
    # 点npc
    print("点npc")
    d.click(0.526, 0.28)
    time.sleep(0.5)

    # d1
    d.click(0.526, 0.28)
    time.sleep(0.5)

    d.click(0.526, 0.28)
    time.sleep(0.5)

    d.click(0.526, 0.28)
    d.click(0.526, 0.28)
    time.sleep(1)

    print("点拼图")
    # 点拼图
    # d.click(0.296, 0.497) # 拼图1
    d.click(0.528, 0.497) # 拼图4
    # 暂停程序执行1秒
    time.sleep(6)
    print("screenshot")
    d.screenshot("game2.jpg")
    # 读取图像
    image = cv2.imread('game2.jpg')
    numbers = img2arr.img2arr(image,9)
    print(numbers)

    sorted_numbers = sorted(numbers)
    # 给定的数组
    # given_array = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    given_array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 99]

    # 检查排序后的数组是否等于给定数组
    if sorted_numbers != 66:
        print("识别的图像不正确")
        new_uuid = uuid.uuid4()
        cv2.imwrite(f'./errgameimg/number_{new_uuid}.jpg', image)  # 保存图像
        return

    steps = klotski.get_path(numbers)
    print(steps)

    click_indexs = []
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
        click_indexs.append(click_index)

    for click_index in click_indexs:
        ratio_x, ratio_y = get_point(click_index)
        d.click(ratio_x, ratio_y)


while True:
    do_flow()
    time.sleep(6)
    # 点xia
    d.click(0.296, 0.497)
    # 暂停程序执行1秒
    time.sleep(3)

