import os
import csv
import random

# 设置随机修改数据的百分比
percent_to_modify = 5

# 定义函数，用于读取CSV文件并随机修改数据
def process_csv(input_file, output_file):
    # 打开输入文件和输出文件
    with open(input_file, 'r', newline='') as f_input, open(output_file, 'w', newline='') as f_output:
        # 创建CSV reader和writer
        csv_reader = csv.reader(f_input, delimiter=',')
        csv_writer = csv.writer(f_output, delimiter=',')
        
        # 读取第一行，即列名
        headers = next(csv_reader)
        
        # 判断哪些列不需要修改
        columns_to_skip = set()
        for i, header in enumerate(headers):
            if header.endswith('+') or header.endswith('-'):
                columns_to_skip.add(i)
        
        # 写入列名
        csv_writer.writerow(headers)
        
        # 遍历每一行数据，进行随机修改
        for row in csv_reader:
            modified_row = []
            for i, value in enumerate(row):
                # 判断该列是否需要跳过
                if i in columns_to_skip:
                    modified_row.append(value)
                    continue
                
                # 判断是否需要修改该行数据
                if random.randint(1, 100) <= percent_to_modify:
                    modified_row.append('?')
                else:
                    modified_row.append(value)
            
            # 写入修改后的行数据
            csv_writer.writerow(modified_row)

# 获取输入文件夹中所有CSV文件的路径
input_dir = './etc/data/origin'
input_files = [os.path.join(input_dir, f) for f in os.listdir(input_dir) if f.endswith('.csv')]

# 遍历每个CSV文件，进行处理并保存到输出文件夹
output_dir = './etc/data/highnoise'
os.makedirs(output_dir, exist_ok=True)
for input_file in input_files:
    output_file = os.path.join(output_dir, os.path.basename(input_file))
    process_csv(input_file, output_file)
