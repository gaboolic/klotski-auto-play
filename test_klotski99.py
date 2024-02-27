from klotski import klotski99

numbers = [0, 1, 2, 3, 5, 7, 25, 16, 8, 9, 10, 11, 99, 39, 14, 26, 15, 17, 18, 20, 21, 4, 12, 6, 32, 24, 35, 28, 19, 49,
           30, 31, 40, 13, 34, 44, 45, 36, 29, 41, 22, 33, 23, 43, 53, 27, 72, 38, 56, 50, 68, 42, 51, 62, 37, 54, 48,
           47, 55, 67, 61, 69, 79, 46, 64, 65, 66, 59, 57, 58, 71, 52, 73, 63, 75, 76, 74, 78, 77, 60, 70]
# 151.8437054157257秒
# 91.57500386238098秒
# 5.013743162155151秒
# 9.509095907211304秒
# 7.042182922363281秒

#numbers = [21, 20, 1, 2, 3, 4, 5, 7, 8, 9, 0, 40, 18, 12, 14, 16, 25, 17, 19, 11, 10, 29, 6, 22, 23, 15, 35, 28, 36, 31, 39, 13, 24, 42, 43, 33, 45, 27, 37, 48, 30, 58, 34, 26, 44, 54, 46, 38, 57, 51, 41, 32, 52, 53, 55, 56, 47, 99, 50, 49, 60, 61, 62, 63, 64, 65, 66, 67, 59, 68, 69, 70, 72, 73, 74, 75, 76, 77, 78, 79, 71]
# 18.806761026382446秒
# 20.898056030273438秒
# 72.39168286323547秒
# 13.048104047775269秒

# 慢
# numbers = [0, 1, 2, 3, 14, 5, 6, 15, 8, 9, 10, 11, 4, 31, 7, 33, 13, 26, 18, 19, 21, 12, 30, 23, 35, 16, 24, 27, 28, 20, 29, 40, 22, 25, 34, 17, 36, 37, 39, 48, 49, 32, 50, 52, 42, 45, 46, 38, 67, 41, 57, 59, 53, 43, 54, 55, 47, 99, 68, 58, 70, 44, 61, 63, 64, 56, 66, 60, 69, 78, 51, 62, 72, 73, 65, 75, 74, 76, 77, 79, 71]
# 26.121688842773438秒
# 27.186790943145752秒
# 98.94178318977356秒
# 14.906550884246826秒
# 4.032459020614624秒

# numbers = [0, 12, 1, 2, 3, 14, 6, 7, 8, 20, 36, 21, 11, 5, 4, 15, 16, 17, 9, 29, 10, 13, 22, 23, 24, 25, 26, 19, 18, 37, 30, 31, 32, 33, 35, 44, 27, 47, 28, 57, 39, 41, 42, 34, 53, 45, 46, 38, 56, 64, 50, 52, 43, 62, 63, 54, 72, 67, 66, 59, 51, 61, 70, 75, 48, 65, 74, 58, 40, 68, 78, 79, 99, 55, 49, 73, 76, 77, 60, 69, 71]
# 15.028950929641724秒

steps = klotski99.get_path_warp(numbers)

print(len(steps))
print(steps)

print("打印移动")
current_state = numbers
for path in steps:
    index = path
    zero_index = current_state.index(99)
    current_state[zero_index] = current_state[index]
    current_state[index] = 99
print(current_state)

expect_result = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27,
                 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53,
                 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79,
                 99]
if current_state == expect_result:
    print("移动正确")
else:
    print("移动错误")
