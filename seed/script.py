import re

# 打开文件并逐行读取数据
with open("./out2/auto2.csv/937162217.out", "r") as f:
    data = f.readlines()

# 初始化字典
result = {"all": {}, "sway with": {}, "xpln on": {}, "sort with": {}}

# 使用正则表达式匹配数据行中的键和值
for line in data:
    if line.startswith("all") or line.startswith("sway with") or \
       line.startswith("xpln on") or line.startswith("sort with"):
        # 匹配键
        key = re.findall(r":\w+\s*(\+|-)?", line)
        key = [k.strip(":") for k in key]
        key = ['CityMPG+_mean','Class-_mean','HighwayMPG+_mean','N_mean','Weight-_mean','CityMPG+_div','Class-_div','HighwayMPG+_div','N_div','Weight-_div']
        # 匹配值
        value = re.findall(r"[-+]?\d*\.\d+|\d+", line)
        value = [float(v) for v in value]
        # 存储在相应的字典中
        if line.startswith("all"):
            for i, k in enumerate(key):
                if k not in result["all"]:
                    result["all"][k] = []
                result["all"][k].append(value[i])
        elif line.startswith("sway with"):
            for i, k in enumerate(key):
                if k not in result["sway with"]:
                    result["sway with"][k] = []
                result["sway with"][k].append(value[i])
        elif line.startswith("xpln on"):
            for i, k in enumerate(key):
                if k not in result["xpln on"]:
                    result["xpln on"][k] = []
                result["xpln on"][k].append(value[i])
        elif line.startswith("sort with"):
            for i, k in enumerate(key):
                if k not in result["sort with"]:
                    result["sort with"][k] = []
                result["sort with"][k].append(value[i])

# 输出结果
print(result['all'])
