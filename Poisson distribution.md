[[Poisson process]]

[[distribution]]

[[countable]]
[[descrete]]
[[柏松分布于随机性 Chat]] chat history
the [[random variable]]  X of Poisson is defined by number of events in [unit time]

if X is defined by number of events in "[any given time]", then the parameter inside Poisson should be $\lambda t$ instead of just $\lambda$
![[Pasted image 20250922193123.png]]
---
## **Example: Poisson**

- The Poisson distribution is not “a formula we chose.”
    
- It arises from the physical idea:
    
    - Events happen independently,
    - The chance of one event in a tiny interval Δt ≈ λΔt
    - The chance of 2 or more in Δt is negligible.
        
- From those assumptions, the mathematics forces the count distribution to be Poisson.
    
- And in that math, both the expected count and the variance = λ
    

So the _reason_ Poisson variance equals mean is that the process has no “memory” and no extra parameter for variability — once you set the rate, everything is determined.

---
## Approximated from Binomial

![[Pasted image 20250922193451.png]]
[[Binomial Distribution]]


n= number of independent trials:
We want to model a process where:
- The number of opportunities n is huge (conceptually infinite).
- Each opportunity has a tiny chance p of “success.”
- But the product np=λ (the expected count) stays finite.

Think:
- 1 minute broken into 1,000,000 tiny sub-intervals.
- Each sub-interval has a small chance p of seeing 1 arrival.
- On average, λ arrivals happen in the whole minute.

###### Intuitive interpretation

- Break time into infinitely many tiny “coin flips.”
- Each flip has tiny probability of success.
- The distribution of total successes in the whole interval → Poisson.
- That’s why Poisson naturally models rare, independent events occurring at some constant average rate.
p=λ/n

when you let the number of trials go to infinity while making each trial’s success probability shrink in just the right way p=λ/n, the Binomial converges to a limiting distribution — and the limiting formula simplifies to the Poisson.

---
### restriction
- **独立性**：不同时间段内发生的事情彼此不影响。
    
    > 你什么时候撒豆子，和未来/过去在别的时间点撒不撒无关。
    
- **稀疏性**：在极短的时间 Δt 内，几乎不可能撒两颗豆子。
    
    > 一口气撒两颗的概率比 (Δt) 还小，可以忽略。
    
- **匀速性**：在同样长度的时间段里，撒豆子的期望次数一样。
    
    > 也就是说，如果 1 分钟平均撒 3 颗，那么每个 20 秒的期望是 1 颗。
    

----
### From Poisson (count) to Gamma (waiting time)

Let \( N(t) \) be a homogeneous Poisson process with constant rate \( \lambda \).

#### 1. Poisson view — distribution of counts
The number of events observed by time \( t \) is:

$$
P(N(t) = k) = \frac{(\lambda t)^k e^{-\lambda t}}{k!}, \quad k = 0, 1, 2, \ldots
$$

#### 2. Waiting-time view — distribution of finishing time
Let \( T_k \) denote the *time of the k-th event*:

$$
T_k = \sum_{i=1}^{k} E_i, \quad E_i \stackrel{iid}{\sim} \text{Exp}(\lambda)
$$

Then the pdf of \( T_k \) is the [[Gamma (Erlang) distribution]]:

$$
f_{T_k}(t) = \frac{\lambda^k t^{k-1} e^{-\lambda t}}{(k-1)!}, \quad t > 0
$$

#### 3. Relationship between the two
These two views describe the same process:

$$
P(N(t) \ge k) = P(T_k \le t)
$$

and differentiating w.r.t. \( t \) converts between them.

Hence:

- The **Poisson distribution** gives the *probability of k events by time t*.
- The **Gamma distribution** gives the *distribution of the time for k events*.

They are dual descriptions of the same Poisson process.


---
## Poisson and exponential
![[Pasted image 20251014114928.png]]
“The probability that **no event has happened yet** by time _t_ is the same as the probability that **the waiting time until the first event** is **longer than _t_**.”


![[Pasted image 20251014114951.png]]
![[Pasted image 20251014115256.png]]