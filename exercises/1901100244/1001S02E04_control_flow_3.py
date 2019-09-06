# -*- coding: UTF-8 -*-

# Filename : 1001S02E04_control_flow_3.py
# author by : @shen-huang
# reference : [Python 3 print 重定向输出的几种方法]
#             (https://blog.csdn.net/qq_35528593/article/details/74453104)
#             [Python 3 进阶 —— print 打印和输出]
#             (https://shockerli.net/post/python3-print/)

# 使用 while 循环打印九九乘法表并用条件判断把偶数行去掉

import sys

# 原始输出会出现空行，故构造一个类，重定向输出，再去掉多余的空行


class FakeOut:

    def __init__(self):
        self.str = ''
        self.n = 0

    def write(self, s):
        self.str += s
        self.n += 1

    def show(self):  # 显示函数，非必须
        print(self.str)

    def clear(self):  # 清空函数，非必须
        self.str = ''
        self.n = 0


# 修改标准输出实现重定向

f_out = FakeOut()

std_out = sys.stdout
sys.stdout = f_out

# 会出现空行的输出

i = 1
while (i < 10):
    if i % 2 != 0:
        j = 1
        while j <= i:
            print(j, '×', i, '=', i*j, sep='', end='\t')
            j += 1
    i += 1
    print()
print()

# 恢复标准输出

sys.stdout = std_out

# 去掉多余的空行并输出

print(f_out.str.replace("\n\n", "\n"))
