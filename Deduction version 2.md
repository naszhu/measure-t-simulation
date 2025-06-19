Below is a rigorous derivation of the REM posterior odds, considering an activation filter and specific origins for targets and confusing foils. We will first assume a uniform non-match likelihood $f_N(s_i)$ and then show how it adapts for type-specific non-match likelihoods $f_{N,type(i)}(s_i)$. 

### Glossary of Terms (Applicable to Both Sections)

| Symbol        | Meaning                                                                                                                                             |     |
| :------------ | :-------------------------------------------------------------------------------------------------------------------------------------------------- | --- |
| $M$           | Total number of **activated** traces after any first-stage filter. The similarity vector $D$ (or $\mathbf{s}$) has $M$ components.                  |     |
| $n$           | Number of items in the **current study list**. All $n$ are assumed to be activated. Let $A$ be the set of indices for these $n$ traces.             |     |
| $n'_{phys}$   | *Physical* number of items in the **most-recent prior list** from which confusing foils ($CF$) are sampled. Let $B_{phys}$ be this set of indices.  |     |
| $n^{\dagger}$ | Number of **activated** traces from the set $B_{phys}$. Let $B_{act}$ be this set of $n^{\dagger}$ activated traces ($B_{act} \subseteq B_{phys}$). |     |
| $x$           | Prior probability that a foil trial is a confusing foil ($CF$).                                                                                     |     |
| $1-x$         | Prior probability that a foil trial is a pure new foil ($NF$).                                                                                      |     |
| $D$           | The observed data, i.e., the vector of $M$ similarity scores $(s_1, s_2, \ldots, s_M)$ from the activated traces.                                   |     |
| $O$           | Event that the test item is an "Old" target (from the current list).                                                                                |     |
| $N$           | Event that the test item is a "New" foil (either $CF$ or $NF$).                                                                                     |     |
| $S_j$         | Event that trace $j$ is the true source/match for the test item.                                                                                    |     |
| $N_j$         | Event that trace $j$ is a non-match for the test item.                                                                                              |     |
| $f_M(s_j)$    | Likelihood $P(D_j \mid S_j)$ of observing data $s_j$ from trace $j$ if it's a match.                                                                |     |

---

## Section 1: Derivation Assuming a Uniform $f_N(s_i)$

In this section, we assume a single likelihood function $f_N(s_i) = P(D_i|N_i)$ for all non-matching components $i$.
Let $\lambda_k = \frac{f_M(s_k)}{f_N(s_k)}$.

### Rigorous Derivation Steps (Uniform $f_N$)

The goal is to compute the posterior odds $\frac{P(O \mid D)}{P(N \mid D)}$.

$$
\begin{aligned}
\frac{P(O \mid D)}{P(N \mid D)}
\;&=\; \frac{P(D \mid O)P(O)}{P(D \mid N)P(N)} && \text{(Bayes' Theorem)} \\[1ex]
\;&=\; \frac{P(D \mid O)}{P(D \mid N)} && \text{(Assuming equal priors } P(O)=P(N)\text{)} \\[1ex]
\end{aligned}
$$

**1.1. Numerator: Likelihood $P(D \mid O)$ (Uniform $f_N$)**

Targets ($O$) are drawn only from the $n$ current list items (set $A$, all assumed activated). Given $O$, each of these $n$ items is equally likely to be the source.
$$
\begin{aligned}
P(D \mid O) \;&=\; \sum_{j \in A} P(D \mid S_j \text{ and } O) P(S_j \mid O) && \text{(Law of Total Probability over sources } j \in A\text{)} \\[1ex]
\;&=\; \sum_{j \in A} P(D \mid S_j) \frac{1}{n} && \text{(Since } P(S_j|O) = 1/n \text{ for } j \in A \text{, and } 0 \text{ otherwise)} \\[1ex]
\;&=\; \frac{1}{n} \sum_{j \in A} \left[ f_M(s_j) \prod_{\substack{i=1 \\ i \neq j}}^{M} f_N(s_i) \right] && \text{(If } j \text{ is match, } D_j \sim f_M, \text{ other } D_i \sim f_N \text{ over } M \text{ activated traces)}
\end{aligned}
$$

**1.2. Denominator: Likelihood $P(D \mid N)$ (Uniform $f_N$)**

A foil ($N$) is either a confusing foil ($CF$) with probability $x$, or a new foil ($NF$) with probability $1-x$.
$$P(D \mid N) \;=\; x P(D \mid CF) \;+\; (1-x) P(D \mid NF)$$

* **1.2a. Likelihood $P(D \mid CF)$ (Confusing Foil, Uniform $f_N$):**
    Confusing foils are sampled uniformly from the $n'_{phys}$ items in the physical prior list ($B_{phys}$).
    If the sampled item $j \in B_{phys}$ is activated ($j \in B_{act}$), its $s_j \sim f_M$ and other $M-1$ activated $s_i \sim f_N$.
    If the sampled item $j \in B_{phys}$ is *not* activated ($j \notin B_{act}$), then for the $M$ *activated* traces, none are a match, so $D \sim \prod_{i=1}^M f_N(s_i)$.

    $$
    \begin{aligned}
    P(D \mid CF) \;&=\; \sum_{j \in B_{phys}} P(D \mid S_j \text{ and } CF) P(S_j \mid CF) && \text{(LTP over sources } j \in B_{phys}\text{)} \\[1ex]
    \;&=\; \frac{1}{n'_{phys}} \sum_{j \in B_{phys}} P(D \mid S_j) && \text{(Since } P(S_j|CF) = 1/n'_{phys} \text{ for } j \in B_{phys}\text{)} \\[1ex]
    \;&=\; \frac{1}{n'_{phys}} \left( \sum_{j \in B_{act}} \left[ f_M(s_j) \prod_{\substack{i=1 \\ i \neq j}}^{M} f_N(s_i) \right] + \sum_{j \in B_{phys} \setminus B_{act}} \left[ \prod_{i=1}^{M} f_N(s_i) \right] \right) \\[1ex]
    \;&=\; \frac{1}{n'_{phys}} \left( \sum_{j \in B_{act}} \left[ f_M(s_j) \prod_{\substack{i=1 \\ i \neq j}}^{M} f_N(s_i) \right] + (n'_{phys} - n^{\dagger}) \prod_{i=1}^{M} f_N(s_i) \right)
    \end{aligned}
    $$

* **1.2b. Likelihood $P(D \mid NF)$ (New Foil, Uniform $f_N$):**
    A pure new foil matches none of the $M$ activated traces.
    $$
    P(D \mid NF) \;=\; \prod_{i=1}^{M} f_N(s_i)
    $$

**1.3. Combine and Cancel Common Product $P_0(D) = \prod_{i=1}^{M} f_N(s_i)$ (Uniform $f_N$)**

Recall $\lambda_k = f_M(s_k)/f_N(s_k)$. Any term $f_M(s_k) \prod_{i \neq k} f_N(s_i)$ can be written as $\lambda_k P_0(D)$.

* $P(D \mid O) = \frac{1}{n} \sum_{j \in A} \lambda_j P_0(D)$
* $P(D \mid CF) = \frac{1}{n'_{phys}} \left( \sum_{j \in B_{act}} \lambda_j P_0(D) + (n'_{phys} - n^{\dagger}) P_0(D) \right)$
* $P(D \mid NF) = P_0(D)$

Substituting into $\frac{P(D \mid O)}{x P(D \mid CF) + (1-x) P(D \mid NF)}$:
$$
\begin{aligned}
\frac{P(O \mid D)}{P(N \mid D)} \;&=\; \frac{ \frac{1}{n} \sum_{j \in A} \lambda_j P_0(D) }{ x \left[ \frac{1}{n'_{phys}} \left( \sum_{j \in B_{act}} \lambda_j P_0(D) + (n'_{phys} - n^{\dagger}) P_0(D) \right) \right] + (1-x) P_0(D) } \\[2ex]
\;&=\; \frac{ \frac{1}{n} \sum_{j \in A} \lambda_j }{ x \left[ \frac{1}{n'_{phys}} \left( \sum_{j \in B_{act}} \lambda_j + (n'_{phys} - n^{\dagger}) \right) \right] + (1-x) } && \text{(Cancel } P_0(D) \text{ from all terms)} \\[2ex]
\;&=\; \frac{ \frac{1}{n} \sum_{j \in A} \lambda_j }{ x \left( \frac{1}{n'_{phys}} \sum_{j \in B_{act}} \lambda_j + \frac{n'_{phys} - n^{\dagger}}{n'_{phys}} \right) + (1-x) } && \text{(Distribute } 1/n'_{phys}\text{)}
\end{aligned}
$$

---

### Final Exact Odds Formula (Assuming Uniform $f_N$)
This is the rigorous expression for the posterior odds, given the activation filter, specific sources for targets and confusing foils, AND assuming a single $f_N(s_i)$ for all non-matching components.

$$
\boxed{
\frac{P(O \mid D)}{P(N \mid D)} \;=\; \frac{\displaystyle \frac{1}{n} \sum_{k \in A} \frac{f_M(s_k)}{f_N(s_k)}}{\displaystyle x \left( \frac{1}{n'_{phys}} \sum_{k \in B_{act}} \frac{f_M(s_k)}{f_N(s_k)} + \frac{n'_{phys} - n^{\dagger}}{n'_{phys}} \right) + (1-x)}
}
$$

* The sums $\sum_{k \in A}$ and $\sum_{k \in B_{act}}$ are over the respective sets of **activated** traces.
* The term $\frac{n'_{phys} - n^{\dagger}}{n'_{phys}}$ accounts for confusing foils sampled from physical prior list items that were *not* activated. If all $n'_{phys}$ items are activated ($n^{\dagger} = n'_{phys}$), this term becomes zero.

---
---

## Section 2: Derivation with Type-Specific $f_{N,type(i)}(s_i)$


You're absolutely right to scrutinize that step! It's crucial. Let's clarify exactly why $P_0^*(D)$ can still be defined and cancelled, even when the individual $f_{N,type(i)}(s_i)$ functions are different for each trace type.

#### Explanation (why can it be adapted)

**1. Defining the "Baseline" Noise Product $P_0^*(D)$**

When we introduce type-specific non-match likelihoods, we define $P_0^*(D)$ as the joint likelihood of observing the entire data vector $D=(s_1, s_2, \ldots, s_M)$ under the condition that **all $M$ activated traces are non-matches of their respective specific types**.

So, $P_0^*(D) = \prod_{i=1}^{M} f_{N,type(i)}(s_i)$.

* This means $P_0^*(D) = f_{N,type(1)}(s_1) \times f_{N,type(2)}(s_2) \times \ldots \times f_{N,type(M)}(s_M)$.
* It's critical to understand that $P_0^*(D)$ is still a single, well-defined value for a given data vector $\mathbf{s}$, even if $f_{N,type(1)}(\cdot)$ is a different mathematical function than $f_{N,type(2)}(\cdot)$, and so on. It's simply the product of the likelihoods of each observed $s_i$ under its own trace's specific non-match characteristic.
* This $P_0^*(D)$ correctly represents $P(D \mid NF)$ (the likelihood of the data given a Pure New Foil, where no activated trace is a match).
* It also correctly represents the likelihood of the data for a Confusing Foil that was sampled from a physical list item $j \in B_{phys}$ which was *not activated* ($j \notin B_{act}$). In this case, for the $M$ *activated* traces, none of them are the source of the CF, so they all behave as non-matches of their respective types.

**2. How a "Match" Term Relates to $P_0^*(D)$**

Now, consider a situation where one specific activated trace, say trace $j$, *is* the match (either as a target or an activated confusing foil). The likelihood of the data $D$ in this case is:
$P(D \mid S_j) = f_M(s_j) \times \prod_{\substack{i=1 \\ i \neq j}}^{M} f_{N,type(i)}(s_i)$

We can algebraically rewrite this term by multiplying and dividing by $f_{N,type(j)}(s_j)$ (assuming $f_{N,type(j)}(s_j) \neq 0$, which is necessary for $s_j$ to be observable under that non-match hypothesis):

$P(D \mid S_j) = f_M(s_j) \times \frac{\prod_{i=1}^{M} f_{N,type(i)}(s_i)}{f_{N,type(j)}(s_j)}$

$P(D \mid S_j) = \frac{f_M(s_j)}{f_{N,type(j)}(s_j)} \times \left( \prod_{i=1}^{M} f_{N,type(i)}(s_i) \right)$

Let $\lambda_j^* = \frac{f_M(s_j)}{f_{N,type(j)}(s_j)}$. This $\lambda_j^*$ is the likelihood ratio for trace $j$, using its own specific non-match likelihood in the denominator.

Then, $P(D \mid S_j) = \lambda_j^* \times P_0^*(D)$.

**3. Why This Still Allows Cancellation**

Because *every* term in the expanded likelihoods can be expressed as some coefficient times this *same* $P_0^*(D)$:

* $P(D \mid O) = \left( \frac{1}{n} \sum_{j \in A} \lambda_j^* \right) P_0^*(D)$
* The part of $P(D \mid CF)$ from activated confusing foils: $\left( \frac{1}{n'_{phys}} \sum_{j \in B_{act}} \lambda_j^* \right) P_0^*(D)$
* The part of $P(D \mid CF)$ from non-activated confusing foils: $\left( \frac{n'_{phys} - n^{\dagger}}{n'_{phys}} \times 1 \right) P_0^*(D)$ (because for these, the likelihood of $D$ *is* $P_0^*(D)$)
* $P(D \mid NF) = 1 \times P_0^*(D)$

When you substitute these into the odds ratio:
$$
\frac{P(O \mid D)}{P(N \mid D)} = \frac{ \left( \frac{1}{n} \sum_{j \in A} \lambda_j^* \right) P_0^*(D) }{ x \left[ \left( \frac{1}{n'_{phys}} \sum_{j \in B_{act}} \lambda_j^* + \frac{n'_{phys} - n^{\dagger}}{n'_{phys}} \right) P_0^*(D) \right] + (1-x) P_0^*(D) }
$$

The term $P_0^*(D) = \prod_{i=1}^{M} f_{N,type(i)}(s_i)$ is a common factor in the numerator and in every additive part of the denominator. Therefore, it **cancels out perfectly**.

**What you might have missed:**

The key is not that all $f_{N,type(i)}(s_i)$ have to be the *same function* for cancellation to occur. It's that the product $\prod_{i=1}^{M} f_{N,type(i)}(s_i)$ serves as the universal "baseline" likelihood when *no specific activated trace $j$ is designated as the unique source/match*. When a specific trace $j$ *is* the source, its individual $f_{N,type(j)}(s_j)$ contribution to this baseline product is replaced by $f_M(s_j)$. The ratio of $f_M(s_j)$ to $f_{N,type(j)}(s_j)$ (which is $\lambda_j^*$) is precisely what quantifies the change from that baseline due to the match at $j$.

So, the deduction shown in the image you screenshotted (which was my corrected rigorous derivation) remains algebraically sound even with type-specific $f_N$ functions, provided that $\lambda_k^*$ is understood to be $f_M(s_k)/f_{N,type(k)}(s_k)$. The complexity moves into defining and calculating each $f_{N,type(k)}(s_k)$, but the overall structure of the final odds ratio, after cancellation, is preserved.

#### Now The Deduction
Now, we address Steve's point by allowing the non-match likelihood $f_N(s_i)$ to be specific to the type of trace $i$, denoted $f_{N,type(i)}(s_i)$. This $f_{N,type(i)}(s_i)$ could itself be a mixture: $f_{N,type(i)}(s_i) = \sum_{k'} P(D_i=s_i \mid N_i, \text{subtype}=k')P(N_i \text{ is subtype } k')$.

Let $\lambda_k^* = \frac{f_M(s_k)}{f_{N,type(k)}(s_k)}$.

### Rigorous Derivation Steps (Type-Specific $f_N$)

The overall structure of the odds $\frac{P(D \mid O)}{P(D \mid N)}$ remains the same. The divergence occurs in the expansion of the product terms.

**2.1. Numerator: Likelihood $P(D \mid O)$ (Type-Specific $f_N$)**
$$
\begin{aligned}
P(D \mid O) \;&=\; \frac{1}{n} \sum_{j \in A} \left[ f_M(s_j) \prod_{\substack{i=1 \\ i \neq j}}^{M} f_{N,type(i)}(s_i) \right]
\end{aligned}
$$

**2.2. Denominator: Likelihood $P(D \mid N)$ (Type-Specific $f_N$)**
$$P(D \mid N) \;=\; x P(D \mid CF) \;+\; (1-x) P(D \mid NF)$$

* **2.2a. Likelihood $P(D \mid CF)$ (Confusing Foil, Type-Specific $f_N$):**
    $$
    \begin{aligned}
    P(D \mid CF) \;&=\; \frac{1}{n'_{phys}} \left( \sum_{j \in B_{act}} \left[ f_M(s_j) \prod_{\substack{i=1 \\ i \neq j}}^{M} f_{N,type(i)}(s_i) \right] + (n'_{phys} - n^{\dagger}) \prod_{i=1}^{M} f_{N,type(i)}(s_i) \right)
    \end{aligned}
    $$

* **2.2b. Likelihood $P(D \mid NF)$ (New Foil, Type-Specific $f_N$):**
    $$
    P(D \mid NF) \;=\; \prod_{i=1}^{M} f_{N,type(i)}(s_i)
    $$

**This is the point before cancellation where you would substitute the type-specific $f_{N,type(i)}(s_i)$ if you were to calculate without the $\lambda_k^*$ simplification.** If you proceed with the cancellation:

**2.3. Combine and Cancel Common Product $P_0^*(D) = \prod_{i=1}^{M} f_{N,type(i)}(s_i)$ (Type-Specific $f_N$)**

Define $\lambda_k^* = \frac{f_M(s_k)}{f_{N,type(k)}(s_k)}$. Any term $f_M(s_k) \prod_{i \neq k} f_{N,type(i)}(s_i)$ can be written as $\lambda_k^* P_0^*(D)$.

* $P(D \mid O) = \frac{1}{n} \sum_{j \in A} \lambda_j^* P_0^*(D)$
* $P(D \mid CF) = \frac{1}{n'_{phys}} \left( \sum_{j \in B_{act}} \lambda_j^* P_0^*(D) + (n'_{phys} - n^{\dagger}) P_0^*(D) \right)$
* $P(D \mid NF) = P_0^*(D)$

Substituting into $\frac{P(D \mid O)}{x P(D \mid CF) + (1-x) P(D \mid NF)}$:
$$
\begin{aligned}
\frac{P(O \mid D)}{P(N \mid D)} \;&=\; \frac{ \frac{1}{n} \sum_{j \in A} \lambda_j^* P_0^*(D) }{ x \left[ \frac{1}{n'_{phys}} \left( \sum_{j \in B_{act}} \lambda_j^* P_0^*(D) + (n'_{phys} - n^{\dagger}) P_0^*(D) \right) \right] + (1-x) P_0^*(D) } \\[2ex]
\;&=\; \frac{ \frac{1}{n} \sum_{j \in A} \lambda_j^* }{ x \left[ \frac{1}{n'_{phys}} \left( \sum_{j \in B_{act}} \lambda_j^* + (n'_{phys} - n^{\dagger}) \right) \right] + (1-x) } && \text{(Cancel } P_0^*(D) \text{ from all terms)} \\[2ex]
\;&=\; \frac{ \frac{1}{n} \sum_{j \in A} \lambda_j^* }{ x \left( \frac{1}{n'_{phys}} \sum_{j \in B_{act}} \lambda_j^* + \frac{n'_{phys} - n^{\dagger}}{n'_{phys}} \right) + (1-x) } && \text{(Distribute } 1/n'_{phys}\text{)}
\end{aligned}
$$

---

### Final Exact Odds Formula (With Type-Specific $f_N$)
This is the rigorous expression, now explicitly accommodating type-specific non-match likelihoods $f_{N,type(k)}(s_k)$ within each $\lambda_k^*$.

$$
\boxed{
\frac{P(O \mid D)}{P(N \mid D)} \;=\; \frac{\displaystyle \frac{1}{n} \sum_{k \in A} \frac{f_M(s_k)}{f_{N,type(k)}(s_k)}}{\displaystyle x \left( \frac{1}{n'_{phys}} \sum_{k \in B_{act}} \frac{f_M(s_k)}{f_{N,type(k)}(s_k)} + \frac{n'_{phys} - n^{\dagger}}{n'_{phys}} \right) + (1-x)}
}
$$

* Each $f_{N,type(k)}(s_k)$ in the denominator of $\lambda_k^*$ is specific to the type of non-matching trace $k$ (and could be a mixture as per Steve's suggestion).
* This formula is "accurate" in the sense that it correctly applies Bayes' theorem given these more nuanced likelihood definitions. The challenge shifts to defining and computing each $f_{N,type(k)}(s_k)$.