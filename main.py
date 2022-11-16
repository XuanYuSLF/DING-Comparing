import pandas as pd

# 初始化原表格内容元素
i = 0
df = pd.read_excel("./data/8.xlsx")
name1 = df.iloc[i, 0]

# 初始化待被处理文件元素
j = 0
data = pd.read_table('./data/comparing.txt',
                     sep=',',
                     names=['序列', '名字', '内容'],
                     engine='python',
                     encoding='utf8')
name2 = data.iloc[j, 1]

# 用来判断是否为非表格内容元素
a = 0

# 计算提交人数
number = 0

# 双循环，以待对比元素一一与表格内容元素对比
for i in range(45):
    name1 = df.iloc[i, 0]
    j = 0
    for j in range(data.shape[0]):
        if name1 == name2:
            # 如果该元素不存在于该待对比元素中，则不会经过此代码块，变量a也就为0
            a = 1
            number = number + 1
            name2 = data.iloc[j, 1]
        else:
            name2 = data.iloc[j, 1]
    # 通过判断a的真假，来判断该元素是否存在于待对比元素中
    if a == 1:
        a = 0
    else:
        # 输出非待对比内容元素
        print(name1)

print("已交总人数", number)
