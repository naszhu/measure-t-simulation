
simultaneously increase the similarity between a target cue and its trace in memory and decrease the similarity between the target trace and other traces in memory This is referred to as differentiation (Criss, 2006), 

My interpretation: Differentiation is caused by the drop speed (or, really, the shape) of the distribution. while, remember, the distribution is where gives the weights for the weighted dot product. This is where differentiation comes from. But the dropping speed of the curve decides how differentiation look like. 
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