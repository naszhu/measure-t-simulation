[[Stochastic Process]]
[[decision making]]

[[racing model]]

[[Poisson racing model]]

[[drift diffusion model (DDM)]]
[[Leaky Competitive Accumulator (LCA)]]
[[Linear Ballistic Model (LBA)]]

The following is a similarity based sampling process (each step based on similarity sampling)  
[[Examplar Based Random Walk Model (EBRW)]]

## Q： what's the [[evidence]]


## Deep of unified frame
## 1.1 Latent world and sensory encoding

θ∼p(θ),x∼p(x∣θ).\theta \sim p(\theta), \qquad x \sim p(x\mid \theta).θ∼p(θ),x∼p(x∣θ).

This introduces **sensory noise** (variability in xxx even for the same θ\thetaθ).

## 1.2 An internal “evidence statistic”

Define a _target_ evidence statistic you’d want _if you were ideal_: often a (scaled) log-likelihood ratio (LLR) or a posterior functional,

$ϕ^⋆(x)  =  {\log\frac{p(x\mid \theta_1)}{p(x\mid \theta_2)}}_{\text{LLR example}}\quad\text{or}\quad \phi^\star(x)=\mathbb{E}[g(\theta)\mid x]$

### Difference bewteen EVA and [[auto-correlated Bayesian sampler (ABS)]] 
**Unification:** both are stochastic processes that aim to approximate ϕ⋆(x)\phi^\star(x)ϕ⋆(x), but EAM perturbs a **signal**; ABS estimates a **distributional functional**.


## Q: Is this a conscious or unconscious process?
[[consciousness]]

#### Unconscious Process View

**Proponents:** Schurger, Ratcliff, Smith
**Evidence accumulation:** Happens below consciousness threshold
**Consciousness:** Only aware of final decision
**Neural basis:** Subcortical, automatic


#### Conscious Control View

**Proponents:** Gold & Shadlen, Heekeren
**Evidence accumulation:** Can be consciously monitored
**Working Memory:** Holds intermediate evidence states
**Neural basis:** Prefrontal cortex, conscious access


#### Hybrid View (Most Common)

**Process:** Evidence accumulation is mostly unconscious
**Awareness:** Can become conscious with effort/attention
**Working Memory:** Interface between unconscious and [conscious]
**Control:** Top-down bias setting is conscious

**Mathematical Models Reflect This:**  
• Evidence accumulation: dx = μdt + σdW (unconscious drift-diffusion)  
• Decision threshold: θ (can be consciously set)  
• Bias parameter: z (conscious strategic control)  
• Final decision: conscious report when x(t) hits threshold