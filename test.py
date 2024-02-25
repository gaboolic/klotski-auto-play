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
image = cv2.imread('gameimg/55/55.jpg')
numbers = img2arr.img2arr(image,5)
print(numbers)
print(sorted(numbers))

# 将数组中所有元素加1
numbers = [num + 1 for num in numbers]

# 将一维数组转换为二维数组
numbers_2d = [numbers[i:i+5] for i in range(0, len(numbers), 5)]
print(numbers_2d)


# 将数组中所有元素加1
# numbers = [num + 1 for num in numbers]
# 将一维数组转换为二维数组
numbers_2d = [numbers[i:i+9] for i in range(0, len(numbers), 9)]
print(numbers_2d)