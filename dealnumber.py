import cv2
import numpy as np

# 读取图像
# image = cv2.imread('errgameimg/game2.jpg')
image = cv2.imread('errgameimg/number_0e67ce2a-8154-4f7c-ab1e-8faa23900a8d.jpg')
# image = cv2.imread('gameimg/99/99.jpg')

# 获取图像宽度和高度
height, width, _ = image.shape

# 定义白色像素的阈值
white_threshold = 0.8 * height

# 初始化白色竖线宽度总和
white_line_width_sum = 0

# 从右到左，从上到下遍历图像
for x in range(width-1, width-150, -1):
    white_pixel_count = 0
    for y in range(height):
        if (image[y, x] == 255).all():
            white_pixel_count += 1
    if white_pixel_count >= white_threshold:
        white_line_width_sum += 1

print("白色竖线总宽度：", white_line_width_sum)

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
# end_x = 132
end_x = white_line_width_sum
end_y = 21

roi_width = width - start_x - end_x
roi_height = height - start_y - end_y

split_count = 3
# one_w = 710
# one_h = 344
one_w = (roi_width) // split_count
one_h = (roi_height) // split_count

image = image[start_y:start_y + roi_height, start_x:start_x + roi_width]
ori_image = image
cv2.imwrite('temp/roi.jpg', image)

# 将图像转换为灰度图像
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 或保存结果图像
cv2.imwrite('temp/gray.jpg', image)

# 对图像进行二值化处理
ret, image = cv2.threshold(image, 150, 255, cv2.THRESH_BINARY )
# ret, image = cv2.threshold(image, 254, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
# 或保存结果图像
cv2.imwrite('temp/thresh.jpg', image)

# 对图像进行形态学操作（可选）
kernel = np.ones((1, 1), np.uint8)
image = cv2.morphologyEx(image, cv2.MORPH_ERODE, kernel, iterations=2)
cv2.imwrite('temp/closing.jpg', image)

little_images = []
for i in range(split_count):
    for j in range(split_count):
        # 计算当前小区域的起始坐标
        start_x = j * (one_w)
        start_y = i * (one_h)

        # 提取中心数字图像
        number_image = image[start_y: start_y + one_h, start_x: start_x + one_w]

        # 存储提取的中心数字图像
        little_images.append(number_image)

for idx, num_img in enumerate(little_images):
    cv2.imwrite(f'temp/little_{idx}.jpg', num_img)  # 保存图像

number_images = []
for i in range(split_count):
    for j in range(split_count):
        # 计算当前小区域的起始坐标
        start_x = j * one_w
        start_y = i * one_h

        # 计算当前小区域的中心坐标
        center_x = start_x + one_w // 2
        center_y = start_y + one_h // 2

        # 提取当前小区域的图像
        half_size = 28  # 因为我们想要20像素，所以取一半的大小
        # 提取中心数字图像
        number_image = image[center_y: center_y + half_size, center_x -14: center_x + 14]

        # 存储提取的中心数字图像
        number_images.append(number_image)

for idx, num_img in enumerate(number_images):
    cv2.imwrite(f'temp/number_{idx}.jpg', num_img)  # 保存图像
