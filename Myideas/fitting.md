| **Parameter**               |                                                                                                                                                                                                         |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Capacity ($C$)**          |                                                                                                                                                                                                         |
| **Threshold ($k$)**         |                                                                                                                                                                                                         |
| **Residual Time ($t_0$)**   |                                                                                                                                                                                                         |
| **Drift Weights ($w$)**     |                                                                                                                                                                                                         |
| **Rate Variance ($1/\xi$)** | fix slow error (right tail)                                                                                                                                                                             |
| **Starting Point ($z$)**    | **The Fast Errors (Left Side).** If $z$ varies, sometimes you start closer to the wrong boundary. This creates a tiny bump of very fast, incorrect responses (guessing).                                |
| **Encoding Ramp ($\mu_S$)** | **The Leading Edge (Left Side).** It controls how sharp the "start" of the distribution is. A slow ramp ($\mu_S$) makes the distribution rise gradually, rather than shooting up instantly after $T_0$. |

- **Trial-by-Trial Variability:**
    
    - **Rate Variability ($1/\xi$):** 1 parameter. The scale parameter for the gamma distribution of processing rates6.
        
    - **Starting Point ($z_A, z_B$):** 2 parameters. These describe the beta-binomial distribution of the starting point7.
        
- **Temporal Dynamics:**
    
    - **Encoding Time ($\mu_S$):** 1 parameter. Describes the time course of sustained visual processing8.
---
high C, distribution move left, become more sharp as well (but fat right tail doesnt work)
high k, move towards guassian, low, move towards skewed 

$$RT \propto \frac{k}{v}$$

$$NLL = - \sum_{i=1}^{N} \ln \left( P_{model}(RT_i) \right)$$
- $\ln(0.1) = -2.3$ (Manageable penalty)
    
- $\ln(0.000000001) = -20.7$ (Huge penalty)
    
- $\ln(0) = -\infty$


#### "Slow" Trial ($RT = 1.2s$)

Scenario A: Current Fit ($C = 3.5$)

The model is "short and fat." It predicts a probability density of $0.01$ at 1.2s.

$$\text{Cost} = -\ln(0.01) = \mathbf{4.6}$$

Status: The optimizer pays a cost of 4.6. This is fine.

Scenario B: The Fit You Want ($C = 30$)

The model is "tall and thin." Because the curve drops off so sharply, the probability density at 1.2s is infinitesimal.

$$P_{model}(1.2) \approx 1 \times 10^{-40}$$

$$\text{Cost} = -\ln(10^{-40}) \approx \mathbf{92.1}$$