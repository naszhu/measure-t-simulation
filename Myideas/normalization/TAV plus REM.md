这非常硬核。我们要做的不是文学修辞，而是**数学外科手术**。我们要把 TVA (Bundesen) 和 REM (Shiffrin & Steyvers) 切开，看看它们的内脏到底哪里不一样，然后用最新的 **GenBC (General Biased Competition)** 的逻辑把它们缝合起来。

这里没有废话。直接上公式对比。

### 第一部分：解剖台——TVA vs. REM

为什么公式长得不一样？因为一个是**流速（Rate）**，一个是**状态（State）**。

#### 1. TVA (Theory of Visual Attention)

本质： 泊松赛跑模型 (Poisson Race Model)。

核心量： $v$ (速率/Hazard Rate)。

物理意义： 此时此刻，每毫秒有多少证据积累进来？

$$v(x, i) = \eta(x, i) \beta_i \frac{w_x}{\sum w}$$

- **输入：** 像素/特征强度 ($\eta$)。
    
- **参数：** 偏置 ($\beta$)，资源池 ($\sum w$)。
    
- **过程：** 连续时间的**竞争**。谁先跑到终点 $K$，谁就进入 VSTM。
    
- **输出：** 编码完成的时间 $t$ (服从指数分布)。
    

#### 2. REM (Retrieving Effectively from Memory)

本质： 贝叶斯似然比模型 (Bayesian Likelihood Ratio)。

核心量： $\lambda$ (似然比/Odds)。

物理意义： 此时此刻，这东西看起来像不像那个东西？（静态匹配）。

$$\lambda_j = (1-c)^{n_q} \prod_{k \in M} \frac{c + (1-c)g}{g}$$

- **输入：** 两个向量的匹配特征数 ($M$) 和不匹配特征数 ($n_q$)。
    
- **参数：** $c$ (正确匹配概率), $g$ (几何分布参数/区分度)。
    
- **过程：** 离散特征的**比对**。计算 Probe 和 Trace $j$ 的相似度。
    
- **输出：** 认出概率 $P(Rec) = \frac{\Phi}{1+\Phi}$。
    

---

### 第二部分：Missing Link —— 动态编码 (Cox & Shiffrin)

你提到了 Cox & Shiffrin (Dynamic Encoding)。这就是连接两者的**传送门**。

TVA 的输出，正是 REM 的输入。

数学桥梁：

TVA 的速率 $v$ 决定了 REM 中的特征向量 $\mathbf{V}$ 是如何随时间 $t$ 被填充的。

假设一个物体有 $N$ 个特征（对应 REM 的向量维度）。

在 TVA 视角下，每一个特征 $k$ 都有一个被感知到的速率 $v_k$。

在时间 $t$ 时，特征 $k$ 被成功编码进长时记忆的概率是：

$$P(\text{Feature } k \text{ encoded at time } t) = 1 - e^{-v_k \cdot t}$$

**这就是统一的关键：**

- **TVA** 描述了 $\frac{d}{dt}$ (特征积累的速度)。
    
- **REM** 描述了 $\int_0^t$ (特征积累的总量) 之后的匹配结果。
    

如果 $t \to \infty$，TVA 跑完了，所有能看见的特征都记下来了，这时候你再去做 REM，就是经典的 REM。

如果 $t$ 很短，TVA 还在跑，REM 的向量就是残缺的 (Noisy/Sparse Vector)。

---

### 第三部分：GenBC 统一方程 —— 用 GenBC 表达 Recognition Memory

GenBC (Kyllingsbæk et al., 2025) 的核心思想是：无论是“看物体”还是“选动作”，本质都是**基于效用的偏置竞争**。

我们现在把 **Recognition Memory** 也看作一种 **Action Selection**（选择“旧”还是“新”，或者选择“回忆起 Trace A”）。

我们要用 GenBC 的通用公式来重写 REM。

#### 1. GenBC 的通用形式 (The Template)

$$E(j) = F(\text{Evidence}_j, \text{Bias}_j) \ominus \text{Normalization}$$

- $E(j)$: 选择选项 $j$ 的净能量。
    

#### 2. 把 REM 塞进 GenBC

我们不再计算冷冰冰的似然比，我们计算**提取强度 (Retrieval Strength)**。

**定义的映射：**

- Sensory Evidence ($\eta$): 变成了 Probe-Trace Similarity ($S_{pj}$)。
    
    即：现在的线索 (Probe) 和记忆库里的痕迹 $j$ 有多像？
    
    $$S_{pj} \approx \text{REM Likelihood Equation}$$
    
- Bias ($\beta$): 变成了 Context/Goal Relevance ($C_j$)。
    
    即：当前的上下文 (Context) 或者你的搜索意图（比如“我在找红色的东西”）对痕迹 $j$ 的加权。
    
- Normalization ($\sum w$): 变成了 Global Familiarity / Noise ($\sum S \cdot C$)。
    
    即：所有记忆痕迹的总共鸣强度。
    

#### 3. 最终的 Unified Equation (The GenBC-Memory Equation)

这是一个描述 **Memory Retrieval Rate** 的公式：

$$v_{\text{retrieve}}(j, t) = \underbrace{S_{pj}(t)}_{\text{Evidence}} \cdot \underbrace{\beta_{\text{context}}}_{\text{Bias}} \cdot \frac{1}{\sum_{k \in LTM} (S_{pk}(t) \cdot \beta_k)}$$

**物理意义解读：**

- **$S_{pj}(t)$ (Dynamic Evidence):** 这里不再是静态的，而是结合了 Cox & Shiffrin。随着你注视 Probe 的时间 $t$ 变长，你提取出的特征越多，证据 $S$ 越强。
    
- **$\beta$ (Bias):** 这就是 GenBC 的精髓。你可以通过意念控制（Top-down）去放大某些特定的记忆痕迹。比如 Bias 指向“上次派对遇到的人”，所有该 Context 下的 $S$ 都会被放大。
    
- **分母 (Competition):** 这解释了 REM 中的 **List Length Effect** 和 **Fan Effect**。记忆库越大（$k$ 越多），分母越大，提取速率 $v$ 越慢。
    

---

### 第四部分：终极实验范式 (The "Gradual Shift" Paradigm)

你要一个能“一下包含所有”的范式，从感知 (TVA) 平滑过渡到记忆 (REM/GenBC)。

**范式名称：The Continuous Evidence Stream (CES) Paradigm**

**1. 任务流程：**

- **Phase 1: Dynamic Visual Search (The TVA Phase)**
    
    - 屏幕上出现杂乱的特征流（比如不断变换的颜色碎片）。
        
    - 任务：一旦看到“红色圆圈”组合（Target），立即按键。
        
    - _模型拟合：_ 用 TVA 拟合反应时分布。计算 $v_{\text{percept}}$ 和 $\beta_{\text{visual}}$。
        
    - _关键变量：_ 操纵 **Exposure Duration** ($t_{enc}$).
        
- **Phase 2: Action Selection (The GenBC/MIS Phase)**
    
    - 在某些 trial 中，看到 Target 后，不仅要按键，还要从三个动作中选一个（例如：红圆 $\to$ 左手；蓝方 $\to$ 右手）。
        
    - _模型拟合：_ 用 GenBC 拟合动作选择的错误率和RT。
        
    - _过渡：_ 这里的 Input 不再是像素，而是 Phase 1 建立的 Object Representation。
        
- **Phase 3: Delayed Recognition (The REM Phase)**
    
    - 延迟 5秒 - 1分钟。
        
    - 屏幕出现一个 Probe（可能是刚才看过的，也可能是新的）。
        
    - 任务：“这个刚才出现过吗？”
        
    - _关键操纵：_ **不匹配的 Context。** (例如：Phase 1 是黑色背景，Phase 3 是白色背景)。
        

**2. 核心预测 (The "Money" Prediction)**

我们要证明 **Memory Retrieval 只是 Time-Shifted Perception**。

- 预测公式关联：
    
    我们在 Phase 1 测出的视觉速率 $v_{\text{percept}}$，经过时间 $t_{enc}$ 积分后，形成的向量强度 $M$，必须能直接预测 Phase 3 中的 Memory Discrimination ($d'$)。
    
    如果你用 GenBC 的逻辑，你应该能观察到：
    
    Visual Crowding (TVA中的分母) 和 Memory Interference (REM中的分母) 是连续的。
    
    - **实验操作：** 在 Phase 1 增加视觉干扰物（Distractors）。
        
    - **结果 A (TVA):** $v_{\text{target}}$ 下降（因为分母 $\sum w$ 变大）。
        
    - **结果 B (REM):** 即使你在 Phase 3 把干扰物撤掉，只留 Target，Phase 3 的 $d'$ 也会下降。
        
    - **最强证据：** 如果你在 Phase 3 重新引入那些干扰物作为 Context 线索，反而能利用 GenBC 的 Bias ($\beta$) 把 Target 的提取速率救回来！
        

总结：

这个范式不需要你分别跑两个模型。你建立一个单一的随机微分方程 (SDE)。

- $0-500ms$: 方程由 $\eta_{visual}$ 驱动 (TVA)。
    
- $500ms - \text{delay}$: 方程状态冻结或缓慢衰减 (MIS/VSTM)。
    
- $\text{Test Phase}$: 方程由 $S_{probe}$ 和 $\beta_{context}$ 重新激活 (REM/GenBC)。
    

这就是你要的“一下包含所有”。所有的参数（$v, \beta, K$）在整个时间轴上是共享的，只是在不同阶段被不同的输入源（光子 vs. 神经痕迹）所驱动。