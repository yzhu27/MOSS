# MOSS
A Multi Objective Semi Supervised explanation system.

## Process
1. 在python sklearn库里找一个能用的sota半监督多目标方法能用到所有数据集上
2. 改一改lua的sway和xpln然后解释为什么有改进
3. 使用关于x, y变量的所有信息，用齐茨勒谓词对数据进行排序。将这些等级标准化为1-100
4. 做B0次predict, 评估predict的y结果,收集分布




1. 挑一个数据集跑二十次
2. 取每个的均值得到第一个表
3. 取不同sway和xpln均值的差得到tax
4. 