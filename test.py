import cv2
import uiautomator2 as u2

from recognition import img2arr

# d = u2.connect() # connect to device
# d = u2.connect_wifi('192.168.1.3') # connect to device
# print(d.info)
# print(d.serial) #BEWOOZNBYLFYQWHA
# # d.screenshot("home.jpg")
# d.click(0.178, 0.49)

# 读取图像
# image = cv2.imread('errgameimg/game2.jpg')
# image = cv2.imread('gameimg/55/55.jpg')
image = cv2.imread('gameimg/99/99_xiandai_shengdan.jpg')
numbers = img2arr.img2arr(image,9)
print(numbers)

sorted_numbers = sorted(numbers)
print(sorted_numbers)

split_count = 9
given_array = list(range(split_count * split_count - 1))
given_array.append(99)

# 检查排序后的数组是否等于给定数组
if sorted_numbers != given_array:
    print("识别的图像不正确")
else:
    print("识别的图像正确")


# 将数组中所有元素加1
numbers = [num + 1 for num in numbers]

# 将一维数组转换为二维数组
numbers_2d = [numbers[i:i+9] for i in range(0, len(numbers), 9)]
print(numbers_2d)

# 将数组中所有元素加1
sorted_numbers = [num + 1 for num in sorted_numbers]
# 将一维数组转换为二维数组
sorted_numbers_2d = [sorted_numbers[i:i+9] for i in range(0, len(sorted_numbers), 9)]
print(sorted_numbers_2d)