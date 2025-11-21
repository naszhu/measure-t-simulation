# 项目完整解释文件（Markdown）

以下内容对 **How Gamification Affects Software Developers: Cautionary Evidence from a Natural Experiment on GitHub**（论文）及你提供的 **Gamification × Developers**（PPT）进行系统性整合、结构化说明。

内容覆盖：

1. 所有术语（terminologies）与数据分析方法（data analysis methods）解释。
    
2. 每个研究问题（RQ1–RQ4）从提出到分析方法、到论文结果的完整逻辑。
    
3. 所有论文中的图（figures）逐一解释图意、数据来源、分析方式。
    
4. PPT 每张 slide 的 finding 与论文内容的对应关系。
    
5. PPT 中绘制每个图的底层数据来源（来自论文哪个部分、哪张图、哪种分析）。
    
6. 覆盖论文的 introduction、discussion、limitations 等其余部分。
    

---

# 1. Terminologies（关键术语）

以下为论文与 PPT 中出现的核心研究术语，用 **中文连接词** + **English 术语** 解释：

### • Gamification（游戏化）

指在非游戏环境中加入 **points, badges, leaderboards** 等机制，去改变或强化用户行为。  
在 GitHub 中，对应的就是 **contribution streak counters**。

### • Streak / Streak Counter（连续贡献天数计数器）

GitHub 曾显示：

- **Current Streak** 当前连续几天有贡献。
    
- **Longest Streak** 历史最长连续贡献天数。
    

### • Natural Experiment（自然实验）

因为 GitHub **突然、无预警** 移除 streak counters，等于提供一个“外生冲击”，可用来观察行为变化。

### • Contribution Types（贡献类型）

论文中 streak 计算包含：

- commits
    
- issues
    
- pull requests
    

### • Single Contribution Day（SCD 单一贡献日）

一天之中只做 **exactly one** 贡献的日子，常意味着行为是为了“维持 streak”，而不是正常开发。

### • Regression Discontinuity Design（RDD 回归不连续设计）

一种统计方法，用来检测某个时间点是否出现 **因处理导致的跳变**。  
论文用它来检测：

- “周末贡献比例”是否在移除 counter 当周突然下降。
    

### • Assortativity（同质性 / 属性相关性）

用于社交网络，衡量“节点是否更倾向与具有相同标签的节点连接”。论文用它检测：

- streakers 是否互相连接（表示 social influence）。
    

### • Survival Curve（生存曲线）

用来表示 “一个 streak 能活多久”。论文用它比较：

- 2016（移除之前）vs 2017（移除之后）的 streak survival。
    

### • 100DaysOfCode（100 天编码挑战）

GitHub 上真实存在的挑战，用 streak（或 repo journal）来完成“连续 100 天编码”的目标。  
论文用它分析：

- goal-setters 是否在 counter 移除后“中断努力”。
    

---

# 2. Research Questions（研究问题）完整解释

论文四个研究问题（RQ）形成一个完整因果链：

## **RQ1: Did streaking behavior change after the removal?**

**研究目的：** streak counters 移除后，开发者是否停止维持 streak？

**分析方法：**

- 计算 streak 分布（长度 ≥ 20, ≥ 60, ≥ 200 的比例）。
    
- 比较设计变更前后 **share of streaking developers** 的变化趋势。
    
- 使用 **Mann-Whitney U test** 检验 streak 长度分布的差异。
    

**论文结论：**

- 长 streak（≥20, ≥60）在移除当天后 **大规模立即下降**。
    
- 特别是“正在进行中的长 streak”大量被放弃。
    
- 但极度极端 streak（>200）短期内无立即变化（因为已经很深了）。
    

**核心含义：**  
→ streak counters 的激励功能 **强且即时**。

---

## **RQ2: Did timing/distribution of activity change?**

目标：移除 streak counters 后，开发者“贡献的时间模式”是否改变？

论文拆成两个子问题：

### (A) Weekend Activity 是否下降？

方法：

- 计算变更前后“周末贡献比例”。
    
- 使用 **RDD 回归不连续设计** 检测周末工作是否出现跳变。
    
- 做 placebo tests 确认跳变不是“季节或假期”造成的。
    

结果：

- **周末贡献显著下降**。  
    → 说明 streak counters 之前确实在“强迫开发者周末也来提交一行”。
    

---

### (B) Single Contribution Day 减少了吗？

方法：

- 比较 streak ≥60 的 SCD 分布。
    
- 看 streak 生命周期末端的 SCD 是否下降。
    

结果：

- 移除前 → SCD 占比更高（尤其是末端）。
    
- 移除后 → SCD 明显减少。
    

含义：  
→ 之前很多“无意义的小提交”是为了“喂 streak 计数器”。

---

## **RQ3: Did developers use counters to set goals?**

观察 **100DaysOfCode** 这类 goal-setting 群体。

方法：

- 抓取 fork 100DaysOfCode 的用户。
    
- 比较移除前后达到目标 g=50, 100, 105, 150 的人数。
    

结果：

- 移除后“集体 drop”现象非常明显。
    
- g=100 与 g=105 差距巨大（达成 100 后不愿继续）。
    

含义：  
→ streak counter 是一个 goal-setting 工具。  
→ 移除它会“削弱或终止”这类目标维持行为。

---

## **RQ4: Was social-network synchronization reduced?**

研究 streak 在社交网络中的“模仿效应”。

方法：

- 使用 mutual-follow network。
    
- 计算 assortativity（属性同质性）。
    
- 用 randomization 排除“排序/同类人本来就一起”的机制。
    

结果：

- 移除前：显著高 assortativity（强 social influence）。
    
- 移除后：assortativity 大幅下降（但仍非零）。
    

含义：  
→ counters 提供了“公开排行榜”性质，使得“看到别人 streak”时更可能模仿。

---

# 3. Paper Figures（论文所有图）逐图解释

以下依照论文顺序：

## **Figure 1: GitHub profile with streak counters（界面示例）**

意义：

- 让读者理解“被移除的计数器是什么”。  
    来源：GitHub 官方过去的 UI。
    

---

## **Figure 2: Share of developers with streaks ≥ 20 / 60 / 200**

意义：

- 展示 streak counters 移除后 **即时下降**。
    
- 可看到 holiday / GitHub outage 的对称性下降（验证数据稳定性）。
    

数据来源：

- 所有贡献日志（290M contributions）。
    
- 重新计算 daily streak length。
    

---

## **Figure 3: Country-wise streak levels（美国/德国/英国/中国）**

意义：

- 中国 developer 在计数器移除后下降幅度较小。
    
- 论文推测与“工作文化差异”“996 抗议事件”相关。
    

---

## **Table I: Monday-start streak comparison across dates**

意义：

- Monday Effect：周一开始的 streak 本来更长。
    
- 移除后 Monday streak 明显更短。
    

---

## **Figure 4: Survival curves（2016 vs 2017）**

意义：

- “长 streak 的生存概率”在移除后下降。
    
- 长 tail 减少 → fewer extremely long streaks。
    

---

## **Table II & Table III: Weekend Activity + RDD**

意义：

- TABLE II：描述性统计：周末贡献下降。
    
- TABLE III：RDD 显著（p<0.001）→ causal effect。
    

---

## **Figure 5: Placebo RDD tests**

意义：

- 确认真实跳变发生在“移除那周”，其他周没有。
    
- 排除假期、季节性干扰。
    

---

## **Figure 6: SCD by Decile**

意义：

- 之前 SCD 很高 → streak-chasing。
    
- 移除后下降 → 行为变自然。
    

---

## **Figure 7 & Figure 8: 100DaysOfCode Users**

意义：

- 移除后目标追踪明显受影响。移除 gamification 会让人“当场停止维持行为”。**每天看有多少人还在继续备考**  
→ 过程中放弃的人会立即下降
    
- 100 vs 105 的巨大 drop 体现“anchoring to round number”。
    计数器移除后，“积极维持 streak 的人”有没有瞬间消失？

移除 counter 是否影响开发者成功达成“100天目标”？

假设你在研究“备考 100 天挑战”：

- **Figure 7 就像是：每天看有多少人还在继续备考**  
    → 过程中放弃的人会立即下降
	    ### 它显示的是什么？
	
	每天
	- 有多少开发者 streak ≥ 50？
	- 有多少开发者 streak ≥ 100？
	- 有多少开发者 streak ≥ 150？
	
	这些数是 daily、实时的。
    
- **Figure 8 就像是：最终有多少人真的考满 100 天？**  
    → 即使中间有人坚持，最终完成的人数仍会受影响
	### 它显示的是什么？
	随着时间推移，有多少人：
	- 完成了 streak ≥ 50
	- 完成了 streak ≥ 100
	- 完成了 streak ≥ 105
	- 完成了 streak ≥ 155
	    

这是 cumulative（累计）曲线，不是 daily 状态。
---

## **Table IV & V: Assortativity Before vs After**

意义：

- 移除前 social influence 强。
    
- 移除后显著下降 → counters 的 social signaling 消失。
    

---

# 4. PPT Slides 与论文内容的对应关系

下面解释 PPT 每一页 slide 的 finding “来自论文哪一部分”。

## **Slide: One UI change → Global behavior shift**

对应：论文 Introduction + Figure 2

- 提到 sudden, silent removal
    
- Figure 2 显示“全球级行为改变”
    

---

## **Slide: The Event — Removal of streak counters**

对应：论文 Fig.1 + Section III.A

---

## **Effect #1: Long streaks vanished**

来自：Figure 2, Figure 4, Table I

- counters 移除后 streak 大幅下降
    

---

## **Effect #2: Weekend activity ↓**

来自：Table II + RDD Table III + Figure 5

---

## **Effect #3: Single-commit days ↓**

来自：Figure 6

---

## **Effect #4: Social influence weakened**

来自：Table IV, Table V

---

## **Effect #5: Goal-setters affected (100DaysOfCode)**

来自：Figure 7, Figure 8

---

## **Risks: Overwork, metric chasing, low-value activity**

来自：Discussion

---

## **For Designers: Rare Natural Experiment**

来自：Discussion + Introduction

---

# 5. PPT 图的数据来自哪里？

PPT 所有图均由 **论文原始图表** 改写：

|PPT 图标题|数据来源|对应论文图|
|---|---|---|
|Long streaks vanished|Daily streak counts × thresholds|Figure 2 / Figure 4|
|Weekend activity ↓|weekend contribution ratio|Table II / Table III / Figure 5|
|Single-commit days ↓|SCD share by decile|Figure 6|
|Social influence ↓|assortativity, P(SN|S)|
|Goal-setters drop|streak≥100 user counts|Figure 7 / Figure 8|

---

# 6. Introduction（导论）概括

论文指出：

- gamification 有“提升 engagement”的一面，也有“扭曲行为、造成压力”的一面。
    
- GitHub 的 streak counters 是一种典型 gamification。
    
- 移除它构成一个 rare natural experiment。
    
- 可以回答：gamification 是如何改变 developer 的行为。
    

---

# 7. Discussion（讨论）

三大核心论点：

### **(1) Gamification 不是中性的**

它有：

- 过度激励 → overwork
    
- 指标导向 → metric chasing
    
- 社交压力 → peer pressure
    

### **(2) 设计者必须承担伦理责任**

因为用户会为了游戏机制改变工作习惯。

### **(3) streak counters 造成的行为有部分“不可取”**

包括：

- 单一贡献日（低价值）
    
- 周末强迫工作
    
- 追求数字而不是产出
    

---

# 8. Limitations（限制）

论文提到：

- streak computation 对时间戳敏感
    
- 用户地理位置推断准确度有限
    
- 只能观察“移除”，没有观察“添加”阶段
    
- contribution graph 仍存在 gamification 影响
    

---

# 总结

全文结合 PPT，你的 slide 就是在“论文 50 页内容 → 8 分钟展示” 的精炼表达。现在这份 MD 文件是从最细的层级把论文所有方法、术语、图表、结果、含义、PPT 对应关系全部写清楚。

你可以继续要求我：

- 把这个文件扩写成更长版本
    
- 或拆成多个子章节
    
- 或补充可视化图示说明