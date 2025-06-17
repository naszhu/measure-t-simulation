## Original REM.1 Odds Derivation (Considering $M$ Activated Traces)

This derivation details how the original REM.1 odds ($\Phi$) are calculated. It specifically addresses the scenario where "Old" targets ($O$) are defined as coming *only* from the $n$ items in the current study list, even if a larger set of $M$ total traces are active in memory ($M \ge n$) due to accumulation from prior lists or other factors. New foils ($N$) are assumed to match none of these $n$ current list items. The derivation will clarify how the total number of activated traces ($M$) is accounted for, and why the final averaging factor pertains to the size of the target pool ($n$).

### Glossary of Terms
* $M$: Total number of **activated** traces in memory at the time of test. The observed data $D$ consists of $M$ similarity scores $s_1, \ldots, s_M$.
* $n$: Number of items physically present in the **current study list**. We assume all $n$ of these items have corresponding traces that are activated.
* $A$: The set of indices corresponding to the $n$ **current list traces** which are activated. Thus, $|A|=n$. These are the only possible sources for an "Old" target in this specific model.
* $O$: The event that the test item is an "Old" target (i.e., it matches one of the $n$ traces in set $A$).
* $N$: The event that the test item is a "New" foil (i.e., it does not match any of the $n$ traces in set $A$; consequently, with respect to the $M$ active traces, all are treated as d-images).
* $D$: The observed data vector, $D = (s_1, s_2, \ldots, s_M)$, comprising similarity scores from all $M$ activated traces.
* $D_j$: The data component (e.g., similarity score $s_j$) from comparing the test probe to the $j^{th}$ activated trace (where $j \in \{1, \ldots, M\}$).
* $S_j$: The event that activated trace $j$ is the specific s-image (the true, matching trace) for an Old probe. This can only occur if $j \in A$.
* $N_j$: The event that activated trace $j$ is a d-image (a non-matching trace) with respect to the probe.
* $f_M(s_j) = P(D_j=s_j|S_j)$: The likelihood (density) of observing similarity $s_j$ for trace $j$ if it is the s-image.
* $f_N(s_j) = P(D_j=s_j|N_j)$: The likelihood (density) of observing similarity $s_j$ for trace $j$ if it is a d-image. For the basic REM.1, this is assumed to be a uniform function for all d-images.
* $\lambda_j = f_M(s_j)/f_N(s_j)$: The likelihood ratio for activated trace $j$.

---

### 1. Formal Probabilistic Setup for REM.1

To provide a rigorous foundation, we define the probabilistic framework:

* **Sample Space ($\Omega$)**: This is the set of all possible elementary outcomes of a single recognition trial. An outcome $\omega \in \Omega$ implicitly defines:
    1.  $T_{state}(\omega)$: The true nature of the test item, $T_{state} \in \{O, N\}$.
    2.  If $T_{state}=O$, $S_{source}(\omega)$: Which of the $n$ current list items ($m_1, \ldots, m_n$) is the source.
    3.  $D(\omega)$: The complete data vector $(s_1, \ldots, s_M)$ from comparing the probe to all $M$ activated traces.
    Effectively, $\Omega$ can be thought of as enabling the definition of these random outcomes.

* **Sigma-Algebra ($\mathcal{F}$)**: A collection of subsets of $\Omega$ (events) for which probabilities are defined, satisfying closure properties. It includes events like $\{T_{state}=O\}$, $\{S_{source}=m_k \text{ given } O\}$, and $\{D \in B\}$ for Borel sets $B \subseteq \mathbb{R}^M$.

* **Probability Measure ($P$)**: A function assigning probabilities to events in $\mathcal{F}$.

* **Random Variables**:
    1.  **$T_{state}$**: A discrete random variable, $T_{state}: \Omega \to \{O, N\}$.
    2.  **$S_{source}$** (conditional on $T_{state}=O$): A discrete random variable, $S_{source}: \Omega \to A$. For $k \in A$, $P(S_{source}=k | T_{state}=O) = 1/n$.
    3.  **$D = (D_1, \ldots, D_M)$**: A continuous random vector, $D: \Omega \to \mathbb{R}^M$. Each $D_j$ (representing $s_j$) is a real-valued similarity score. $\mathbb{R}^M$ is equipped with its Borel sigma-algebra $\mathcal{B}(\mathbb{R}^M)$.

* **Conditional Likelihoods**:
    The derivation uses conditional probability density functions $P(D=\mathbf{s} \mid O)$ and $P(D=\mathbf{s} \mid N)$.
    * $P(D_j=s_j \mid S_j \text{ (trace } j \text{ is match)})$: This is $f_M(s_j)$.
    * $P(D_j=s_j \mid N_j \text{ (trace } j \text{ is non-match)})$: This is $f_N(s_j)$.

---
### Derivation Steps for REM.1 Odds ($\Phi$)

The posterior odds are given by Bayes' Theorem. Assuming equal prior odds for an item being Old or New ($P_o(O) = P_o(N)$, so their ratio is 1.0):
$$
\Phi = \frac{P(O \mid D)}{P(N \mid D)} = \frac{P(D \mid O)}{P(D \mid N)}
$$

#### 2. Numerator: $P(D \mid O)$ (Likelihood of data $D$ given the item is Old)
An "Old" item, by this model's definition, originates from one of the $n$ items in the current study list (set $A$). All $n$ items in $A$ are assumed to be among the $M$ activated traces. Given $O$, each of these $n$ items is equally likely to be the specific source of the target.
$$
\begin{aligned}
P(D \mid O) &= \sum_{k \in A} P(D \mid S_k \text{ is the s-image}) P(S_k \text{ is the s-image} \mid O) && \text{(Law of Total Probability: summing over which of the } n \text{ traces in } A \text{ is the true source.)} \\[1ex]
&= \sum_{k \in A} P(D \mid S_k) \cdot \frac{1}{n} && \text{(Given } O\text{, the prior for any } k \in A \text{ being the source is } 1/n \text{.)} \\[1ex]
&= \frac{1}{n} \sum_{k \in A} P(D \mid S_k) && \text{(Rearranging the constant } 1/n \text{.)} \\[1ex]
&= \frac{1}{n} \sum_{k \in A} \left( f_M(s_k) \prod_{\substack{j=1 \\ j \neq k}}^{M} f_N(s_j) \right) && \text{(Conditional Independence: If trace } k \text{ is the s-image ($S_k$), its data } D_k \text{ for similarity } s_k \text{ is drawn from } f_M(s_k)\text{. All other } M-1 \\&&& \text{activated traces } (j \neq k) \text{ are d-images ($N_j$), and their data } D_j \text{ for similarities } s_j \text{ are drawn independently from } f_N(s_j)\text{.)}
\end{aligned}
$$

#### 3. Denominator: $P(D \mid N)$ (Likelihood of data $D$ given the item is New)
If the item is a New foil, it does not match any of the $n$ current list items by definition. Consequently, all $M$ activated traces (including those from the current list and any from prior lists) behave as d-images with respect to this New probe.
$$
P(D \mid N) = \prod_{j=1}^{M} f_N(s_j) 
$$
All  $M$ activated traces are d-images ($N_j$), so their data  $D_j$ for similaritie $s_j$ are drawn independently from  $f_N(s_j)$

#### 4. Explanation: Why Product Terms Run Over All $M$ Activated Traces

* **Data $D$ is Comprehensive**: The observed data $D$ that the system uses for its decision is the full vector of $M$ similarity scores $(s_1, s_2, \ldots, s_M)$, derived from comparing the probe to *all $M$ traces currently active in memory*. Therefore, any likelihood expression for $D$, such as $P(D|\text{Hypothesis})$, must explain the origin of all $M$ of these scores under that hypothesis.

* **For $P(D|O)$ (given $S_k$ is the s-image from set $A$):**
    * The similarity $s_k$ for the matching trace $k$ comes from $f_M(s_k)$.
    * For *all other $M-1$ activated traces* (indexed $j \neq k$, where $j$ spans $1 \ldots M$), they are non-matches (d-images). This includes the $n-1$ other current list traces and all $M-n$ activated prior list traces. Each of their similarities $s_j$ comes from $f_N(s_j)$.
    * The joint likelihood is thus $f_M(s_k)$ multiplied by the product of $M-1$ terms of $f_N(s_j)$.

* **For $P(D|N)$:**
    * If the probe is a New foil, it doesn't match any of the current list items. It's also assumed not to systematically match any prior list items (i.e., all prior list items are also d-images relative to a truly new probe).
    * Therefore, all $M$ activated traces produce similarity scores $s_j$ according to $f_N(s_j)$.
    * The joint likelihood is the product of all $M$ of these $f_N(s_j)$ terms.

This shows that both the numerator terms (before summing) and the denominator term inherently consider the contributions (or lack thereof, in the case of $f_N$) from all $M$ activated traces to the overall data vector $D$.

#### 5. Forming the Odds: The Role and Cancellation of the Common Product Term $P_0(D)$

To simplify the ratio $\frac{P(D|O)}{P(D|N)}$, we identify a common component.
Let $P_0(D) = \prod_{j=1}^{M} f_N(s_j)$. This $P_0(D)$ is the likelihood of the data vector $D$ if all $M$ activated traces were non-matches. This is exactly $P(D|N)$.

Now, consider a single term from the sum in the numerator for $P(D|O)$, where trace $k \in A$ is the s-image:
$$ \text{Term}_k = f_M(s_k) \prod_{\substack{j=1 \\ j \neq k}}^{M} f_N(s_j) $$
This can be rewritten by noting that $\prod_{\substack{j=1 \\ j \neq k}}^{M} f_N(s_j) = \frac{\prod_{j=1}^{M} f_N(s_j)}{f_N(s_k)} = \frac{P_0(D)}{f_N(s_k)}$.
So, $\text{Term}_k = f_M(s_k) \frac{P_0(D)}{f_N(s_k)} = \frac{f_M(s_k)}{f_N(s_k)} P_0(D) = \lambda_k P_0(D)$.

Substituting this back into the expression for $P(D|O)$:
$$P(D \mid O) = \frac{1}{n} \sum_{k \in A} (\lambda_k P_0(D)) = \left( \frac{1}{n} \sum_{k \in A} \lambda_k \right) P_0(D)$$
The denominator is $P(D \mid N) = P_0(D)$.

The odds ratio $\Phi$ is therefore:
$$
\Phi = \frac{P(O \mid D)}{P(N \mid D)} = \frac{\left( \frac{1}{n} \sum_{k \in A} \lambda_k \right) P_0(D)}{P_0(D)}
$$
The common factor $P_0(D) = \prod_{j=1}^{M} f_N(s_j)$, representing the joint likelihood of non-matches across all $M$ activated traces, cancels from the numerator and denominator:
$$
\boxed{
\Phi = \frac{1}{n} \sum_{k \in A} \lambda_k
}
$$
This is the classic REM.1 formula (Equation 2 in Shiffrin & Steyvers, 1997).
The divisor $n$ (size of set $A$) is correct because the "Old" hypothesis is restricted to items from the current list. The $M$ activated traces provide the full context for calculating individual $\lambda_k$ values (as $P_0(D)$ involved all $M$ traces before cancellation). If the definition of "Old" were expanded to include any of the $M$ activated traces as potential sources with prior $1/M$, then the divisor and sum limit would become $M$.