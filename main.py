import time
import uuid
import cv2
import numpy as np
from recognition import img2arr
from klotski import klotski
from klotski import klotski99
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

    ratio_x = (center_x ) / width
    ratio_y = (center_y ) / height

    return ratio_x, ratio_y


print("start connect")
d = u2.connect()  # connect to device
print("end connect")
print(d.info)
print(d.serial)  # BEWOOZNBYLFYQWHA


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
    split_count = 9
    print("点拼图")
    # 点拼图
    # d.click(0.296, 0.497) # 拼图1
    d.click(0.528, 0.497)  # 拼图4
    # 暂停程序执行1秒
    time.sleep(6)
    print("screenshot")
    d.screenshot("game2.jpg")
    # 读取图像
    image = cv2.imread('game2.jpg')
    numbers = img2arr.img2arr(image, split_count)
    print(numbers)

    sorted_numbers = sorted(numbers)
    # 给定的数组
    # given_array = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    given_array = list(range(split_count * split_count - 1))
    given_array.append(99)

    # 检查排序后的数组是否等于给定数组
    if sorted_numbers != given_array:
        print("识别的图像不正确")
        print(sorted_numbers)
        new_uuid = uuid.uuid4()
        cv2.imwrite(f'./errgameimg/number_{new_uuid}.jpg', image)  # 保存图像
        return

    if split_count == 9:
        steps = klotski99.get_path_warp(numbers)
    else:
        steps = klotski.get_path(numbers)
    print(steps)
    if not steps:
        print("klotski steps为空")
        return

    click_indexs = []
    for step in steps:
        click_index = step

        print(click_index)
        click_indexs.append(click_index)

    print(click_indexs)
    for click_index in click_indexs:
        ratio_x, ratio_y = get_point(click_index, split_count)
        print(f"click_index:{click_index}")
        print(ratio_x, ratio_y)
        d.click(ratio_x, ratio_y)


while True:
    do_flow()
    time.sleep(6)
    # 点xia
    d.click(0.296, 0.497)
    # 暂停程序执行1秒
    time.sleep(3)
