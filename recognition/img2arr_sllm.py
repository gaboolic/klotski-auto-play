import time

import cv2
import numpy as np
from tensorflow import keras

# 加载模型
lenet5_100_model = keras.models.load_model('recognition/lenet5_100.keras')


def one_img(image):
    # 计算平均像素值
    average_pixel_value = cv2.mean(image)[0]

    # 阈值化检查图像是否全黑或全白
    _, binary_image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
    unique_values = cv2.countNonZero(binary_image)

    if average_pixel_value < 10:
        return 0
    elif average_pixel_value > 245:
        return 0

    resize_img = cv2.resize(image, (28, 28))  # 调整大小为28x28
    image = resize_img / 255.0  # 归一化
    # 添加批次维度
    image = np.expand_dims(image, axis=0)

    # 进行预测
    predictions = lenet5_100_model.predict(image)
    # 打印预测结果
    predicted_label = np.argmax(predictions[0])
    cv2.imwrite(f'temp/predict_{predicted_label}_{time.time()}.jpg', resize_img)  # 保存图像
    return predicted_label


def img2arr(image, split_count):
    # 获取图像宽度和高度
    height, width, _ = image.shape

    width = 1080
    height = 2400

    # 100 100
    start_x = 19
    start_y = 666

    one_w = 1062 // 9 - 20
    one_h = 1062 // 9 - 20

    image = image[start_y:start_y + 120 * 9 - 20, start_x:start_x + 120 * 9 - 20]
    cv2.imwrite('temp/roi.jpg', image)

    # 将图像转换为灰度图像
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 对图像进行二值化处理
    ret, image = cv2.threshold(image, 150, 255, cv2.THRESH_BINARY)
    # ret, image = cv2.threshold(image, 254, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # 对图像进行形态学操作（可选）
    kernel = np.ones((1, 1), np.uint8)
    image = cv2.morphologyEx(image, cv2.MORPH_ERODE, kernel, iterations=2)

    number_images = []
    for i in range(split_count):
        for j in range(split_count):
            # 计算当前小区域的起始坐标
            start_x = j * (one_w + 20)
            start_y = i * (one_h + 20)
            # 98
            # 54
            half = 22
            # 提取中心数字图像
            number_image = image[start_y+22: start_y + one_h-22, start_x+22: start_x + one_w-22]
            cv2.imwrite(f'temp/number__{i}_{j}.jpg', number_image)  # 保存图像

            # 存储提取的中心数字图像
            number_images.append(number_image)

    numbers = []
    for idx, num_img in enumerate(number_images):
        number = one_img(num_img)
        numbers.append(number)
        cv2.imwrite(f'temp_number/number_{number}_{time.time()}.jpg', num_img)  # 保存图像
    return numbers
