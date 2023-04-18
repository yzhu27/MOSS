#!/bin/bash

# 设置数据文件夹路径
data_dir="../etc/data"

# 设置输出文件夹路径
out_dir="../etc/out"

# 查找数据文件夹下的所有csv文件
csv_files=$(find "$data_dir" -type f -name "*.csv")

# 循环遍历每个csv文件
for file in $csv_files
do
    # 获取相对路径
    relative_path=$(realpath --relative-to="$data_dir" "$file")

    # 创建相应的输出文件夹
    out_path="$out_dir/$relative_path"
    mkdir -p "$(dirname "$out_path")"
    # 执行lua脚本，并将输出保存到对应的.out文件
    lua5.3 ./xpln/xpln.lua -f "$file" -g xpln > "$out_path.out"
    echo "Complete output on $file"
done
