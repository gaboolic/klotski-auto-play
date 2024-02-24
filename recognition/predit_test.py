import tensorflow as tf
from tensorflow import keras
import cv2
import numpy as np

# 加载模型
model = keras.models.load_model('lenet5.keras')

# 加载测试数据集
(_, _), (test_images, test_labels) = keras.datasets.mnist.load_data()
image = test_images[2]
cv2.imwrite('image_mnist.jpg', image)  # 保存图像
# 数据预处理
test_images = test_images / 255.0


image = cv2.resize(image, (28, 28))  # 调整大小为28x28

image = np.expand_dims(image, axis=0)  # 添加批次维度

# 进行预测
predictions = model.predict(image)

# 打印预测结果
predicted_label = np.argmax(predictions[0])
print("Predicted label:", predicted_label)

# todo 评估模型