import os
import csv
import re

# 定义一个函数来处理单个文件
def process_file(file_path, result):
    with open(file_path, 'r') as f:
        data = f.readlines()

        # 使用正则表达式匹配数据行中的键和值
        for line in data:
            if line.startswith("all") or line.startswith("sway with") or \
            line.startswith("xpln on") or line.startswith("sort with"):
                # 匹配键
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


# 定义一个函数来处理一个文件夹
def process_folder(folder_path):
    data_dict = {'all': {}, 'sway with': {}, 'xpln on': {}, 'sort with': {}}

    for file_name in os.listdir(folder_path):
        if file_name.endswith('.out'):
            file_path = os.path.join(folder_path, file_name)
            process_file(file_path, data_dict)

    return data_dict

# 处理所有文件夹
root_folder = './out2'
auto2_data = {}
for folder_path, _, file_names in os.walk(root_folder):
    folder_name = os.path.basename(folder_path)
    if folder_name == root_folder:
        continue
    folder_name = folder_name.split('.')[0]
    auto2_data[folder_name] = process_folder(folder_path)

# print(auto2_data)

def pretty_print_dict(d, indent=0):
    for key, value in d.items():
        print('\t' * indent + str(key))
        if isinstance(value, dict):
            pretty_print_dict(value, indent + 1)
        else:
            print('\t' * (indent + 1) + str(value))

# 打印结果
pretty_print_dict(auto2_data)