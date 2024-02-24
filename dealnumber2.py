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
    split_count = 5
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
    numbers = img2arr.img2arr(image,split_count)
    print(numbers)

    sorted_numbers = sorted(numbers)
    # 给定的数组
    # given_array = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    given_array = list(range(split_count*split_count-1))
    given_array.append(99)

    # 检查排序后的数组是否等于给定数组
    if sorted_numbers != given_array:
        print("识别的图像不正确")
        print(sorted_numbers)
        new_uuid = uuid.uuid4()
        cv2.imwrite(f'./errgameimg/number_{new_uuid}.jpg', image)  # 保存图像
        return

    steps = klotski.get_path(numbers)
    print(steps)
    if not steps:
        print("klotski steps为空")
        return

    click_indexs = []
    for step in steps:
        index0 = step[0]
        index1 = step[1]

        a = numbers[index0]
        b = numbers[index1]

        click_index = index1
        # if a == 8:
        #     click_index = index1

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

