the odds is essentially weighted [[dot product]], this is what different from the traditional global matching methods 
### [[Question]]

WHy REM use geometric? [Google Gemini](https://gemini.google.com/app/bed88f2cfa8438e8)


- Why REM isn't a [[Stochastic Process]]?

[[Output Interference in REM]]

[[REM deduction]]


[[concentration of measure]]

vs. [[GCM]]
#### **A List of Codes in a [[feature space]]**

- **Representation:** $\mathbf{v} = [20, 0, 5, ...]$.
    
    - Position 1 is just "Feature Slot 1" (abstract).
        
    - The _Value_ ($20$) carries the meaning (e.g., "Has a beak").
        
- **The Math:** This is a **Discrete Probability Space** (or a Sparse Feature Space).
    
- **Property:** **Cardinality (Identity) matters.**
    
    - Is $20$ "closer" to $21$ than $50$? **No.** In REM, features are usually treated as discrete codes drawn from a geometric distribution1.
        
    - If Target has `20` and Probe has `21`, it is a **Mismatch**. It doesn't matter how close the numbers are; they are different identities.