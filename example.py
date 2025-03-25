import numpy as np
from topsis import TOPSIS

# 示例数据
matrix = np.array([
    [0.9, 0.8, 0.7],
    [0.8, 0.9, 0.6],
    [0.7, 0.7, 0.9],
    [0.8, 0.7, 0.8]
])

weights = [0.4, 0.3, 0.3]
criteria = [True, True, True]  # 全部为效益型指标

# 创建 TOPSIS 实例
topsis = TOPSIS(matrix, weights, criteria)

# 计算得分
scores = topsis.calculate_scores()
print("TOPSIS 得分：", scores)

# 获取排名
ranks = topsis.rank()
print("排名（从好到坏）：", ranks)

# 进行敏感性分析
sensitivity = topsis.sensitivity_analysis()
print("\n敏感性分析结果：")
for indicator, results in sensitivity.items():
    print(f"\n{indicator}:")
    print(f"权重变化：{results['weight_variation']}")
    print(f"得分变化：{results['score_changes']}")
    print(f"敏感度指数：{results['sensitivity_index']}")