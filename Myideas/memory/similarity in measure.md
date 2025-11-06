你现在的问题非常核心。你其实已经触到了一个深层次的哲学与数学交汇点：

> “我们到底在算什么？”  
> 是在算 similarity 吗？还是在算 density？还是在算 discriminability？  
> 这些概念是不是其实都只是不同层次上对“测度的近似”？

我来帮你把整个结构“拆回到第一原理”，然后一层一层往上，直到你清楚：  
1️⃣ 我们真正算的是什么；  
2️⃣ 为什么会出现距离、比值这些不同形式；  
3️⃣ discriminability 和 measure 之间的真实关系是什么。

---

## 一、最底层：我们要算的对象到底是什么

在所有记忆、分类、判别模型里——**无论是心理学的还是统计学的**——  
我们其实都在估计一个非常古老的对象：

$$  
\text{Given data }x,\quad \text{estimate the probability that it came from one source rather than another.}  
$$

数学上这就是：  
$$  
P(\text{old}|\ x) = \frac{p(x|\text{old})P(\text{old})}{p(x|\text{old})P(\text{old}) + p(x|\text{new})P(\text{new})}.  
$$

所以——无论你叫它 familiarity, discriminability, or decision variable，  
**本质都是“两个测度之间的相对密度”**。

也就是说：

- 我们并不是直接想“测相似度”；
    
- 我们想知道 “当前样本在两个测度体系里分别有多大权重”。
    

---

## 二、为什么出现“比值”（likelihood ratio）

这其实是一个非常深的定理的结果：  
**Neyman–Pearson lemma（奈曼–皮尔逊引理）**。

它证明了：

> 在所有可能的判别函数中，**似然比检验（likelihood ratio test）**  
>$$  
> \frac{p(x|\text{old})}{p(x|\text{new})} > \eta  
>$$  
> 是在给定错误率下最优的（maximizes power at fixed false alarm）。

换句话说，  
“比值”不是一个凭空的操作，而是——**在测度论下，两个测度 ν 与 μ 之间最优区分的唯一充分统计量**。

这就是为什么 REM 的 likelihood ratio 形式，实际上是 RN 导数 ( \frac{d\nu}{d\mu} )：  
它在数学上正是**两个测度之间的最优区分器**。

---

## 三、为什么 metric / distance 也能当 similarity

当我们没有显式的密度函数（即 (p(x)) 不可得）时，  
我们只能用距离来**近似密度变化**。

比如高维流形学习里的基本思想：  
$$  
\text{If } d(x,m) \text{ is small, then } p(x|m) \text{ is high.}  
$$  
因此所有的 metric-based similarity，本质上是一个**density approximation**：  
$$  
s(x,m) \approx \phi(-\beta d(x,m)) \propto \hat p(x|m)  
$$

再把这些相似度归一化：  
$$  
\frac{s(x,m)}{\sum_m s(x,m)} \approx \frac{\hat p(x|m)}{\hat p(x)} \approx P(m|\ x),  
$$  
你会发现：这就是**一个粗糙的概率密度比**。

所以你猜的完全正确：

> 所有 metric similarity、kernel similarity、normalized similarity，  
> 其实都在试图用“距离”去近似局部密度的比值。
> 
> 它们是在没有显式测度时，通过核或距离函数构造测度的近似。

---

## 四、Discriminability 是不是 density？

非常好，这个问题需要分层回答。

|层级|名称|本质|
|---|---|---|
|(1) Density (p(x))|测度在空间上的分布强度|对“世界”如何分布的描述|
|(2) Discriminability (d(x))|两个密度的相对差异|“这个点更属于哪个分布”的强度|
|(3) Decision|Discriminability 与阈值的函数|将连续差异离散化|

数学上：  
$$  
d(x) = \frac{p_1(x)}{p_2(x)} \quad \text{或} \quad d(x) = p_1(x) - p_2(x)  
$$  
它本质就是两个测度的**局部差异密度**，也就是一种 “density contrast”。

所以可以说：

> discriminability = density difference (or ratio)  
> 也就是说，它不是另一个东西，它是密度在两个测度之间的局部偏向度。

---

## 五、measure theory 里有没有“discriminability”的成熟概念？

有的，但数学里它通常不会用这个词。  
对应的概念有三个：

| 名称                                         | 定义                                             | 对应心理概念                        |
| ------------------------------------------ | ---------------------------------------------- | ----------------------------- |
| **Radon–Nikodym derivative**               | $f = \frac{d\nu}{d\mu}$                        | local discriminability (REM)  |
| **f-divergence**                           | $D_f(\nu\|\mu)=\int f(\frac{d\nu}{d\mu}),d\mu$ | global discriminability       |
| **Total variation / Wasserstein distance** | 测度之间的全局差异                                      | metric-based discriminability |

所以——在数学上，“discriminability”确实已经存在，只是换了名字：  
它以各种 divergence、distance、derivative 的形式出现。

---

## 六、你真正想问的最后一句话的答案

> “所以我们最后到底是在算什么？”

**答案：**  
我们在算的不是“距离”，也不是“相似性”本身，  
我们在算的是——

> “在测度空间中，当前样本点相对于两种测度（old/new）的局部权重比”。

形式上：  
$$  
f(x)=\frac{d\nu}{d\mu}(x)  
$$  
或近似地：  
$$  
f(x)\approx\frac{k(x,m)}{\int k(x,m'),d\mu(m')}  
$$  
所有的 similarity、normalization、distance、kernel、likelihood ratio  
都是对这个 (f(x)) 的不同层级近似。

---

### 🔹所以总结

1. **最终目标**：区分两种测度（old/new） → 求相对密度。
    
2. **不同路径**：
    
    - metric → 距离近似密度；
        
    - kernel → 积分近似密度；
        
    - ratio → 直接计算密度比。
        
3. **decision rule**：在密度比上设阈值（Neyman–Pearson最优判别）。
    
4. **discriminability**：是密度差异的另一种表达。
    
5. **所以 similarity 只是工具，density ratio 才是本体。**
    

---

如果你想，我可以把这一整段重写成论文用的正式 “Theoretical Grounding: Similarity as Density-Ratio Approximation” 部分，用测度论+心理建模的语言，把你的直觉（similarity 只是测度近似工具）系统地形式化。是否要我帮你写那一节？