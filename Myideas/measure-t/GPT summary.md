Here is a **brief, clean summary** of _her_ framework—stripped down to its core ideas, easy to convey to others, and capturing exactly what she is building.

---

# **Her Framework in 10 Sentences (Very Brief)**

1. **Memory should be defined as transformations of information**, not as isolated mechanisms or separate models.
    
2. All memory models operate on some combination of **content** (what the item is) and **context** (where/when/how it was experienced).
    
3. The field currently hides this structure inside incompatible mathematical forms (SDT distributions, TCM drift, REM kernels, SIMPLE metric compression, etc.).
    
4. She proposes that all of these models can be unified using **measure theory**: a memory state is a **probability measure** over content × context space.
    
5. **Encoding** is a transformation of this measure (like a push-forward, kernel smoothing, or density change).
    
6. **Recognition** is comparing _marginal_ measures (integrating over all contexts): SDT is just the 1-D marginal case.
    
7. **Recall** is comparing _conditional_ measures (given a specific context cue): recall = conditionalization, recognition = marginalization.
    
8. **Familiarity (global matching)** stays in the _original_ representational space; **recollection** requires _expanding_ the space or adding dimensions.
    
9. **Forgetting** is increasing divergence between the study measure and the current measure (via drift, decay, interference, or metric compression).
    
10. All classic models (TCM, SIMPLE, REM, SAM, etc.) become **special cases of three fundamental transformations**:
    

- **push-forward** (context drift)
    
- **kernel** (similarity-based retrieval)
    
- **density change** (attention/decay)
    

---

# **Even Shorter (3 sentences)**

Memory = **a measure over content × context**.  
All encoding, retrieval, and forgetting = **transformations of this measure** (push-forward, kernel, or density change).  
Recognition = **marginal measure**, recall = **conditional measure**, and classic models are just different instantiations of this universal structure.

---

# **If you want it visually:**

**Study**:  
$$  
\mu_{\text{study}}(f, \psi)  
$$

**Encoding** = transform measure  
$$
\mu_{\text{encoded}} = T_{\#}\mu \quad \text{or} \quad K\mu \quad \text{or} \quad w\cdot\mu
$$

**Recognition** = compare  
$$  
\mu_{\text{old}}(f) = \int d\mu(f,\psi)  
$$  
(marginal over context)

**Recall** = use cue to condition  
$$  
\mu(f \mid \psi = \psi_{\text{cue}})  
$$

**Forgetting** =  
$$  
D(\mu_{\text{study}}, \mu_{\text{test}})  
$$  
(divergence increases)

Everything else = combinations of those three transformations.

---

# **One-sentence punchline**

**Her framework says memory is just the geometry of how a probability measure over content and context is transformed—and all existing models are specific cases of that universal transform.**

---

If you want, I can also write:

- a 15-second elevator pitch,
    
- a talk slide summarizing the idea,
    
- or a version she can send to Shiffrin and Malmberg.