"""
    将一个列表中的每个值乘2并生成新的列表
"""
lst = [1, 2, 3, 4, 5]
new_lst = list(map(lambda x: x * 2, lst))
print(new_lst)
