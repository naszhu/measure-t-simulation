### Original REM.1 Odds Derivation: Targets from Current List Only

This derivation shows how the REM.1 odds are calculated when "Old" targets are defined as coming only from the $n$ items in the current study list, even if $M$ total traces are active in memory ($M \ge n$).

**Glossary:**
* $M$: Total number of **activated** traces in memory. The observed data $D$ consists of $M$ similarity scores $s_1, \ldots, s_M$.
* $n$: Number of items in the **current study list**. All are assumed to be activated.
* $A$: Set of indices for the $n$ **current list traces** (so $|A|=n$). These are the only possible sources for a "Target."
* $O$: Event that the test item is an "Old" target (i.e., it matches one of the $n$ traces in set $A$).
* $N$: Event that the test item is a "New" foil (i.e., it matches none of the $n$ traces in set $A$; with respect to the $M$ active traces, all are d-images).
* $D_j$: Data (e.g., similarity score $s_j$) from comparing the probe to activated trace $j$.
* $S_j$: Event that activated trace $j$ is the specific s-image (true match) for an Old probe.
* $N_j$: Event that activated trace $j$ is a d-image (non-match) for the probe.
* $f_M(s_j) = P(D_j|S_j)$: Likelihood of $s_j$ if trace $j$ is the s-image.
* $f_N(s_j) = P(D_j|N_j)$: Likelihood of $s_j$ if trace $j$ is a d-image (assumed uniform for all d-images here).
* $\lambda_j = f_M(s_j)/f_N(s_j)$: Likelihood ratio for trace $j$.

---

**Derivation Steps:**

The posterior odds are given by Bayes' Theorem (assuming equal prior odds $P_o(O)=P_o(N)$):
$$
\frac{P(O \mid D)}{P(N \mid D)} = \frac{P(D \mid O)}{P(D \mid N)}
$$

**1. Numerator: $P(D \mid O)$ (Likelihood of data $D$ given the item is Old)**
If the item is Old, it must correspond to one of the $n$ traces in set $A$. The prior probability that any specific trace $k \in A$ is the true s-image, given $O$, is $P(S_k|O) = 1/n$.
$$
\begin{aligned}
P(D \mid O) &= \sum_{k \in A} P(D \mid S_k \text{ is s-image}) P(S_k \text{ is s-image} \mid O) && \text{(Law of Total Probability over } k \in A\text{)} \\
&= \sum_{k \in A} \left( f_M(s_k) \prod_{\substack{j=1 \\ j \neq k}}^{M} f_N(s_j) \right) \frac{1}{n} && \text{(If } S_k \text{ is match, } D_k \sim f_M; \text{ all other } M-1 \text{ activated traces are d-images, } D_j \sim f_N \text{)} \\
&= \frac{1}{n} \sum_{k \in A} \left( f_M(s_k) \prod_{\substack{j=1 \\ j \neq k}}^{M} f_N(s_j) \right)
\end{aligned}
$$

**2. Denominator: $P(D \mid N)$ (Likelihood of data $D$ given the item is New)**
If the item is a New foil, it does not match any of the $n$ current list items (by definition of "New" in this context), and thus all $M$ activated traces behave as d-images with respect to this New probe.
$$
P(D \mid N) = \prod_{j=1}^{M} f_N(s_j)
$$

**3. Forming the Odds and Cancelling:**
Let $P_0(D) = \prod_{j=1}^{M} f_N(s_j)$.
We can rewrite the term from the numerator: $f_M(s_k) \prod_{\substack{j=1 \\ j \neq k}}^{M} f_N(s_j) = \frac{f_M(s_k)}{f_N(s_k)} \prod_{j=1}^{M} f_N(s_j) = \lambda_k P_0(D)$.

So,
$$P(D \mid O) = \left( \frac{1}{n} \sum_{k \in A} \lambda_k \right) P_0(D)$$
And the denominator is $P(D \mid N) = P_0(D)$.

The odds ratio becomes:
$$
\frac{P(O \mid D)}{P(N \mid D)} = \frac{\left( \frac{1}{n} \sum_{k \in A} \lambda_k \right) P_0(D)}{P_0(D)}
$$
Cancelling the common term $P_0(D)$:
$$
\boxed{
\Phi = \frac{P(O \mid D)}{P(N \mid D)} = \frac{1}{n} \sum_{k \in A} \lambda_k
}
$$
Here, $n$ is the number of items in the current list (i.e., $|A|$), and the sum is over these $n$ current list traces. The existence of $M-n$ other activated traces (from prior lists) is accounted for because they formed part of the $P_0(D)$ product that was cancelled. They contribute to the "noise floor" against which the current list items are evaluated.