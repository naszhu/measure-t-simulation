[[state space - mathcal{X}]]
[[measure]]

You can say, that the original [[Measure - P]] on [[Sample space - Omega]] is P, and then you say the pushforward measure after pushing P through X onto x ([[state space - mathcal{X}]]), would be written as P_X; 

![[Pasted image 20251025153247.png]]

#### **Pushforward (Measure Theory)**

- Definition: Let $(X, \Sigma_X)$ and $(Y, \Sigma_Y)$ be measurable spaces. Let $\mu$ be a measure (probability mass) on $X$. A function $T: X \to Y$ creates a Pushforward Measure $T_* \mu$ on $Y$, defined as:
    
    $$(T_* \mu)(B) = \mu(T^{-1}(B))$$
    
    - _Meaning:_ The "weight" of a region in the new space $Y$ is strictly determined by how much "mass" from $X$ lands there.
        
- **Application in REM:** [[REM]] is a **Pushforward**.
    
    - $X$ = The Environment (Real World statistics).
        
    - $\mu$ = The frequency of features in the world (The Geometric Distribution).
        
    - $Y$ = The Memory Trace (Discrete Feature Space).
        
    - **Crucial Difference:** Pushforward does **not** preserve topology. It only preserves **Mass** (Probability). Two items can be "close" in the world (conceptually) but mapped to totally different feature integers in REM, as long as the probability math works out.

# definition
- $P_X$ is the **pushforward measure** on $\mathcal{X}$ (the state space of ). It is defined as $P_X(A)=P(X^{−1}(A))$.
or 
![[Pasted image 20251101180913.png]]

But, what is the way to write f_X(x)? what this f is? ([[Question]])



## caution: typically people deal with state space

P is irrelevant 
![[Pasted image 20250728203604.png]]
### a) The probability measure

- Formally you have a probability space (Ω,F,P)
    
- A random variable $X\colon\Omega\to\mathbb R$  **pushes forward** that measure to a new measure $P_X$ on the real line.
    
- $P_X$ is only defined on [[event]] ([[Borel sets]]) in $\mathbb R$, not “at a point.” [[Question]], events=borel sets? i.e., sets=> a way to make equal points into another definition of weighted (point have mass?). 

![[Pasted image 20250728191028.png]]

# measure methods
[[Lebesgue measure]], [[counting measure]]
![[Pasted image 20250728191240.png]]