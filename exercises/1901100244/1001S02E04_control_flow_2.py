# -*- coding: UTF-8 -*-

# Filename : 1001S02E04_control_flow_2.py
# author by : @shen-huang
# reference : [Python:文件的读取、创建、追加、删除、清空]
#             (https://blog.csdn.net/u010281626/article/details/53908099)
#             [Python print 输出到文件]
#             (https://blog.csdn.net/yageeart/article/details/38386121)
#             [Python 读取文件的三种方式]
#             (https://zhuanlan.zhihu.com/p/42784651)
#             [Python 指定编码格式创建、打开文件]
#             (https://blog.csdn.net/damys/article/details/79352410)

# 使用 while 循环打印九九乘法表并用条件判断把偶数行去掉

import os

# 原始输出会出现空行，故新建一个文件，重定向输出，再去掉多余的空行

# 新建一个文件

f = open('f_temp.txt', 'w', encoding='utf-8')

# 会出现空行的输出，将其重定向，存入文件

i = 1
while (i < 10):
    if i % 2 != 0:
        j = 1
        while j <= i:
            print(j, '×', i, '=', i*j, sep='', end='\t', file=f)
            j += 1
    i += 1
    print(file=f)
print(file=f)

# 关闭文件

f.close()

# 打开文件，去掉多余的空行并输出，关闭文件

f = open('f_temp.txt', encoding='utf-8')

print(f.read().replace('\n\n', '\n'))

f.close()

# 删除文件

os.remove('f_temp.txt')
