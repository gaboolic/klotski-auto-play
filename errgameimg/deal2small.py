import uuid
import os
import cv2
import numpy as np

def img2small(image):
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
    start_y = 21
    end_x = 147
    end_y = 21

    roi_width = width - start_x - end_x
    roi_height = height - start_y - end_y

    split_count = 3
    # one_w = 710
    # one_h = 344
    one_w = (roi_width) // split_count
    one_h = (roi_height) // split_count

    image = image[start_y:start_y + height, start_x:start_x + width]
    ori_image = image

    # 将图像转换为灰度图像
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 对图像进行二值化处理
    # ret, image = cv2.threshold(image, 240, 255, cv2.THRESH_BINARY )
    ret, image = cv2.threshold(image, 254, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # 对图像进行形态学操作（可选）
    kernel = np.ones((1, 1), np.uint8)
    image = cv2.morphologyEx(image, cv2.MORPH_ERODE, kernel, iterations=2)

    number_images = []
    for i in range(3):
        for j in range(3):
            # 计算当前小区域的起始坐标
            start_x = j * one_w
            start_y = i * one_h

            # 计算当前小区域的中心坐标
            center_x = start_x + one_w // 2
            center_y = start_y + one_h // 2

            # 提取当前小区域的图像
            half_size = 28  # 因为我们想要20像素，所以取一半的大小
            # 提取中心数字图像
            number_image = image[center_y: center_y + half_size, center_x - 14: center_x + 14]

            # 存储提取的中心数字图像
            number_images.append(number_image)

    numbers = []
    for idx, num_img in enumerate(number_images):
        new_uuid = uuid.uuid4()
        cv2.imwrite(f'../todosmall/number_{new_uuid}.jpg', num_img)  # 保存图像

# 读取图像并进行预处理
path = './'
# 读取path下所有图片
files = os.listdir(path)
# 筛选出所有以'.jpg'或'.png'结尾的文件
image_files = [f for f in files if f.endswith('.jpg') or f.endswith('.png')]

# 打印所有图片文件名
for image_file in image_files:
    print(image_file)
    image = cv2.imread(path + image_file)
    img2small(image)