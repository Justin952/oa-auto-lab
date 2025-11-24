# Filename: quadratic_solver.py
# Author: www.runoob.com (优化 by ChatGPT)

# 程序功能: 求解二次方程 ax**2 + bx + c = 0
# 注意: a ≠ 0，a、b、c 为用户输入的实数

import cmath  # 导入 cmath 模块，支持复数运算


def get_float_input(prompt):
    """
    获取用户输入的浮点数，并处理非法输入。
    :param prompt: 提示信息
    :return: 用户输入的浮点数
    """
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("请输入有效的数字！")


def solve_quadratic(a, b, c):
    """
    计算二次方程的解。
    :param a: 二次项系数
    :param b: 一次项系数
    :param c: 常数项
    :return: 二次方程的两个解
    """
    discriminant = b ** 2 - 4 * a * c  # 计算判别式
    root1 = (-b - cmath.sqrt(discriminant)) / (2 * a)
    root2 = (-b + cmath.sqrt(discriminant)) / (2 * a)
    return root1, root2


def main():
    print("求解二次方程 ax^2 + bx + c = 0")

    # 获取用户输入
    a = get_float_input("请输入二次项系数 a（a ≠ 0）：")
    while a == 0:
        print("二次方程的二次项系数 a 不能为 0！")
        a = get_float_input("请重新输入二次项系数 a（a ≠ 0）：")

    b = get_float_input("请输入一次项系数 b：")
    c = get_float_input("请输入常数项 c：")

    # 计算并输出结果
    root1, root2 = solve_quadratic(a, b, c)
    print(f"方程的解为：{root1} 和 {root2}")


if __name__ == "__main__":
    main()