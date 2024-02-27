from klotski import klotski99

numbers = [0, 1, 2, 3, 5, 7, 25, 16, 8, 9, 10, 11, 99, 39, 14, 26, 15, 17, 18, 20, 21, 4, 12, 6, 32, 24, 35, 28, 19, 49, 30, 31, 40, 13, 34, 44, 45, 36, 29, 41, 22, 33, 23, 43, 53, 27, 72, 38, 56, 50, 68, 42, 51, 62, 37, 54, 48, 47, 55, 67, 61, 69, 79, 46, 64, 65, 66, 59, 57, 58, 71, 52, 73, 63, 75, 76, 74, 78, 77, 60, 70]
# 151.8437054157257秒

# 慢
# numbers = [21, 20, 1, 2, 3, 4, 5, 7, 8, 9, 0, 40, 18, 12, 14, 16, 25, 17, 19, 11, 10, 29, 6, 22, 23, 15, 35, 28, 36, 31, 39, 13, 24, 42, 43, 33, 45, 27, 37, 48, 30, 58, 34, 26, 44, 54, 46, 38, 57, 51, 41, 32, 52, 53, 55, 56, 47, 99, 50, 49, 60, 61, 62, 63, 64, 65, 66, 67, 59, 68, 69, 70, 72, 73, 74, 75, 76, 77, 78, 79, 71]

steps = klotski99.get_path_warp(numbers)