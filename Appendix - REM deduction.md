# Appendix A: Rigorous Probabilistic Derivation of REM Likelihood Ratios

## A.1 Introduction to Probabilistic Formalism in REM

This appendix provides a complete and rigorous derivation of the Retrieving Effectively from Memory (REM) likelihood ratios used in this dissertation. This level of mathematical detail, building from foundational probabilistic principles, is often condensed in standard presentations of REM. However, a full exposition is crucial for a foundational understanding of the model's assumptions and for systematically extending the model, particularly to incorporate different types of foils, such as confusing foils.

## A.2 Fundamental Probabilistic Setup

To formally derive the REM equations, we first define the underlying probabilistic structure.

### A.2.1 Sample Space ($\Omega$)

Let $\Omega$ be the sample space representing all possible elementary outcomes of a single recognition memory trial. An outcome $\omega \in \Omega$ encapsulates all relevant factors for a given trial, including:
* The true nature of the test probe, $T_p(\omega)$ (e.g., whether it corresponds to a previously studied item, and if so which one, or if it's an entirely new item).
* The set of $N$ memory traces $\{m_1, m_2, \dots, m_N\}$ currently active or available in memory. (Note: $N$ here represents the total number of traces considered in the model, which might be $n$ for a single list or $n+2zn$ if including context drift from $z$ prior lists, each contributing $2n$ traces, plus the current list of $n$ items).
* The resulting vector of $N$ similarity (or data) observations, $\mathbf{S}(\omega) = (S_1(\omega), S_2(\omega), \dots, S_N(\omega))$, where $S_j(\omega)$ represents the outcome of comparing the probe $T_p(\omega)$ with the memory trace $m_j$. For simplicity, we often denote the observed data vector as $\mathbf{s} = (s_1, \dots, s_N)$.

### A.2.2 Sigma-Algebra ($\mathcal{F}$)

Let $\mathcal{F}$ be an appropriate sigma-algebra defined on $\Omega$, containing all events of interest. If the similarity scores $S_j$ are continuous, $\mathcal{F}$ would typically be constructed to include pre-images of Borel sets in $\mathbb{R}^N$ under the mapping $\mathbf{S}:\Omega \to \mathbb{R}^N$, as well as events defining the nature of the test probe.

### A.2.3 Probability Measure ($P$)

$P$ is a probability measure defined on the measurable space $(\Omega, \mathcal{F})$.

### A.2.4 Key Random Variables and Events

* **Event $O$ (Old/Target):** The event that the test probe $T_p$ corresponds to an item previously studied and whose trace is among the $N$ memory traces.
* **Event $Foil$:** The event that the test probe $T_p$ does not correspond to a target item. This can be further broken down.
    * **Event $N_E$ (New/Pure New Foil):** The event that the test probe $T_p$ is entirely new and does not correspond to any of the $N$ memory traces.
    * **Event $C_F$ (Confusing Foil):** The event that the test probe $T_p$ is a foil that, by design, exactly matches one of the existing memory traces (typically from a specific subset of traces).
* **Event $S_k$:** The event that trace $m_k$ (from the set of $N$ active traces) is the specific memory trace that generated the target probe $T_p$.
* **Observed Data $D_j$ (or $s_j$):** The observed similarity value resulting from the comparison of the test probe $T_p$ with the $j$-th memory trace $m_j$. The vector of all such observations is $\mathbf{D}$ (or $\mathbf{s}$).
* **Likelihood Densities:**
    * $f_M(s_j) \equiv p(D_j=s_j \mid S_j, \text{trace } m_j \text{ is the source of the probe})$: The probability density function (pdf) of observing similarity $s_j$ for trace $m_j$ given that $m_j$ is a match to the probe.
    * $f_N(s_j) \equiv p(D_j=s_j \mid \neg S_j, \text{trace } m_j \text{ is not the source of the probe})$: The pdf of observing similarity $s_j$ for trace $m_j$ given that $m_j$ is a non-match to the probe.

## A.3 Derivation of Traditional REM Likelihood Ratio (No Confusing Foils)

In the traditional REM formulation, foils are assumed to be pure new foils ($N_E$). The goal is to derive the likelihood ratio $\Lambda_{\text{orig}}^{(N_T)}(\mathbf{s}) = \frac{P(\mathbf{s} \mid O)}{P(\mathbf{s} \mid N_E)}$, where $N_T$ is the number of traces in the pool considered for targets.

### A.3.1 Likelihood of Data Given Target ($P(\mathbf{s} \mid O)$)

We use the Law of Total Probability, summing over the mutually exclusive events $S_k$ (that trace $m_k$ was the source of the target):
$$
P(\mathbf{s} \mid O) = \sum_{k=1}^{N_T} P(\mathbf{s} \mid O, S_k) P(S_k \mid O)
$$
**Assumption 1 (Equal Prior for Target Source):** Any of the $N_T$ traces in the target pool is equally likely to be the source of the target probe.
$$
P(S_k \mid O) = \frac{1}{N_T}
$$
**Assumption 2 (Conditional Independence for Targets):** Given that trace $m_k$ is the source of the target ($S_k$), the similarity $S_k$ is drawn from $f_M(\cdot)$, and all other similarities $S_j$ (for $j \neq k$, $j \in \{1, \dots, N_T\}$) are drawn independently from $f_N(\cdot)$.
Thus,
$$
P(\mathbf{s} \mid O, S_k) = f_M(s_k) \prod_{j \neq k, j=1}^{N_T} f_N(s_j)
$$
Combining these, we get:
$$
P(\mathbf{s} \mid O) = \sum_{k=1}^{N_T} \left[ f_M(s_k) \prod_{j \neq k, j=1}^{N_T} f_N(s_j) \right] \cdot \frac{1}{N_T} = \frac{1}{N_T} \sum_{k=1}^{N_T} \left[ f_M(s_k) \prod_{j \neq k, j=1}^{N_T} f_N(s_j) \right]
$$

### A.3.2 Likelihood of Data Given New Foil ($P(\mathbf{s} \mid N_E)$)

**Assumption 3 (Nature of New Foils):** If the probe is a pure new foil, it does not match any of the $N_T$ memory traces.
**Assumption 4 (Conditional Independence for New Foils):** Given the probe is a new foil ($N_E$), all similarity scores $S_j$ (for $j \in \{1, \dots, N_T\}$) are drawn independently from $f_N(\cdot)$.
Thus,
$$
P(\mathbf{s} \mid N_E) = \prod_{j=1}^{N_T} f_N(s_j)
$$

### A.3.3 Likelihood Ratio ($\Lambda_{\text{orig}}^{(N_T)}$)

The likelihood ratio is:
$$
\Lambda_{\text{orig}}^{(N_T)}(\mathbf{s}) = \frac{P(\mathbf{s} \mid O)}{P(\mathbf{s} \mid N_E)} = \frac{\frac{1}{N_T} \sum_{k=1}^{N_T} \left[ f_M(s_k) \prod_{j \neq k, j=1}^{N_T} f_N(s_j) \right]}{\prod_{j=1}^{N_T} f_N(s_j)}
$$
Each term in the sum in the numerator is $f_M(s_k) \prod_{j \neq k} f_N(s_j)$. Dividing this by the denominator $\prod_{j=1}^{N_T} f_N(s_j) = f_N(s_k) \prod_{j \neq k} f_N(s_j)$ yields $\frac{f_M(s_k)}{f_N(s_k)}$.
Thus,
$$
\Lambda_{\text{orig}}^{(N_T)}(\mathbf{s}) = \frac{1}{N_T} \sum_{k=1}^{N_T} \frac{f_M(s_k)}{f_N(s_k)}
$$

## A.4 Derivation of Extended REM Likelihood Ratio (With Confusing Foils)

Now, we consider foils that can be either "confusing foils" ($C_F$) with prior probability $x$ (given it's a foil trial), or "pure new foils" ($N_E$) with prior probability $(1-x)$. The total pool of traces considered for target generation is $N_T$. The pool of traces from which confusing foils can be drawn is $A_C$, with size $|A_C| = N_C$. The likelihood of data given a target, $P(\mathbf{s} \mid O)$, remains as derived in A.3.1 (using $N_T$).

### A.4.1 Likelihood of Data Given Foil ($P(\mathbf{s} \mid \text{Foil})$) - Now a Mixture

By the Law of Total Probability, conditioning on the type of foil:
$$
P(\mathbf{s} \mid \text{Foil}) = P(\mathbf{s} \mid C_F)P(C_F \mid \text{Foil}) + P(\mathbf{s} \mid N_E)P(N_E \mid \text{Foil})
$$
Given $P(C_F \mid \text{Foil}) = x$ and $P(N_E \mid \text{Foil}) = (1-x)$.
The term $P(\mathbf{s} \mid N_E)$ is from A.3.2 (though here, non-matches are against all $N_T$ traces, so the product is over $N_T$):
$$
P(\mathbf{s} \mid N_E) = \prod_{j=1}^{N_T} f_N(s_j)
$$
For $P(\mathbf{s} \mid C_F)$:
**Assumption 5 (Nature of Confusing Foils):** A confusing foil exactly matches one specific trace $m_k$ from a predefined pool $A_C$ of $N_C$ traces.
**Assumption 6 (Equal Prior for Confusing Foil Source):** Any trace $m_k \in A_C$ is equally likely to be the source of the confusing foil.
$$P(S_k \mid C_F) = \frac{1}{N_C} \quad \text{for } k \in A_C$$
**Assumption 7 (Conditional Independence for Confusing Foils):** Given that trace $m_k \in A_C$ is the source of the confusing foil ($S_k$), the similarity $S_k$ is drawn from $f_M(\cdot)$, and all other similarities $S_j$ (for $j \neq k$, $j \in \{1, \dots, N_T\}$) are drawn independently from $f_N(\cdot)$.
Thus, $P(\mathbf{s} \mid C_F, S_k) = f_M(s_k) \prod_{j \neq k, j=1}^{N_T} f_N(s_j)$.
So, by Law of Total Probability for $P(\mathbf{s} \mid C_F)$:
$$
P(\mathbf{s} \mid C_F) = \sum_{k \in A_C} P(\mathbf{s} \mid C_F, S_k) P(S_k \mid C_F) = \frac{1}{N_C} \sum_{k \in A_C} \left[ f_M(s_k) \prod_{j \neq k, j=1}^{N_T} f_N(s_j) \right]
$$
Combining these for $P(\mathbf{s} \mid \text{Foil})$:
$$
P(\mathbf{s} \mid \text{Foil}) = x \left( \frac{1}{N_C} \sum_{k \in A_C} \left[ f_M(s_k) \prod_{j \neq k, j=1}^{N_T} f_N(s_j) \right] \right) + (1-x) \left( \prod_{j=1}^{N_T} f_N(s_j) \right)
$$

### A.4.2 Likelihood Ratio (Extended REM, $\Lambda_{\text{mix}}$)

The likelihood ratio for the extended model is $\Lambda_{\text{mix}}(\mathbf{s}) = \frac{P(\mathbf{s} \mid O)}{P(\mathbf{s} \mid \text{Foil})}$.
$$
\Lambda_{\text{mix}}(\mathbf{s}) = \frac{
    \frac{1}{N_T} \sum_{k=1}^{N_T} \left[ f_M(s_k) \prod_{j \neq k, j=1}^{N_T} f_N(s_j) \right]
}{
    x \left( \frac{1}{N_C} \sum_{k \in A_C} \left[ f_M(s_k) \prod_{j \neq k, j=1}^{N_T} f_N(s_j) \right] \right) + (1-x) \left( \prod_{j=1}^{N_T} f_N(s_j) \right)
}
$$
To simplify, we divide both the numerator and the denominator by $\prod_{j=1}^{N_T} f_N(s_j)$.

The numerator becomes:
$$
\frac{
    \frac{1}{N_T} \sum_{k=1}^{N_T} \left[ f_M(s_k) \prod_{j \neq k, j=1}^{N_T} f_N(s_j) \right]
}{
    \prod_{j=1}^{N_T} f_N(s_j)
}
= \frac{1}{N_T} \sum_{k=1}^{N_T} \frac{f_M(s_k)}{f_N(s_k)} \equiv \Lambda_{\text{orig}}^{(N_T)}(\mathbf{s})
$$
The first term in the denominator (the confusing foil component) becomes:
$$
\frac{
    x \left( \frac{1}{N_C} \sum_{k \in A_C} \left[ f_M(s_k) \prod_{j \neq k, j=1}^{N_T} f_N(s_j) \right] \right)
}{
    \prod_{j=1}^{N_T} f_N(s_j)
}
= x \left( \frac{1}{N_C} \sum_{k \in A_C} \frac{f_M(s_k)}{f_N(s_k)} \right) \equiv x \cdot \Lambda_{\text{orig}}^{(A_C)}(\mathbf{s})
$$
The second term in the denominator (the pure new foil component) becomes:
$$
\frac{
    (1-x) \left( \prod_{j=1}^{N_T} f_N(s_j) \right)
}{
    \prod_{j=1}^{N_T} f_N(s_j)
}
= (1-x)
$$
Thus, the final likelihood ratio for the extended REM with confusing foils is:
$$
\Lambda_{\text{mix}}(\mathbf{s}) = \frac{\Lambda_{\text{orig}}^{(N_T)}(\mathbf{s})}{x \cdot \Lambda_{\text{orig}}^{(A_C)}(\mathbf{s}) + (1-x)}
$$
If the pool of traces from which targets can arise ($N_T$) and the pool from which confusing foils can arise ($A_C$, size $N_C$) are identical, such that $N_T = N_C = N$, this formula simplifies to:
$$
\Lambda_{\text{mix}}^{(N)}(\mathbf{s}) = \frac{\Lambda_{\text{orig}}^{(N)}(\mathbf{s})}{x \cdot \Lambda_{\text{orig}}^{(N)}(\mathbf{s}) + (1-x)}
$$
where $\Lambda_{\text{orig}}^{(N)}(\mathbf{s}) = \frac{1}{N} \sum_{k=1}^{N} \frac{f_M(s_k)}{f_N(s_k)}$.

## A.5 Discussion of Approximations (Optional)

It is worth noting that alternative heuristic approaches to incorporating confusing foils exist, such as the "per-trace mixture then average" method discussed previously:
$$
\Lambda_{\text{approx}}(\mathbf{s}) = \frac{1}{N_T} \sum_{j=1}^{N_T} \frac{f_M(s_j)}{x \cdot f_M(s_j) + (1-x) \cdot f_N(s_j)}
$$
This formulation differs from the rigorous joint-likelihood derivation presented above because it applies the mixture proportion $x$ at the level of individual trace likelihoods before averaging, rather than at the level of the overall foil likelihood. The rigorous derivation accounts for the joint probability of the entire set of observations under each hypothesis before forming the ratio.