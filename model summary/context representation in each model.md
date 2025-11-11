Excellent — this is exactly the right next step: to see _what the context vectors themselves actually look like_ in each model, written concretely in vector form, so you can compare how they move through representational space.

Let’s formalize it clearly and side-by-side.

---

## **Conclusion**

All models store context as a high-dimensional vector $\mathbf{c}_t$,  
but the _way that vector changes across time_ differs sharply:

- **Simple Hebb demo:** fixed or orthogonal.
    
- **Davelaar / TCM / CMR:** exponentially drifting blend of past items.
    
- **OSCAR:** cyclic trajectory from oscillators.
    

Below, I'll write the _explicit form of $\mathbf{c}_t$_ for each.

---

## **1. Simple orthogonal context (no drift)**

### Rule

Each item gets its own unique, independent context:  
$$
\mathbf{c}_t = \mathbf{e}_t,
$$  
where $\mathbf{e}_t$ is the $t^{\text{th}}$ unit basis vector.

### Example (3 items)

$$
\begin{aligned}
\mathbf{c}_1 &= [1,0,0],\\
\mathbf{c}_2 &= [0,1,0],\\
\mathbf{c}_3 &= [0,0,1].
\end{aligned}
$$

**Shape:** perfectly orthogonal, no overlap.  
**Implication:** one-to-one mapping; no temporal contiguity.

---

## **2. Temporal Context Model (Howard & Kahana 2002)**

(same basis used in Davelaar et al. 2005 and CMR family)

### Rule

$$
\mathbf{c}_t = \rho \mathbf{c}_{t-1} + \beta \mathbf{i}_t, \quad 0 < \rho < 1.
$$  
with $\mathbf{c}_0 = \mathbf{0}$.

### Example (3 items, $\rho=0.8, \beta=0.6$)

$$
\begin{aligned}
\mathbf{i}_1 &= [1,0,0],\\
\mathbf{i}_2 &= [0,1,0],\\
\mathbf{i}_3 &= [0,0,1].
\end{aligned}
$$

Then:

$$
\begin{aligned}
\mathbf{c}_1 &= 0.8[0,0,0] + 0.6[1,0,0] = [0.6,0,0],\\
\mathbf{c}_2 &= 0.8[0.6,0,0] + 0.6[0,1,0] = [0.48,0.6,0],\\
\mathbf{c}_3 &= 0.8[0.48,0.6,0] + 0.6[0,0,1] = [0.384,0.48,0.6].
\end{aligned}
$$

**Shape:** smooth drift — each new vector contains fading traces of all earlier items.

---

## **3. Davelaar et al. (2005) STM model**

They directly adopted the TCM rule above but added _retrieval-driven reinstatement_:

During recall of item $k$,  
$$
\mathbf{c}_{r+1} = \mathbf{c}_{r} + \gamma M^{FC}\mathbf{i}_{k}.
$$

So during encoding the vectors are identical to TCM;  
during recall they **bend back** toward earlier contexts.  
E.g., if item 2 reinstates item 1's context:  
$$
\mathbf{c}_{r+1}^{(\text{after recall 2})} = [0.48,0.6,0] + \gamma[1,0,0] = [0.48+\gamma,0.6,0].
$$

**Shape:** same drift during study, partial reversal during recall.

---

## **4. Context Maintenance and Retrieval (CMR; Sederberg et al., 2008)**

CMR extends TCM with **semantic context** and **temporal context**:

$$
\mathbf{c}_t = \rho_T \mathbf{c}_{t-1}^T + \beta_T \mathbf{i}_t + \rho_S \mathbf{c}_{t-1}^S + \beta_S \mathbf{s}_t.
$$

Simplified temporal part is still:  
$$
\mathbf{c}_t^T = \rho_T \mathbf{c}_{t-1}^T + \beta_T \mathbf{i}_t.
$$

So numerically the drift looks identical to TCM, just with added dimensions representing semantic similarity.

---

## **5. OSCAR (Brown, Preece, & Hulme 2000)**

### Rule

Each dimension is driven by a sinusoidal oscillator:  
$$
c_j(t) = \sin(\omega_j t + \phi_j), \quad j=1,\dots,J.
$$

### Example (3 oscillators)

$$
\begin{aligned}
\mathbf{c}_1 &= [\sin(\omega_1 t_1+\phi_1), \sin(\omega_2 t_1+\phi_2), \sin(\omega_3 t_1+\phi_3)],\\
\mathbf{c}_2 &= [\sin(\omega_1 t_2+\phi_1), \sin(\omega_2 t_2+\phi_2), \sin(\omega_3 t_2+\phi_3)],\\
\mathbf{c}_3 &= [\sin(\omega_1 t_3+\phi_1), \sin(\omega_2 t_3+\phi_2), \sin(\omega_3 t_3+\phi_3)].
\end{aligned}
$$

**Shape:** oscillatory trajectory on a multi-frequency torus.  
Successive contexts have overlapping phases, enabling periodic reinstatement.

---

## **6. Comparison summary**

|Model|Context formula|Example vectors (3 items)|Qualitative shape|
|---|---|---|---|
|Orthogonal baseline|$\mathbf{c}_t=\mathbf{e}_t$|[1,0,0], [0,1,0], [0,0,1]|discrete, no overlap|
|TCM / Davelaar|$\mathbf{c}_t=\rho\mathbf{c}_{t-1}+\beta\mathbf{i}_t$|[0.6,0,0], [0.48,0.6,0], [0.384,0.48,0.6]|smooth exponential drift|
|CMR|same as TCM + semantic part|extended version of above|multi-source drift|
|OSCAR|$c_j(t)=\sin(\omega_j t+\phi_j)$|[sin(ω₁t₁+ϕ₁), sin(ω₂t₁+ϕ₂), …]|cyclic oscillatory|

---

### **Intuitive picture**

- **Orthogonal:** jumps between independent axes.
    
- **TCM/Davelaar/CMR:** slides smoothly through a fading mixture — like a moving window.
    
- **OSCAR:** loops through phase space — like a rotating wheel whose position uniquely marks time.
    

Each context vector therefore traces a fundamentally different _geometry of temporal representation_, even though all use Hebbian item–context binding.