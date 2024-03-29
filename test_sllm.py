import time

import cv2
import uiautomator2 as u2

from recognition import img2arr, img2arr_sllm
from klotski import klotski99_sllm

# d = u2.connect() # connect to device
# d = u2.connect_wifi('192.168.1.3') # connect to device
# print(d.info)
# print(d.serial) #BEWOOZNBYLFYQWHA
# # d.screenshot("home.jpg")
# d.click(0.178, 0.49)

# 读取图像
# image = cv2.imread('gameimg/sllm/WechatIMG702.jpg')
image = cv2.imread('gameimg/sllm/WechatIMG723.jpg')

recognition_start_time = time.time()
# numbers = img2arr_dev.img2arr(image, 9)
numbers = img2arr_sllm.img2arr(image, 9)
recognition_end_time = time.time()
print(f"图片识别耗时{recognition_end_time - recognition_start_time}秒")

# numbers = [0, 1, 2, 4, 13, 5, 6, 7, 8, 18, 9, 11, 3, 22, 25, 33, 16, 17, 10, 20, 28, 12, 24, 14, 15, 35, 34, 39, 27, 21,
#            32, 30, 51, 23, 26, 43, 19, 29, 47, 46, 31, 41, 50, 59, 44, 36, 45, 37, 38, 68, 61, 42, 77, 53, 54, 55, 74,
#            56, 49, 40, 66, 58, 62, 63, 64, 75, 48, 67, 78, 57, 70, 79, 72, 73, 99, 65, 76, 69, 60, 52, 71]

print(numbers)
sorted_numbers = sorted(numbers)
print(sorted_numbers)

split_count = 9
given_array = list(range(0, split_count * split_count))

# 检查排序后的数组是否等于给定数组
if sorted_numbers != given_array:
    print("识别的图像不正确")
    exit()
else:
    print("识别的图像正确")

expect_result = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27,
                 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54,
                 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72,
                 73, 74, 75, 76, 77, 78, 79, 80, 0]

# 将一维数组转换为二维数组Ï
numbers_2d = [numbers[i:i + 9] for i in range(0, len(numbers), 9)]
expect_result_2d = [expect_result[i:i + 9] for i in range(0, len(expect_result), 9)]
paths = klotski99_sllm.get_path(numbers_2d, expect_result_2d)
print(f"移动步数:{len(paths)}")
print(paths)

print("打印移动")
current_state = numbers
for path in paths:
    index = path[0] * 9 + path[1]
    zero_index = current_state.index(0)
    current_state[zero_index] = current_state[index]
    current_state[index] = 0
print(current_state)

if current_state == expect_result:
    print("移动正确")
else:
    print("移动错误")

# 86.10537004470825秒
# 移动步数:1361