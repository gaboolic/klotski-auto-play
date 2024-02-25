import time

import cv2
import numpy as np
from tensorflow import keras

# 加载模型
model = keras.models.load_model('recognition/lenet5.keras')
judge_number_model = keras.models.load_model('recognition/train_number.keras')


def judge_number(image):
    resize_img = cv2.resize(image, (28, 28))  # 调整大小为28x28
    image = resize_img / 255.0  # 归一化
    # 添加批次维度
    image = np.expand_dims(image, axis=0)

    # 进行预测
    predictions = judge_number_model.predict(image)
    # 打印预测结果
    predicted_label = np.argmax(predictions[0])
    cv2.imwrite(f'temp/judge_number_{predicted_label}_{time.time()}.jpg', resize_img)  # 保存图像
    return predicted_label

def one_img(image):
    # 计算平均像素值
    average_pixel_value = cv2.mean(image)[0]

    # 阈值化检查图像是否全黑或全白
    _, binary_image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
    unique_values = cv2.countNonZero(binary_image)

    if average_pixel_value < 10:
        return 99
    elif average_pixel_value > 245:
        return 99

    resize_img = cv2.resize(image, (28, 28))  # 调整大小为28x28
    image = resize_img / 255.0  # 归一化
    # 添加批次维度
    image = np.expand_dims(image, axis=0)

    # 进行预测
    predictions = model.predict(image)
    # 打印预测结果
    predicted_label = np.argmax(predictions[0])
    cv2.imwrite(f'temp/predict_{predicted_label}_{time.time()}.jpg', resize_img)  # 保存图像
    return predicted_label


def img2arr(image,split_count):
    # 获取图像宽度和高度
    height, width, _ = image.shape

    # 定义白色像素的阈值
    white_threshold = 0.8 * height

    # 初始化白色竖线宽度总和
    white_line_width_sum = 0

    # 从右到左，从上到下遍历图像
    for x in range(width - 1, width - 150, -1):
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

    # one_w = 710
    # one_h = 344
    one_w = (roi_width) // split_count
    one_h = (roi_height) // split_count

    image = image[start_y:start_y + height, start_x:start_x + width]
    ori_image = image

    # 将图像转换为灰度图像
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 对图像进行二值化处理
    ret, image = cv2.threshold(image, 150, 255, cv2.THRESH_BINARY )
    # ret, image = cv2.threshold(image, 254, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # 对图像进行形态学操作（可选）
    kernel = np.ones((1, 1), np.uint8)
    image = cv2.morphologyEx(image, cv2.MORPH_ERODE, kernel, iterations=2)

    number_images = []
    for i in range(split_count):
        for j in range(split_count):
            # 计算当前小区域的起始坐标
            start_x = j * (one_w)
            start_y = i * (one_h)

            # 计算当前小区域的中心坐标
            center_x = start_x + one_w // 2
            center_y = start_y + one_h // 2

            # 提取当前小区域的图像
            half_size = 28  # 因为我们想要20像素，所以取一半的大小
            # 提取中心数字图像
            number_image = image[center_y: center_y + half_size, center_x - 14: center_x + 28]
            cv2.imwrite(f'temp/number__{i}_{j}.jpg', number_image)  # 保存图像

            # 存储提取的中心数字图像
            number_images.append(number_image)

    numbers = []
    for idx, num_img in enumerate(number_images):
        # 计算分割位置
        split_point = 21
        # 分割number_image
        part1 = num_img[:, :split_point]
        part2 = num_img[:, split_point:]

        num1 = one_img(part1)
        number = num1
        judge_number_res = judge_number(part2)
        if judge_number_res:
            num2 = one_img(part2)
            number = number*10 + num2
        numbers.append(number)
        cv2.imwrite(f'temp/number_{number}.jpg', num_img)  # 保存图像
    return numbers
