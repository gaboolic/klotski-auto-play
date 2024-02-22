import tensorflow as tf
from tensorflow import keras

# 加载MNIST数据集
mnist = keras.datasets.mnist
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

# 数据预处理
train_images = train_images / 255.0
test_images = test_images / 255.0

# 加载模型
model = keras.models.load_model('lenet5.h5')

# 训练模型
model.fit(train_images, train_labels, epochs=50)

# 保存模型
model.save('lenet5.h5')