from PIL import Image, ImageDraw, ImageFont
import numpy as np
import random

# 创建白色背景的图像
image = Image.new('L', (28, 28), color=255)
draw = ImageDraw.Draw(image)

# 添加随机黑白块
for _ in range(10):
    x = random.randint(0, 27)
    y = random.randint(0, 27)
    color = random.choice([0, 255])  # 随机选择黑色或白色
    draw.rectangle([x, y, x+2, y+2], fill=color)

# 添加数字
font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Songti.ttc", 44)  # 选择宋体字体
# font = ImageFont.load_default()  # 使用默认字体
draw.text((1, -18), "1", fill=0, font=font)  # 使用黑色（0）绘制数字，位置(8, 8)

# 将图像保存为文件
image.save("sample_image.png")
