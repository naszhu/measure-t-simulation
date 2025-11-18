# Mediation vs. Moderation in SEM  
A concise mathematical explanation file

---

## 1. Summary  
A *mediator* explains **how/why** $X$ affects $Y$ (via $X \to M \to Y$).  
A *moderator* explains **when/for whom** $X$ affects $Y$ (via interaction $X \times W$).  
Mediation tests an **indirect effect** $ab$; moderation tests an **interaction**.

---

## 2. Mediation Model (Explicit Mathematics)

### 2.1 Model definitions
We define three variables:
- $X$: predictor  
- $M$: mediator  
- $Y$: outcome  

The mediation model requires two linear equations:

### **(a-path)**  
$$
M = \alpha_0 + aX + \varepsilon_M
$$

Here $a$ is the effect of $X$ on $M$.

### **(b-path + direct c’-path)**  
$$
Y = \beta_0 + c'X + bM + \varepsilon_Y
$$

Here:  
- $b$ is the effect of $M$ on $Y$ after controlling for $X$.  
- $c'$ is the direct effect of $X$ on $Y$ after accounting for $M$.

### **(Total effect)**  
$$
Y = \gamma_0 + cX + \varepsilon
$$

Where $c$ is the total effect of $X$ on $Y$ before adding the mediator.

---

## 2.2 Indirect effect  
The indirect effect is defined as the product of the two paths:

$$
\text{Indirect effect} = ab
$$

Why multiplication?  
Because the causal chain requires *both* $a$ and $b$ to be non-zero.  
If either path is zero, no effect is transmitted.

---

## 2.3 How mediation is tested in SEM

1. Estimate the $a$ path ($X \to M$).  
2. Estimate the $b$ path ($M \to Y$ controlling for $X$).  
3. Estimate the direct path $c'$.  
4. Compute $ab$ as the indirect effect.  
5. Test $ab$ using a **bootstrap confidence interval**.

---

## 2.4 What is a bootstrap CI?

Because the product $ab$ is not normally distributed, SEM uses **bootstrapping**:

1. Resample the data with replacement (often 5000 samples).  
2. Recompute $a$, $b$, and $ab$ in each sample.  
3. Form the empirical 95% CI from these 5000 values.  
4. If 0 is **not** inside the CI → mediation is significant.

This is the modern standard for mediation testing.

---

## 2.5 Real-world mediation example

**$X$ = amount of childhood reading**  
**$M$ = vocabulary size**  
**$Y$ = reading comprehension**

- More reading increases vocabulary ($a>0$).  
- Larger vocabulary improves comprehension ($b>0$).  
- The indirect effect $ab$ explains **why** reading improves comprehension.

---

## 3. Moderation Model (Explicit Mathematics)

### 3.1 Model structure  
A moderator $W$ changes the strength of the relationship between $X$ and $Y$.

Regression model:

$$
Y = \delta_0 + b_1X + b_2W + b_3(XW) + \varepsilon
$$

Here:  
- $b_1$ = effect of $X$ when $W=0$  
- $b_3$ = interaction term (the moderation effect)

Interpretation of moderation:

$$
\frac{\partial Y}{\partial X} = b_1 + b_3W
$$

Therefore, the slope of $X \to Y$ depends on the level of $W$.

---

## 3.2 How moderation is tested

### Method A: Interaction term  
- Create the product $XW$.  
- Add it as a predictor of $Y$.  
- If $b_3$ is significant → moderation is supported.

### Method B: Multi-group SEM  
Used when $W$ is categorical (e.g., gender groups).  
- Fit the same SEM in each group.  
- Constrain the $X \to Y$ path to be equal.  
- Use $\chi^2$ difference test.  
- If paths differ → moderation exists.

---

## 3.3 Real-world moderation example

**$X$ = stress**  
**$W$ = social support**  
**$Y$ = depression**

- When social support is low, stress strongly predicts depression.  
- When social support is high, this slope weakens.

Mathematically this means $b_3 < 0$,  
i.e., increasing $W$ reduces the slope of $X \to Y$.

---

## 4. Comparison Table

| Concept | Mathematical Form | Key Test | Interpretation |
|--------|--------------------|----------|----------------|
| Mediator ($M$) | $X\to M\to Y$; indirect effect $ab$ | Bootstrap CI on $ab$ | Explains **how/why** X affects Y |
| Moderator ($W$) | $Y = b_1X + b_2W + b_3(XW)$ | Significance of $b_3$ | Explains **when/for whom** X affects Y |

---

## 5. Final Notes

- Mediation always has **two linear paths** ($a$ and $b$).  
- Moderation always requires **an interaction**.  
- SEM does not change the math; it estimates all paths simultaneously with latent constructs if needed.

