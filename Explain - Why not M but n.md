## Section 2: Original REM.1 with an Expanded View of Active Traces ($M$)

I think, If assuming OLD item's prior (the design) comes from all traces, including both possibly current list traces and past list traces; then, the number used in REM equation should be total number of activated traces M; but if assume OLD only come from current list theoretically, the n use should actually be number of activated traces in current list. 

The main root reason is:

- If an "Old" item is strictly defined as originating from the $n$ items of the **current** study list, then the correct averaging factor in the odds formula is $1/n$, and the sum is over these $n$ traces. If "Old" item is assumed to possibly come from total activated traces including prior traces, then probably the denominator could use M; but, its unsure if 1/M is the prior for  
* The total number of activated traces, $M$, influences the "noise background" ($P_0(D)$ which cancels out) but doesn't change the $1/n$ factor as long as the definition of "Old" is restricted to the current list.


%% the n used in the original REM odds equation, is actually derived from the prior of probability for the old items to be drawn from the list. And the total number of activated traces M (including prior traces) are used during the deduction during expansion of  $P(D|S_j)$ and $P(D|N_j)$ into $\prod_{\substack{j=1 \\ j \neq k}}^{M} f_N(s_j)$ and $\prod_{\substack{j=1 \\ j \neq k}}^{M}$; the theoretical sample size of the data space is M, but it will be cancelled out here.

* $f_M(s_j) = P(D_j|S_j)$: Likelihood of $s_j$ if trace $j$ is the s-image.
* $f_N(s_j) = P(D_j|N_j)$: Likelihood of $s_j$ if trace $j$ is a d-image (assumed uniform for all d-images here). %%

### Key Question: What "$n$" to use in $\Phi = \frac{1}{\text{count}} \sum \lambda_j$?

The email discussion highlights that if $M$ traces are active, using $n_{current\_list}$ as "count" might be problematic if the "Old" hypothesis should consider all $M$ traces.

**Derivation when Targets are ONLY from the Current List ($n$ items, forming set $A$):**

1.  **Numerator $P(D|O)$**: If an item is "Old" (from current list $A$), the prior probability that any specific trace $k \in A$ is the true source is $1/n$. The likelihood $P(D|O)$ is an average over these $n$ possibilities:
    $$P(D|O) = \frac{1}{n} \sum_{k \in A} \left( f_M(s_k) \prod_{\substack{j=1 \\ j \neq k}}^{M} f_N(s_j) \right)$$
    Here, the product $\prod f_N(s_j)$ runs over all $M-1$ other *activated* traces, which act as d-images.

2.  **Denominator $P(D|N)$**: If the item is a new foil, all $M$ activated traces are d-images:
    $$P(D|N) = \prod_{j=1}^{M} f_N(s_j)$$

3.  **Odds $\Phi$**:
    Let $P_0(D) = \prod_{j=1}^{M} f_N(s_j)$.
    We can rewrite $P(D|O) = \left( \frac{1}{n} \sum_{k \in A} \frac{f_M(s_k)}{f_N(s_k)} \right) P_0(D) = \left( \frac{1}{n} \sum_{k \in A} \lambda_k \right) P_0(D)$.
    Then,
    $$\Phi = \frac{P(D|O)}{P(D|N)} = \frac{\left( \frac{1}{n} \sum_{k \in A} \lambda_k \right) P_0(D)}{P_0(D)} = \frac{1}{n} \sum_{k \in A} \lambda_k$$

**Conclusion for This Scenario:**

* If an "Old" item is strictly defined as originating from the $n$ items of the current study list (set $A$), then the correct averaging factor in the odds formula is $1/n$, and the sum is over these $n$ traces.
* The total number of activated traces, $M$, influences the "noise background" ($P_0(D)$ which cancels out) but doesn't change the $1/n$ factor as long as the definition of "Old" is restricted to the current list.

**Reconciling with the Email's Recommendation (use $M$ as the divisor):**

* The email's suggestion to use $M$ (total activated traces) as the divisor in $\Phi = \frac{1}{M} \sum_{k=1}^{M} \lambda_k$ is most appropriate if the definition of an "Old" item is broadened. If "Old" means the item matches *any one of the $M$ currently activated traces* (regardless of its original list), and each of these $M$ traces is an equally likely source, then the prior $P(S_k|O)$ becomes $1/M$, and the derivation naturally leads to $\Phi = \frac{1}{M} \sum_{k=1}^{M} \lambda_k$.
* The email's concern about using an $n$ that is "too small" (e.g., current list length when $M$ is much larger) leading to distorted Hit/CR rates is pertinent if one assumes the sum of $\lambda_k$ should implicitly cover evidence from all $M$ traces, but the division factor doesn't match.

Therefore, the choice of divisor ($n$ vs. $M$) in the final odds formula depends critically on how an "Old" item is defined relative to the pool of $M$ activated traces.