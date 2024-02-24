

import uiautomator2 as u2
# d = u2.connect() # connect to device
# d = u2.connect_wifi('192.168.1.3') # connect to device
# print(d.info)
# print(d.serial) #BEWOOZNBYLFYQWHA
# # d.screenshot("home.jpg")
# d.click(0.178, 0.49)

# 读取图像
# image = cv2.imread('errgameimg/game2.jpg')
# image = cv2.imread('gameimg/99/99.jpg')
# numbers = img2arr.img2arr(image,3)
# print(numbers)

# numbers = [0, 1, 2, 3, 5, 6, 20, 78, 99]
numbers = [0, 1, 2, 4, 13, 5, 6, 7, 8, 18, 9, 11, 3, 22, 25, 33, 16, 17, 10, 20, 28, 12, 24, 14, 15, 35, 34, 39, 27, 21, 32, 30, 51, 23, 26, 43, 19, 29, 47, 46, 31, 41, 50, 59, 44, 36, 45, 37, 38, 68, 61, 42, 77, 53, 54, 55, 74, 56, 49, 40, 66, 58, 62, 63, 64, 75, 48, 67, 78, 57, 70, 79, 72, 73, 99, 65, 76, 69, 60, 52, 71]

# 将数组中所有元素加1
numbers = [num + 1 for num in numbers]

# 将一维数组转换为二维数组
numbers_2d = [numbers[i:i+9] for i in range(0, len(numbers), 9)]
print(numbers_2d)

# numbers = [0, 1, 2, 3, 5, 6, 20, 78, 99]
numbers = list(range(81))

# 将数组中所有元素加1
numbers = [num + 1 for num in numbers]
# 将一维数组转换为二维数组
numbers_2d = [numbers[i:i+9] for i in range(0, len(numbers), 9)]
print(numbers_2d)