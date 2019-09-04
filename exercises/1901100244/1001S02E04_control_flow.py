# -*- coding: UTF-8 -*-

# Filename : 1001S02E04_control_flow.py
# author by : @shen-huang

# 打印两种九九乘法表

# 任务原始要求

# 使用 for...in 循环打印九九乘法表

for i in range(1, 10):
    for j in range(1, 10):
        if j <= i:
            print("{0}*{1}={2}".format(i, j, i*j), end='   ')
    print()
print()

# 使用 while 循环打印九九乘法表并用条件判断把偶数行去掉

a = 1
while (a < 10):
    b = 1
    while b <= a:
        if a % 2 != 0:
            print("{}*{}={}".format(a, b, a*b), end='   ')
            b += 1
        else:
            print()
            break
    a += 1
print()

print()
print("――――――――――――――――――――――――――――――――――――――――")
print()

# 任务其他尝试

# 使用符合标准的乘号（×）

# 修改为常见的九九表呈现方式

for i in range(1, 10):
    for j in range(1, 10):
        if j <= i:
            print("{0}×{1}={2}".format(j, i, i*j), end='\t')
    print()
print()

# 修改为另一种方向的九九表呈现方式

for i in range(1, 10):
    for j in range(1, 10):
        if i > j:
            print("     ", end='\t')
        else:
            print("{0}×{1}={2}".format(i, j, i*j), end='\t')
    print()
print()

# 不同的循环方式

for i in range(1, 10):
    while i % 2 != 0:
        for j in range(1, 10):
            if j <= i:
                print("{0}×{1}={2}".format(i, j, i*j), end='\t')
        print()
        break
print()

# 不同的循环方式，会出现空行

a = 1
while (a < 10):
    b = 1
    while b <= a:
        if a % 2 != 0:
            print(a, '×', b, '=', a*b, sep='', end='\t')
            b += 1
        else:
            break
    a += 1
    print()
print()

# 不同的循环方式，避免了空行，逻辑相对更清晰

a = 1
while (a < 10):
    b = 1
    if a % 2 != 0:
        while b <= a:
            print(a, '×', b, '=', a*b, sep='', end='\t')
            b += 1
        print()
        a += 1
    else:
        a += 1
print()

# 不同的循环方式，避免了空行，代码相对更简洁

a = 0
while (a < 10):
    a += 1
    b = 1
    if a % 2 != 0:
        while b <= a:
            print(a, '×', b, '=', a*b, sep='', end='\t')
            b += 1
        print()
    else:
        continue
print()

# 考虑该表可能的实际用途，去掉了两数大小判断

for i in range(1, 10):
    while i % 2 != 0:
        for j in range(1, 10):
            print("{0}×{1}={2}".format(j, i, i*j), end='\t')
        print()
        break
print()

# 不同的循环方式，省去了两数大小判断

for i in range(1, 10):
    for j in range(1, i+1):
        print("{0}×{1}={2}".format(j, i, i*j), end='\t')
    print()
print()

for i in range(1, 10):
    while i % 2 != 0:
        for j in range(1, i+1):
            print("{0}×{1}={2}".format(j, i, i*j), end='\t')
        print()
        break
print()

# 不同的循环方式，省去了条件判断（while）

for i in [1, 3, 5, 7, 9]:
    for j in range(1, i+1):
        print("{0}×{1}={2}".format(j, i, i*j), end='\t')
    print()
print()

# 不同的循环方式，使用了 if

for i in range(1, 10):
    if i % 2 != 0:
        for j in range(1, i+1):
            print("{0}×{1}={2}".format(j, i, i*j), end='\t')
        print()
print()

# 不同的循环方式，使用了 continue

for i in range(1, 10):
    if i % 2 == 0:
        continue
    else:
        for j in range(1, i+1):
            print("{0}×{1}={2}".format(j, i, i*j), end='\t')
        print()
print()
