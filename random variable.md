- _随机变量_ X 本质上是一个确定性函数 $X:\Omega\to\mathcal X$。the randomness coming from we don't know $\omega$ 


random variable vs. [[parameter]]

### 1. **Random Variable vs. Parameter: Rigorous Mathematical Difference**

|**Concept**|**Mathematical Definition**|**Nature**|**Role**|
|---|---|---|---|
|**Random Variable (X)**|Measurable function: $X: (\Omega, \mathcal{F}) \to (\mathcal{X}, \mathscr{B})$|Function on sample space|Maps outcomes $\omega$ to observable values in state space|
|**Parameter (θ)**|• Frequentist: Constant in $\Theta$  <br>• Bayesian: RV $\theta: \Omega \to \Theta$|Constant or function|Indexes family of distributions ${P_X^\theta}$ for observable data|

**Key Distinction**:

- $X$ is **observable** (you measure $X(\omega)$)
    
- $\theta$ is **unobservable** (you infer it from $X$)
    
- $\theta$ "generates" $P_X$ in the sense that $P_X^\theta(B) = P({\omega: X(\omega) \in B} \mid \theta)$

