import concurrent
import os
import threading
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

    ratio_x = (center_x) / width
    ratio_y = (center_y) / height

    # return ratio_x, ratio_y
    return center_x, center_y


print("start connect")
d = u2.connect()  # connect to device
print("end connect")
print(d.info)
print(d.serial)  # BEWOOZNBYLFYQWHA

print(d.settings)


# 配置点击前延时
# d.settings['operation_delay'] = (0.01, 0.01)


# def async_click(executor, d, x, y):
#     thread_start_time = time.perf_counter()
#     executor.submit(d.click, x, y)
#     thread_end_time = time.perf_counter()
#     print(f"线程执行时间{thread_end_time-thread_start_time}秒")
#     sleep_time = 0.1
#     time.sleep(sleep_time)
#     print(f"点击sleep时间{sleep_time}秒")
def async_click(executor, d, x, y):
    click_start_time = time.perf_counter()
    # d.click(x, y)
    os.system(f'adb shell input tap {x} {y}')
    click_end_time = time.perf_counter()
    # print(f"click时间{click_end_time - click_start_time}秒")


def cancel(d):
    sx1, sy1 = 500, 500
    sx2, sy2 = 600, 600
    ex1, ey1 = 500, 500
    ex2, ey2 = 600, 600
    d().gesture((sx1, sy1), (sx2, sy2), (ex1, ey1), (ex2, ey2))


def do_flow(executor):
    # 点npc
    npc_start_time = time.time()
    print("点npc")
    d.click(0.526, 0.28)
    # async_click(executor,d,0.526, 0.28)
    time.sleep(0.5)

    # d1
    d.click(0.526, 0.28)
    # async_click(executor,d, 0.526, 0.28)
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
    npc_end_time = time.time()
    print(f"npc交互耗时:{npc_end_time - npc_start_time}秒")

    recognition_start_time = time.time()
    # 读取图像
    image = cv2.imread('game2.jpg')
    numbers = img2arr.img2arr(image, split_count)
    recognition_end_time = time.time()
    print(f"图片读取识别耗时:{recognition_end_time - recognition_start_time}秒")
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
        cancel(d)
        time.sleep(6)
        return

    klotski_start_time = time.time()
    if split_count == 9:
        steps = klotski99.get_path_warp(numbers)
    else:
        steps = klotski.get_path(numbers)
    klotski_end_time = time.time()
    print(f"数字华容道求解耗时:{klotski_end_time - klotski_start_time}秒")
    print(f"移动次数:{len(steps)}")
    print(steps)
    if not steps:
        print("klotski steps为空")
        return

    click_indexs = []
    for step in steps:
        click_index = step
        click_indexs.append(click_index)

    print(f"点击次数:{len(click_indexs)},click_indexs:{click_indexs}")

    click_start_time = time.time()
    for click_index in click_indexs:
        ratio_x, ratio_y = get_point(click_index, split_count)
        print(f"click_index:{click_index}")
        print(ratio_x, ratio_y)
        d.click(ratio_x, ratio_y)
        async_click(executor, d, ratio_x, ratio_y)
    click_end_time = time.time()
    print(f"点击耗时:{click_end_time - click_start_time}秒")
    print(f"点击次数:{len(click_indexs)}")
    time.sleep(6)
    # 点xia
    d.click(0.296, 0.497)


while True:
    one_flow_start_time = time.time()
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        do_flow(executor)

    # 暂停程序执行1秒
    time.sleep(3)
    one_flow_end_time = time.time()
    print(f"完成一次流程总时间:{one_flow_end_time - one_flow_start_time}秒")
