
simultaneously increase the similarity between a target cue and its trace in memory and decrease the similarity between the target trace and other traces in memory This is referred to as differentiation (Criss, 2006), (negative list strength effect )

---

My interpretation: Differentiation is caused by the drop speed (or, really, the shape) of the distribution. while, remember, the distribution is where gives the weights for the weighted dot product. This is where differentiation comes from. But the dropping speed of the curve decides how differentiation look like. 

---

### . The "Minimum Mathematical Structure" for Differentiation

You asked for the "essential mathematical assumption" that cannot be removed. It is **Orthogonality of Error**.

To predict the List-Strength Effect (where strengthening Target A does not hurt Target B), your model must satisfy this condition:

The Differentiation Condition:

$$\frac{\partial P(\text{Match} | \text{Foil})}{\partial \text{Strength}} < 0$$

- **Traditional Models (Fail):** As Strength increases, the vector magnitude increases ($|\mathbf{v}| \uparrow$). The "Interaction Space" with a foil grows.
    
    - _Math:_ $\text{Score} = \mathbf{T} \cdot \mathbf{F}$. If $\mathbf{T}$ gets bigger, the dot product likely gets bigger (or stays same). Noise increases.
        
- **Differentiation Models (Succeed):** As Strength increases, the "Interaction Space" shrinks.
    
    - _Math:_ The model must define similarity such that **Adding Information** restricts the set of possible matches.
        
    - **Essential Structure:** You need a **Sparse, High-Dimensional Space** where vectors are effectively **Orthogonal** (Independent).
        
    - _Why Orthogonal?_ In high-dimensional space, two random sparse vectors are nearly orthogonal (their dot product is near zero). Strengthening a vector in REM/SLiM pushes it further out along its _own_ unique axis (or narrows its cone), making it _more_ orthogonal to the random noise cloud.
        

The Minimum Rule:

You do not need "Heavy Tails" specifically. You need a Monotonically Decreasing Likelihood Function for mismatches.

- _Rule:_ The more information I have about Target T, the lower the probability that Random Foil F generated this signal.
    
- _Implementation:_ Likelihood Ratios naturally do this ($L < 1$ for mismatches). Dot products do not (they just add 0).

---
### What Shape gives the "Most" Differentiation?

The optimal shape for differentiation is a **Power Law (Zipfian) Distribution**.

$$P(v) \propto \frac{1}{v^\alpha}$$

Why is it optimal?

It maximizes the inequality between the "Head" and the "Tail."

[Google Gemini](https://gemini.google.com/app/bed88f2cfa8438e8)

- Fat Gaussian (High Variance):
    
    You stretch the bell curve. It becomes wider.
    
    - _Effect:_ You push the "cliff" further out.
        
    - _The Problem:_ Once you reach the cliff, the drop is still **Super-Exponential** ($e^{-x^2}$). The probability of finding a value even slightly beyond the main curve essentially hits zero instantly.
        
- Geometric (Heavy Tail):
    
    The drop is only Exponential ($c^{-x}$).
    
    - _Effect:_ The probability decreases steadily, but it never "falls off a cliff." There is always a fighting chance to find a very large number.