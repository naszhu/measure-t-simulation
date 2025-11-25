You are absolutely right to dismiss the "discrete vs. continuous" distinction as the root cause. You can have a discrete Gaussian (the **Binomial Distribution**), but if you used it in REM, the model would still fail to produce the differentiation effect.

The reason Gaussian fails and Geometric works is indeed **Concentration of Measure**, and it stems specifically from **Symmetry** and **Tail Behavior** (how they average out in high dimensions).

Here is the deep structural difference.

### 1. The Discrete Gaussian (Binomial) vs. Geometric

First, to answer your question: Yes, there is a discrete version of the Gaussian. It is the **Binomial Distribution** (like flipping a coin $N$ times).

- **Shape:** Symmetric hill.
    
- **Peak:** At the mean.
    
- **Tails:** Decay extremely fast ($e^{-x^2}$).
    

If REM used a Binomial distribution for feature values, it would fail. Here is why.

### 2. Why Gaussian/Binomial Leads to "Concentration" (The Grey Sphere)

In a high-dimensional space (e.g., a vector with 100 features), if you draw numbers from a Gaussian/Binomial distribution:

A. The "Spherical Shell" Effect

Because the distribution is Symmetric and clustered around a mean, every single random vector ends up having almost the exact same distance from the origin (Magnitude) and the exact same distance from every other vector.

- **Math:** The Law of Large Numbers kicks in immediately. If you sum 100 random Gaussian numbers, the result is extremely predictable.
    
- **The "Averaging":**
    
    - Feature 1: A little high.
        
    - Feature 2: A little low.
        
    - Feature 3: Average.
        
    - **Result:** The deviations cancel each other out.
        
- **The REM Consequence:**
    
    - Target Similarity: Sum of "Medium" matches $\approx$ Average Score.
        
    - Foil Similarity: Sum of "Medium" matches $\approx$ Average Score.
        
    - **Result:** $d'$ (Sensitivity) stays constant. You cannot differentiate strong items from weak items because **Strong items are just "more average."**
        

### 3. Why Geometric Avoids Concentration (The "Spiky" Space)

The Geometric distribution works because it is **Highly Skewed** (Asymmetric). It resists the Law of Large Numbers because the variance is driven by rare "Jackpot" events.

A. The "Black Swan" Effect

In a Geometric distribution (or Zipfian/Sparse distributions):

- Most values are **0** (or 1). They contribute nothing.
    
- A tiny few values are **Huge** (e.g., 20).
    

B. Why it doesn't "Average Out"

When you compare two vectors in this space:

- **Foil Match:** Matches only on common features (0s and 1s). The sum is small and stable.
    
- **Target Match:** Matches on that _one_ rare feature (20).
    
- **The Math:** The Likelihood Ratio for a match at value 20 is massive (e.g., 1000x).
    
    - One "1000x" match does **not** get cancelled out by a few "0.5x" mismatches.
        
    - **The Average breaks:** You don't get a smooth convergence to the mean. You get a "Spiky" distribution where a single rare feature allows the vector to stick out from the noise.
        

### 4. The Geometric Analogy: The "Sea Urchin"

To visualize the high-dimensional shape difference:

- **Gaussian Space is a Fuzzy Ball:**
    
    Every vector points to the surface of the ball. They all look the same. If you rotate the ball (add strength/noise), it looks identical. You cannot distinguish one point from another easily.
    
- **Geometric Space is a Sea Urchin:**
    

![Image of a sea urchin](https://encrypted-tbn1.gstatic.com/licensed-image?q=tbn:ANd9GcTfV7V7yLOipFV77mH-Z_pAlsIoZ7CGXFxT29zEvEz5WAJ6RRvgGd7M2vGK5LPMkQdln8DZRq1HqrhqNy0XdC3tidouTxwig2qPfLVg0bvs4YDSb3Y)

Shutterstock

```
Most of the vector is near the center (0s), but occasionally a long spike shoots out in one specific direction (a Rare Feature).
* **Differentiation:** Because the spikes are long and sparse, the "Spike pointing North" is totally distinct from the "Spike pointing West."
* **Strength:** Strengthening an item extends its specific spike. It does **not** inflate the whole ball.
```

### Summary

The Gaussian fails because it assumes **Information is Democratic**—every feature contributes roughly the same amount of "average" info, so they all average out to a grey mush (Concentration of Measure).

The Geometric succeeds because it assumes **Information is Aristocratic**—most features are peasants (noise), but a few are kings (rare signal). The kings dominate the sum, preventing the signal from drowning in the average.