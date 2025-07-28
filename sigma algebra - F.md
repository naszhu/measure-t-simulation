- **σ-algebra (F)**:
    
    - F is **not** necessarily all subsets of ΩΩ. It is a restricted collection **satisfying**:
        
        1. Ω∈F,
            
        2. Closed under complements (A∈F  ⟹  A),
            
        3. Closed under countable unions (A1,A2,⋯∈F  ⟹  ∪iAi∈F).

All sets in F are measurable by construction.


- **Why restrict to measurable sets?**
    
    - **Measure-theoretic necessity**: For spaces like RR, we _cannot_ consistently define probabilities for _all_ subsets (due to non-measurable sets like Vitali sets).
        
    - **Avoids paradoxes**: Restricting to F (e.g., [[Borel sets]] for $\mathbb{R}$) ensures P is countably additive without contradictions.
        
    - **Practicality**: We only need to measure "well-behaved" sets (intervals, etc.).