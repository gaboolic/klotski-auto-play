import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten

# 加载MNIST数据集
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# 数据预处理
x_train, x_test = x_train / 255.0, x_test / 255.0
# 将数据集处理为黑白图像
# x_train = x_train.reshape(x_train.shape[0], 28, 28, 1) / 255.0
# x_test = x_test.reshape(x_test.shape[0], 28, 28, 1) / 255.0


# 构建模型
# model = Sequential([
#     Flatten(input_shape=(28, 28)),
#     Dense(128, activation='relu'),
#     Dense(10, activation='softmax')
# ])
#
# # 编译模型
# model.compile(optimizer='adam',
#               loss='sparse_categorical_crossentropy',
#               metrics=['accuracy'])
# 加载模型
model = keras.models.load_model('lenet5.keras')
# 训练模型
# model.fit(x_train, y_train, epochs=5)

# 评估模型
model.evaluate(x_test, y_test)
