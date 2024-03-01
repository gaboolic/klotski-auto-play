import time

from klotski import klotski99
from klotski import klotski99_sllm
import unittest


class TestKlotski99Dev(unittest.TestCase):

    def common_method(self, numbers):
        expect_result = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,
                         26, 27,
                         28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51,
                         52, 53,
                         54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77,
                         78, 79, 80,
                         0]

        start_time = time.time()

        # 将一维数组转换为二维数组
        numbers_2d = [numbers[i:i + 9] for i in range(0, len(numbers), 9)]
        expect_result_2d = [expect_result[i:i + 9] for i in range(0, len(expect_result), 9)]

        steps = klotski99_sllm.get_path(numbers_2d, expect_result_2d)
        end_time = time.time()

        print(f"耗时{end_time - start_time}秒")
        print(len(steps))
        print(steps)

        print("打印移动")
        current_state = numbers
        for path in steps:
            index = path
            zero_index = current_state.index(0)
            current_state[zero_index] = current_state[index]
            current_state[index] = 0
        print(current_state)

        self.assertEqual(current_state, expect_result)

    def test1(self):
        numbers = [13, 20, 60, 46, 38, 71, 14, 21, 17, 1, 47, 8, 69, 65, 70, 73, 50, 51, 3, 10, 58, 35, 55, 76, 77, 59,
                   80, 26, 36, 6, 27, 24, 54, 31, 43, 62, 25, 34, 66, 61, 67, 30, 5, 11, 7, 15, 56, 29, 4, 78, 44, 16,
                   74, 63, 19, 45, 79, 68, 64, 33, 12, 9, 40, 2, 18, 39, 53, 41, 72, 0, 57, 37, 48, 28, 75, 42, 52, 49,
                   22, 23, 32]

        self.common_method(numbers)
