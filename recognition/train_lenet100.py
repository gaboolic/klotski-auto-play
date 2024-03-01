import os
import tensorflow as tf
from tensorflow import keras
import cv2
import numpy as np

def translate_image(image, tx_range, ty_range):
    tx = np.random.randint(-tx_range, tx_range + 1)
    ty = np.random.randint(-ty_range, ty_range + 1)

    rows, cols = image.shape
    M = np.float32([[1, 0, tx], [0, 1, ty]])
    translated_image = cv2.warpAffine(image, M, (cols, rows))

    return translated_image

train_images = []
train_labels = []
for i in range(100):
    # 读取图像并进行预处理
    path = f'../number_template/{i}/'
    print(path)
    # 读取path下所有图片
    files = os.listdir(path)
    # 筛选出所有以'.jpg'或'.png'结尾的文件
    image_files = [f for f in files if f.endswith('.jpg') or f.endswith('.png')]

    # 打印所有图片文件名
    for image_file in image_files:
        print(image_file)
        image = cv2.imread(path + image_file, cv2.IMREAD_GRAYSCALE)  # 以灰度图像方式读取
        image = cv2.resize(image, (28, 28))  # 调整大小为28x28

        # 随机平移图像
        tx_range = 0  # x轴平移范围
        ty_range = 0  # y轴平移范围
        # image = translate_image(image, tx_range, ty_range)

        image = image / 255.0  # 归一化
        train_images.append(image)
        train_labels.append(i)

train_images = np.array(train_images)
train_labels = np.array(train_labels)

# 加载模型
model = keras.models.load_model('lenet5_100.keras')

# 训练模型
model.fit(train_images, train_labels, epochs=600)

# 保存模型
model.save('lenet5_100.keras')
