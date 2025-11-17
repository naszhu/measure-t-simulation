# Bootstrapping: A Mathematical and Intuitive Explanation

Bootstrapping is a **non-parametric resampling method** used to estimate the
sampling distribution of a statistic (e.g., a regression coefficient, mean, or
indirect effect). It is especially important in mediation analysis because the
indirect effect $ab$ has a **skewed, non-normal distribution**.

This document explains exactly what bootstrapping is, why it works, and how it
is computed mathematically.

---

## 1. What Is Bootstrapping?

Bootstrapping produces many “new datasets” by repeatedly **sampling with
replacement** from the original dataset.

- The original dataset has $N$ rows (e.g., $N=400$ participants).
- Each bootstrap sample also has $N$ rows.
- Rows are drawn **with replacement**, so some original cases appear multiple
  times and some do not appear at all.

Each new dataset is used to re-estimate the statistic of interest.

This process creates an **empirical sampling distribution** of that statistic.

---

## 2. Why Bootstrapping?

Classical statistical tests assume normality.  
But many statistics—especially **products**, such as the mediation effect $ab$—do
not follow a normal distribution.

Bootstrapping makes **no distributional assumptions**.  
It uses the data themselves to approximate the sampling distribution.

This is why it is now the **standard method** for testing mediation.

---

## 3. The Mathematical Definition

Let the original dataset be:

$$
D = \{(x_1, m_1, y_1), \dots, (x_N, m_N, y_N)\}.
$$

A bootstrap sample is created by drawing $N$ indices:

$$
(i_1, i_2, \dots, i_N), \quad i_j \in \{1,\dots,N\}, \text{ independently with replacement}.
$$

Then the bootstrap dataset is:

$$
D^*_k = \{(x_{i_1}, m_{i_1}, y_{i_1}), \dots, (x_{i_N}, m_{i_N}, y_{i_N})\}.
$$

This process is repeated for $k = 1,\dots,B$ (typically $B = 5000$).

---

## 4. Re-Estimating the Parameters in Each Resample

For mediation, we estimate:

### Path a
$$
M = \alpha_0 + a_k X + \varepsilon_M.
$$

### Path b and the direct effect
$$
Y = \beta_0 + c'_k X + b_k M + \varepsilon_Y.
$$

Each bootstrap sample produces **new estimates**:

- $a_k$
- $b_k$
- $c'_k$

because each bootstrap dataset is slightly different.

---

## 5. The Bootstrap Indirect Effect

For each bootstrap sample:

$$
\text{Indirect}_k = a_k \cdot b_k.
$$

After $B$ bootstrap samples (e.g., 5000), we have a set of 5000 indirect effects:

$$
\{\text{Indirect}_1, \dots, \text{Indirect}_{5000}\}.
$$

This set is the **bootstrap sampling distribution** of the indirect effect.

---

## 6. Computing the Bootstrap Confidence Interval

1. Sort the 5000 indirect effects:
   $$
   \text{Indirect}_{(1)} \le \dots \le \text{Indirect}_{(5000)}.
   $$

2. Take the percentiles:
   - Lower bound: $\text{Indirect}_{(0.025)}$  
   - Upper bound: $\text{Indirect}_{(0.975)}$

This gives the **95% bootstrap confidence interval**:

$$
\big[\text{Indirect}_{(0.025)},\; \text{Indirect}_{(0.975)}\big].
$$

### Interpretation:

- If the CI **does not include 0**, the indirect effect is significant.  
- If the CI **includes 0**, the indirect effect is not significant.

This test works even when $a$ or $b$ alone is not significant.

---

## 7. Summary

- Bootstrapping draws samples **with replacement** from the original dataset.  
- Each bootstrap sample yields new estimates of $a_k$ and $b_k$.  
- The product $a_k b_k$ is computed for each sample.  
- The distribution of these products forms the **bootstrap sampling distribution**.  
- Significance is determined using the **bootstrap confidence interval**.  

Bootstrapping provides a robust, assumption-free way to test mediation effects
and is the standard approach in modern SEM.

