# 课程回顾：if else用法 判断语句 in 和 ==
# 测试：

# 垃圾分类器 v1.0
""" 程序要求：
1.有害垃圾：锂电池
2.可回收：作业纸、塑料
3.厨房垃圾：鱼骨、鸡蛋壳、大棒骨
4.其他垃圾：渣土、污染纸

用户输入以上要扔的垃圾，程序输出对应的垃圾类型。
"""


# if else 中的嵌套结构（分支结构）
# 数据判断器
# 定义一个数字变量，当数字大于1时，继续判断数字是否大于5，如果大于5，输出“大于1且大于5”，如果小于5，输出“大于1且小于5”。否则输出"小于等于1"。

number = 0
if number > 1:
    print("number 大于 1")
    if number > 5:
        print("number 大于1且大于5")
    else:
        print("number 仅大于1且小于5")
else:
    print("number 小于等于1")


# if elif else 用法
# 体重的算法
# 定义一个体重的变量，使用if elif else 让体重在不同区间时做出对应的输出
weight = 80 
if weight > 40 and weight < 50:
    print("体重小于50公斤，过轻")
elif weight > 50 and weight < 70:
    print("体重在 50 ~ 70 公斤之间，标准体重")
elif weight > 70:
    print("体重大于70公斤，过胖")
else:
    print("不正常的体重")

# if else 和 if elif else区别（演示重点）：
weight = 80 
if weight > 40 and weight < 50:
    print("体重小于50公斤，过轻")
elif weight > 50 and weight < 70:
    print("体重在 50 ~ 70 公斤之间，标准体重")
elif weight > 70:
    print("体重大于70公斤，过胖")
elif weight > 40:
    print("这段代码不会执行")
else:
    print("不正常的体重")
