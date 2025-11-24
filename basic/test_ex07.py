# -*- coding: UTF-8 -*-

# Filename : test.py
# author by : www.runoob.com

# 生成 0 ~ 9 之间的随机数

# 导入 random(随机数) 模块
import random

print(random.randint(0, 9))

list1 = [1, 2, 3, 4, 5]
random_element = random.choice(list1)
print(random_element)


import random

list1 = [1, 2, 3, 4, 5]
random.shuffle(list1)
print(list1)