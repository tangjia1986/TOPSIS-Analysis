# TOPSIS 多准则决策分析

## 项目简介
TOPSIS（Technique for Order Preference by Similarity to Ideal Solution）是一种多准则决策分析方法，通过计算方案与理想解和负理想解的距离来进行方案排序。本项目提供了 TOPSIS 方法的完整实现和实际案例分析。

## 项目结构
- `topsis.py`: TOPSIS 算法核心实现
- `example.py`: 使用示例和案例分析
- `analysis.md`: 详细的分析报告
- `requirements.txt`: 项目依赖

## 分析结果
最新的 TOPSIS 分析结果显示：
- 最优方案：方案3 (得分：0.67095431)
- 次优方案：方案4 (得分：0.54317673)
- 其他方案：方案1 (得分：0.40078715)，方案2 (得分：0.40602972)

## 快速开始
1. 克隆仓库
```bash
git clone https://github.com/tangjia1986/TOPSIS-Analysis.git
```

2. 安装依赖
```bash
pip install -r requirements.txt
```

3. 运行示例
```bash
python example.py
```