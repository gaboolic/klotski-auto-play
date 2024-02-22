import cv2
import numpy as np
from tensorflow import keras

# 加载模型
model = keras.models.load_model('recognition/lenet5.h5')


def one_img(image):
    # 计算平均像素值
    average_pixel_value = cv2.mean(image)[0]

    # 阈值化检查图像是否全黑或全白
    _, binary_image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
    unique_values = cv2.countNonZero(binary_image)

    if average_pixel_value < 10:
        return 8
    elif average_pixel_value > 245:
        return 8

    image = cv2.resize(image, (28, 28))  # 调整大小为28x28
    image = image / 255.0  # 归一化
    # 添加批次维度
    image = np.expand_dims(image, axis=0)

    # 进行预测
    predictions = model.predict(image)
    # 打印预测结果
    predicted_label = np.argmax(predictions[0])
    return predicted_label


def img2arr(image):
    one_w = 710
    one_h = 344
    start_x = 120
    start_y = 23

    width = one_w * 3  # 区域宽度
    height = one_h * 3  # 区域高度

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
        numbers.append(one_img(num_img))
    return numbers
