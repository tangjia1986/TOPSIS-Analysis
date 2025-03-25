import numpy as np
from typing import List, Union, Optional

class TOPSIS:
    def __init__(self, matrix: np.ndarray, weights: List[float], criteria: List[bool]):
        """
        初始化 TOPSIS
        Args:
            matrix: 决策矩阵，每行是一个方案，每列是一个指标
            weights: 权重列表
            criteria: 指标是否为效益型（True）或成本型（False）
        """
        self.matrix = np.array(matrix, dtype=float)
        self.weights = np.array(weights, dtype=float)
        self.criteria = np.array(criteria, dtype=bool)
        
        if not (abs(self.weights.sum() - 1.0) < 1e-6):
            raise ValueError("权重之和必须为1")
            
    def normalize(self) -> np.ndarray:
        """向量归一化"""
        return self.matrix / np.sqrt((self.matrix ** 2).sum(axis=0))
        
    def weighted_normalize(self) -> np.ndarray:
        """加权归一化"""
        return self.normalize() * self.weights
        
    def ideal_solutions(self, weighted_matrix: np.ndarray) -> tuple:
        """计算理想解和负理想解"""
        ideal = np.zeros(weighted_matrix.shape[1])
        neg_ideal = np.zeros(weighted_matrix.shape[1])
        
        for j in range(weighted_matrix.shape[1]):
            if self.criteria[j]:
                ideal[j] = weighted_matrix[:, j].max()
                neg_ideal[j] = weighted_matrix[:, j].min()
            else:
                ideal[j] = weighted_matrix[:, j].min()
                neg_ideal[j] = weighted_matrix[:, j].max()
                
        return ideal, neg_ideal
        
    def calculate_distances(self, weighted_matrix: np.ndarray, 
                          ideal: np.ndarray, neg_ideal: np.ndarray) -> tuple:
        """计算到理想解和负理想解的距离"""
        d_ideal = np.sqrt(((weighted_matrix - ideal) ** 2).sum(axis=1))
        d_neg_ideal = np.sqrt(((weighted_matrix - neg_ideal) ** 2).sum(axis=1))
        return d_ideal, d_neg_ideal
        
    def calculate_scores(self) -> np.ndarray:
        """计算 TOPSIS 得分"""
        weighted_matrix = self.weighted_normalize()
        ideal, neg_ideal = self.ideal_solutions(weighted_matrix)
        d_ideal, d_neg_ideal = self.calculate_distances(weighted_matrix, ideal, neg_ideal)
        
        return d_neg_ideal / (d_ideal + d_neg_ideal)
    
    def rank(self) -> List[int]:
        """获取方案排序（从好到坏）"""
        scores = self.calculate_scores()
        return (-scores).argsort().tolist()
    
    def sensitivity_analysis(self, delta: float = 0.1) -> dict:
        """敏感性分析"""
        base_scores = self.calculate_scores()
        sensitivity = {}
        
        for i in range(len(self.weights)):
            delta_weights = self.weights.copy()
            delta_weights[i] *= (1 + delta)
            delta_weights = delta_weights / delta_weights.sum()
            
            self.weights = delta_weights
            new_scores = self.calculate_scores()
            score_changes = np.abs(new_scores - base_scores)
            
            sensitivity[f'indicator_{i}'] = {
                'weight_variation': delta,
                'score_changes': score_changes.tolist(),
                'sensitivity_index': score_changes.mean()
            }
            
            self.weights = np.array(weights, dtype=float)
            
        return sensitivity