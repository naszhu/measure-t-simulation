## Original REM.1 Odds Derivation (Full)

This derivation shows how the REM.1 odds ($\Phi$) are calculated. It assumes "Old" targets ($O$) are defined as coming only from the $n$ items in the current study list, even if $M$ total traces are active in memory ($M \ge n$). New foils ($N$) match none of these current list items.

### Glossary:
* $M$: Total number of **activated** traces in memory. The observed data $D$ consists of $M$ similarity scores $s_1, \ldots, s_M$.
* $n$: Number of items in the **current study list**. All are assumed to be activated.
* $A$: Set of indices for the $n$ **current list traces** (so $|A|=n$). These are the only possible sources for a "Target."
* $O$: Event that the test item is an "Old" target.
* $N$: Event that the test item is a "New" foil.
* $D_j$: Data (e.g., similarity score $s_j$) from comparing the probe to activated trace $j$.
* $S_j$: Event that activated trace $j$ is the specific s-image (true match) for an Old probe.
* $N_j$: Event that activated trace $j$ is a d-image (non-match) for the probe.
* $f_M(s_j) = P(D_j|S_j)$: Likelihood of $s_j$ if trace $j$ is the s-image.
* $f_N(s_j) = P(D_j|N_j)$: Likelihood of $s_j$ if trace $j$ is a d-image (assumed uniform for all d-images here for simplicity, as in basic REM.1).
* $\lambda_j = f_M(s_j)/f_N(s_j)$: Likelihood ratio for trace $j$.

---

### Derivation Steps:

The posterior odds are given by Bayes' Theorem, assuming equal prior odds for an item being Old or New ($P_o(O)=P_o(N)$, so $P_o(O)/P_o(N) = 1.0$):
$$
\frac{P(O \mid D)}{P(N \mid D)} = \frac{P(D \mid O)}{P(D \mid N)} 
$$

#### 1. Numerator: $P(D \mid O)$ (Likelihood of data $D$ given the item is Old)
If the item is Old, it must correspond to one of the $n$ traces in set $A$. The prior probability that any specific trace $k \in A$ is the true s-image, given $O$, is $P(S_k|O) = 1/n$.
$$
\begin{aligned}
P(D \mid O) &= \sum_{k \in A} P(D \mid S_k \text{ is s-image}) P(S_k \text{ is s-image} \mid O) && \text{(Law of Total Probability over } k \in A\text{)} \\[1ex]
&= \sum_{k \in A} \left( f_M(s_k) \prod_{\substack{j=1 \\ j \neq k}}^{M} f_N(s_j) \right) \frac{1}{n} && \text{(If } S_k \text{ is match, } D_k \sim f_M; \text{ all other } M-1 \text{ activated traces are d-images, } D_j \sim f_N \text{)} \\[1ex]
&= \frac{1}{n} \sum_{k \in A} \left( f_M(s_k) \prod_{\substack{j=1 \\ j \neq k}}^{M} f_N(s_j) \right) && \text{(Rearranging terms)}
\end{aligned}
$$

#### 2. Denominator: $P(D \mid N)$ (Likelihood of data $D$ given the item is New)
If the item is a New foil, it does not match any of the $n$ current list items. With respect to the $M$ activated traces, all $M$ behave as d-images.
$$
P(D \mid N) = \prod_{j=1}^{M} f_N(s_j)
$$

#### 3. Explanation: Why Products Run Over All $M$ Activated Traces

* **Nature of Data $D$**: The observed data $D$ is the complete set of similarity scores $(s_1, s_2, \ldots, s_M)$ resulting from comparing the test probe to *all $M$ currently activated traces*. Any likelihood $P(D|\text{Hypothesis})$ must account for how all $M$ components of $D$ are generated under that hypothesis.

* **Numerator $P(D|O)$**:
    * When we consider the hypothesis that a specific current-list trace $k$ (where $k \in A$) is the s-image ($S_k$), this determines the distribution for $s_k$ (it's $f_M(s_k)$).
    * For this same hypothesis ($S_k$), all other $M-1$ activated traces (indexed by $j$, where $j \in \{1, \ldots, M\}$ and $j \neq k$) are considered d-images relative to the probe. This includes other current-list traces not matching $k$, as well as all activated prior-list traces.
    * Thus, the likelihood of their similarity scores $s_j$ is $f_N(s_j)$.
    * Assuming conditional independence, the joint likelihood of all $M$ scores given $S_k$ is $f_M(s_k) \times \prod_{j \neq k, j \text{ from } 1 \text{ to } M} f_N(s_j)$. The product correctly covers all $M-1$ other activated traces.

* **Denominator $P(D|N)$**:
    * If the test probe is a New foil, it is defined as not matching any of the $n$ current-list items. In the context of REM.1, this also implies it doesn't systematically match any of the prior-list traces either (they are all d-images by definition relative to a new, unrelated probe).
    * Therefore, under the "New foil" hypothesis, *all $M$ activated traces* yield similarity scores $s_j$ according to the non-match distribution $f_N(s_j)$.
    * Assuming conditional independence, the joint likelihood $P(D|N)$ is the product of these $M$ individual non-match likelihoods: $\prod_{j=1}^{M} f_N(s_j)$.

Both the numerator (for each term in its sum) and the denominator are constructed based on how the probe relates to the *entire set of $M$ activated traces*.

#### 4. Forming the Odds: The Role and Cancellation of the Common Product Term $P_0(D)$

To simplify the ratio $\frac{P(D|O)}{P(D|N)}$, we can identify a common component related to the "background noise" from all $M$ activated traces.

Let $P_0(D) = \prod_{j=1}^{M} f_N(s_j)$.
This $P_0(D)$ represents the likelihood of observing the entire data vector $D=(s_1, \ldots, s_M)$ if *all $M$ activated traces were non-matches* (d-images) of a uniform type. This is precisely the likelihood $P(D|N)$ as defined in Step 2.

Now, consider a single term from the sum in the numerator (from Step 1), where trace $k \in A$ is the s-image:
$$ \text{Term}_k = f_M(s_k) \prod_{\substack{j=1 \\ j \neq k}}^{M} f_N(s_j) $$
We can rewrite this by multiplying and dividing by $f_N(s_k)$ (assuming $f_N(s_k) \neq 0$):
$$ \text{Term}_k = \frac{f_M(s_k)}{f_N(s_k)} \times \left(f_N(s_k) \times \prod_{\substack{j=1 \\ j \neq k}}^{M} f_N(s_j)\right) $$
The expression in the large parentheses is simply the product of all $M$ non-match likelihoods, which is $P_0(D)$:
$$ f_N(s_k) \times \prod_{\substack{j=1 \\ j \neq k}}^{M} f_N(s_j) = \prod_{j=1}^{M} f_N(s_j) = P_0(D) $$
So, we have $\text{Term}_k = \frac{f_M(s_k)}{f_N(s_k)} P_0(D) = \lambda_k P_0(D)$.

Substituting this back into the expression for $P(D|O)$:
$$P(D \mid O) = \frac{1}{n} \sum_{k \in A} (\lambda_k P_0(D)) = \left( \frac{1}{n} \sum_{k \in A} \lambda_k \right) P_0(D)$$
And the denominator is $P(D \mid N) = P_0(D)$.

The odds ratio $\Phi$ is therefore:
$$
\Phi = \frac{P(O \mid D)}{P(N \mid D)} = \frac{\left( \frac{1}{n} \sum_{k \in A} \lambda_k \right) P_0(D)}{P_0(D)}
$$
The term $P_0(D) = \prod_{j=1}^{M} f_N(s_j)$, representing the joint likelihood of non-matches across all $M$ activated traces, appears as a common factor in both the numerator's expansion and the denominator. Thus, it **cancels out**:
$$
\boxed{
\Phi = \frac{1}{n} \sum_{k \in A} \lambda_k
}
$$
This final equation matches Equation 2 and the final step of Equation A2 in Shiffrin & Steyvers (1997). The crucial point is that $n$ (specifically $|A|$) is the size of the pool of potential targets, and the sum is over these $n$ traces. The influence of all $M$ activated traces is implicitly handled: they form the comprehensive "noise background" $P_0(D)$ that gets factored out, ensuring each $\lambda_k$ is evaluated against this complete background.