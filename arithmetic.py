# -*- coding: utf-8 -*-
__author__ = 'YongCong Wu'
# @Time    : 2019/4/16 16:17
# @Email   :  : 1922878025@qq.com

# 算术运算符

start_num = 10
end_num = 15

plus = start_num + end_num              # 加
print(plus)

less = end_num - start_num              # 减
print(less)

multiply = start_num * end_num          # 乘
print(multiply)

numexcept = start_num / end_num         # 除
print(numexcept)

mo = start_num % end_num                # 取模
print(mo)

mi = start_num ** end_num               # 取幂
print(min)

intNum = start_num // end_num           # 取整数
print(intNum)

# 比较运算

dengyu = start_num == end_num           # 等于等于，  一个=是赋值， 两个==是比较
print(dengyu)

budengyu = start_num != end_num         # 不等于
print(budengyu)

dayu = start_num > end_num              # 大于
print(dayu)

xiaoyu = start_num < end_num            # 小于
print(xiaoyu)

dadengyu = start_num >= end_num         # 大于等于
print(dadengyu)

xiaodengyu = start_num <= end_num       # 小于等于
print(xiaodengyu)

# 赋值运算
result = start_num                      # 赋值
print(result)

start_num += end_num                    # 加等于

end_num -= start_num                    # 减等于

start_num *= end_num                    # 乘等于

end_num /= start_num                    # 除等于

start_num %= end_num                    # 取模赋值

start_num **= end_num                   # 求幂赋值

start_num //= end_num                   # 取整数赋值

# 逻辑运算

if start_num == 10 and end_num == 15:       # 两个条件都为真，才继续往下执行。
    print(True)                 # True
else:
    print(False)


if start_num == 10 or end_num == 15:        # 有一个为真，继续往下执行。
    print(True)
else:
    print(False)


listNum = [1, 2, 3, 4]
if 2 not in listNum:       # 如果2在listNum列表里边，就为False，不在为True
    print(True)
else:
    print(False)

