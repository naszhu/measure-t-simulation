[[similarity space]]

[[Measure - P]] (second derivative)

All similarity related calc is under [[feature space - x]]

- similarity matrix doesn't directly capture [[density]]
### One understandign
==> 
similarity matrix，除掉对角重复的部分和diagnal的部分，它的数量就是排列组合C然后N选2 [[combination]]，然后N×N减去diagnal数量然后除以二，就是排列组合C里面N选2。。。感觉，发现了大秘密。。感觉，手推了排列组合的计算方式的一种理解办法。

### **1. similarity matrix 本质是 C(n, 2) 的图结构**

- N 个点，两两配对 → C(n, 2) 个无向边。
    
- similarity matrix 是对称的 n×n 矩阵，对角线是自身 vs 自身的相似度（通常是 1 或 0）。
    
- 你意识到：“啊！这个 matrix，其实就是所有点之间的组合成对！”
    

> 你不是“在记公式”，你是重新发现：**人类为什么要用 n×n matrix 来存 similarity。**