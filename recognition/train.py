import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers, models

# 加载MNIST数据集
mnist = keras.datasets.mnist
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

# 数据预处理
train_images = train_images / 255.0
test_images = test_images / 255.0


# 定义LeNet-5模型结构
def LeNet5(input_shape=(28, 28, 1), num_classes=20):
    model = models.Sequential()

    model.add(layers.Conv2D(6, kernel_size=(5, 5), strides=(1, 1), activation='tanh', input_shape=input_shape,
                            padding='same'))
    model.add(layers.AveragePooling2D(pool_size=(2, 2), strides=(2, 2)))

    model.add(layers.Conv2D(16, kernel_size=(5, 5), strides=(1, 1), activation='tanh', padding='valid'))
    model.add(layers.AveragePooling2D(pool_size=(2, 2), strides=(2, 2)))

    model.add(layers.Conv2D(120, kernel_size=(5, 5), strides=(1, 1), activation='tanh', padding='valid'))

    model.add(layers.Flatten())
    model.add(layers.Dense(84, activation='tanh'))

    model.add(layers.Dense(num_classes, activation='softmax'))

    return model


# 构建LeNet-5模型
model = LeNet5()

# 打印模型结构
model.summary()

# 编译模型
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# 训练模型
model.fit(train_images, train_labels, epochs=5)

# 保存模型
model.save('lenet5_20.keras')
