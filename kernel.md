
## difference between kernel and marginal distribution

| **Concept**               | **Definition**                                                                                                                                   | **Example**                                                   |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------- |
| **Kernel**                | A function $k: \mathcal{A} \times \mathscr{B} \to [0,1]$ where:  <br>1. $k(a,\cdot)$ is a probability measure  <br>2. $k(\cdot,B)$ is measurable | $k(\theta, A) = P(X \in A \mid \theta)$ (Bayesian likelihood) |
| **Marginal Distribution** | Obtained by integrating/summing over other variables: $P_X(A) = \int P_{X,Y}(A \times dy)$                                                       | $P_X([160,170]) = \sum_{y} P_{X,Y}([160,170], y)$             |

- Given (Θ, B_Θ) and (𝒳, B_𝒳), a kernel k: Θ × B_𝒳 → [0,1] satisfies:
    
    1. For fixed θ $\in\Theta$ , k(θ, ·) is a probability measure on 𝒳
        
    2. For fixed A ∈ B_𝒳, k(·, A) is measurable
        
- **Bayesian likelihood**: Kernel from Θ to 𝒳
    
    - k(θ, A) = P_X(X ∈ A | θ)
        
- **Frequentist likelihood**: Function L(θ; x), **not** a kernel (θ is fixed)

###  Bayesian Inference: Kernels vs. Joint Distributions
**Kernel perspective** (more general):

- Prior: $P_\theta$ (measure on $\Theta$)
    
- Likelihood: Kernel $k: \Theta \times \mathscr{B}_{\mathcal{X}} \to [0,1]$
    
- Posterior: Kernel $q: \mathcal{X} \times \mathscr{B}_{\Theta} \to [0,1]$

(what is given is write at first as the space, and the sigma algebra is for unknown)

**Joint distribution perspective**:

- Define joint measure on $\Theta \times \mathcal{X}$:  
    $P_{θ,X}(C×A)=∫_Ck(θ,A)dP_θ(θ)$
    
- Posterior obtained via conditioning