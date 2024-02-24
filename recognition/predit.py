import tensorflow as tf
from tensorflow import keras
import cv2
import numpy as np

# 加载模型
model = keras.models.load_model('lenet5.keras')

# 读取图像并进行预处理
image = cv2.imread('../number_0.jpg', cv2.IMREAD_GRAYSCALE)  # 以灰度图像方式读取
# image = cv2.imread('sample_image.png', cv2.IMREAD_GRAYSCALE)  # 以灰度图像方式读取

image = cv2.resize(image, (28, 28))  # 调整大小为28x28
cv2.imwrite('image.jpg', image)  # 保存图像
image = image / 255.0  # 归一化

# 添加批次维度
image = np.expand_dims(image, axis=0)

# 进行预测
predictions = model.predict(image)
print(predictions)
# 打印预测结果
predicted_label = np.argmax(predictions[0])
print("Predicted label:", predicted_label)