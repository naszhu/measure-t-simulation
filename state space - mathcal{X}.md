# definitions
However, if you're modeling **random variables**:

- $X: \Omega -> \mathcal{X}$
    
- Then $\mathcal{X}$ is the **state space of the random variable** $X$ — the set of all values it can take.

Common names for X
![[Pasted image 20250729010317.png]]
# important
- If the context is **underlying probability experiment**:  
    → **State space = $\Omega$**(space of elementary outcomes)
    
- If the context is **random variable modeling**:  
    → **State space = $\mathcal{X}$** ([range of the random variable])

# more deifinition
[[data space x]]
it's called [[feature space]] as well

- **Formal term**: The space - $\mathcal{X}$ is called the **state space** or [**outcome space**] of the random variable X.
- - X:Ω→XX:Ω→X is a measurable function mapping outcomes to a concrete space XX (e.g., RnRn).
![[Pasted image 20250728190930.png]]


- Probability theory **does not** use the term "feature space" (an ML/statistics term).
    
- $\mathcal{X}$ is the **[[codomain]]** of X, where probability distributions are defined.

## differentiation vs. data
1. **State space vs. data**:
    
    - 𝒳 = set of possible data values (e.g., ℝ for heights)
        
    - **Data** = realized values {x₁,...,xₙ} ⊂ 𝒳
# side Q
[[feature dimensions]] (x, y, z,... the axis)


could be feature space of [[feature vector]] and also for [[Configuration - X]]..?? really? rigerously mathemtaically? [[Question]],

=> well, sort of makes sense, because they are all some description of the "data space", not sample space 

[[Question]]: is [[similarity space]] a kind of feature space as well? (i think so)

# notation
### Notation: _X_ vs  _X(ω)_

- **X** (capital)**:** the _function / random variable_.
    
- **X(ω)**: the _realised value_ after ω is fixed.  
    Authors sometimes say “let X ~ N(μ,σ²)” as shorthand for “the distribution induced by X on ℝ is Normal(μ,σ²)”. Strictly, one should write “PXP_XPX​ is Normal(μ,σ²)”.