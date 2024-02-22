import uiautomator2 as u2

d = u2.connect() # connect to device
print(d.info)
print(d.serial) #BEWOOZNBYLFYQWHA
d.screenshot("home.jpg")

# 读取图像
image = cv2.imread('game.jpg')