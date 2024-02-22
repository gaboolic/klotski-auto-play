import uiautomator2 as u2

# d = u2.connect() # connect to device
d = u2.connect_wifi('192.168.1.3') # connect to device
print(d.info)
print(d.serial) #BEWOOZNBYLFYQWHA
# d.screenshot("home.jpg")
d.click(0.178, 0.49)
