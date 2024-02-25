import cv2
import uiautomator2 as u2

from recognition import img2arr
from klotski import klotski99

# d = u2.connect() # connect to device
# d = u2.connect_wifi('192.168.1.3') # connect to device
# print(d.info)
# print(d.serial) #BEWOOZNBYLFYQWHA
# # d.screenshot("home.jpg")
# d.click(0.178, 0.49)

# 读取图像
# image = cv2.imread('errgameimg/game2.jpg')
# image = cv2.imread('gameimg/55/55.jpg')
image = cv2.imread('gameimg/99/99.jpg')
# numbers = img2arr.img2arr(image,9)

numbers = [0, 1, 2, 4, 13, 5, 6, 7, 8, 18, 9, 11, 3, 22, 25, 33, 16, 17, 10, 20, 28, 12, 24, 14, 15, 35, 34, 39, 27, 21,
           32, 30, 51, 23, 26, 43, 19, 29, 47, 46, 31, 41, 50, 59, 44, 36, 45, 37, 38, 68, 61, 42, 77, 53, 54, 55, 74,
           56, 49, 40, 66, 58, 62, 63, 64, 75, 48, 67, 78, 57, 70, 79, 72, 73, 99, 65, 76, 69, 60, 52, 71]
numbers = [-1 if num == 99 else num for num in numbers]

# 将数组中所有元素加1
numbers = [num + 1 for num in numbers]
print(numbers)

sorted_numbers = sorted(numbers)
print(sorted_numbers)

split_count = 9
given_array = list(range(1, split_count * split_count))
given_array.append(0)

# 检查排序后的数组是否等于给定数组
if sorted_numbers != given_array:
    print("识别的图像不正确")
else:
    print("识别的图像正确")

# 将一维数组转换为二维数组
numbers_2d = [numbers[i:i + 9] for i in range(0, len(numbers), 9)]
print(numbers_2d)

# 将数组中所有元素加1
# sorted_numbers = [num + 1 for num in sorted_numbers]
# 将一维数组转换为二维数组
given_array = [given_array[i:i + 9] for i in range(0, len(given_array), 9)]
print(given_array)

paths = klotski99.get_path(numbers_2d, given_array)
print(len(paths))
print(paths)
