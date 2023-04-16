# MOSS
A Multi Objective Semi Supervised explanation system.

## Process
1. 在python sklearn库里找一个能用的sota半监督多目标方法能用到所有数据集上
2. 改一改lua的sway和xpln然后解释为什么有改进
3. 使用关于x, y变量的所有信息，用齐茨勒谓词对数据进行排序。将这些等级标准化为1-100
4. 做B0次predict, 评估predict的y结果,收集分布