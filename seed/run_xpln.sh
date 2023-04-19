#!/bin/bash

# 设置数据文件夹路径
data_dir="./data"

# 设置输出文件夹路径
out_dir="./out2"

# 定义随机数种子数组
seeds=(937162217 937162249 937162267 937162273 937162321 937162361 937162363 937162367 937162397 937162399 937162423 937162453 937162507 937162607 937162649 937162651 937162661 937162691 937162693 937162729)

# 循环遍历每个随机数种子
for seed in "${seeds[@]}"
do
    # 循环遍历每个csv文件
    csv_files=$(find "$data_dir" -type f -name "*.csv")
    for file in $csv_files
    do
        # 获取相对路径
        relative_path=$(realpath --relative-to="$data_dir" "$file")
        # 创建相应的输出文件夹
        out_path="$out_dir/$relative_path"
        mkdir -p "$out_dir/$(basename "$file")"

        # 执行lua脚本，并将输出保存到对应的.out文件
        lua5.3 ./xpln.lua -f "$file" -s $seed -g xpln > "$out_dir/$(basename "$file")/$seed.out"
        echo "Complete output on $file with seed $seed"
    done
done