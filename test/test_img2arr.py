import time

import cv2
import uiautomator2 as u2

from recognition import img2arr, img2arr_dev
from klotski import klotski99
import unittest


class TestMyModule(unittest.TestCase):

    def test1(self):
        # 读取图像
        image = cv2.imread('../game2.jpg')

        recognition_start_time = time.time()
        numbers = img2arr_dev.img2arr(image, 9)
        recognition_end_time = time.time()
        print(f"图片识别耗时{recognition_end_time - recognition_start_time}秒")

        # numbers = [0, 1, 2, 4, 13, 5, 6, 7, 8, 18, 9, 11, 3, 22, 25, 33, 16, 17, 10, 20, 28, 12, 24, 14, 15, 35, 34, 39, 27, 21,
        #            32, 30, 51, 23, 26, 43, 19, 29, 47, 46, 31, 41, 50, 59, 44, 36, 45, 37, 38, 68, 61, 42, 77, 53, 54, 55, 74,
        #            56, 49, 40, 66, 58, 62, 63, 64, 75, 48, 67, 78, 57, 70, 79, 72, 73, 99, 65, 76, 69, 60, 52, 71]

        print(numbers)
        sorted_numbers = sorted(numbers)
        print(sorted_numbers)

        split_count = 9
        given_array = list(range(0, split_count * split_count - 1))
        given_array.append(99)

        self.assertEqual(sorted_numbers, given_array)
        # 检查排序后的数组是否等于给定数组
