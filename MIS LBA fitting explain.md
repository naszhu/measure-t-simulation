Here is the theoretical and mathematical analysis of how varying each parameter influences the result (Reaction Time distribution and Choice Probability) in a Race Model framework like MIS.

To understand this, visualize the model as a **Car Race**:

- **Accumulators** = The Cars.
    
- **$C$ (Capacity)** = The Engine Power (Fuel).
    
- **$w$ (Weights)** = The Distribution of Fuel (which car gets more).
    
- **$k$ (Threshold)** = The Distance to the Finish Line.
    
- **$t_0$ (Non-decision time)** = The Time taken to Start the Engine.
    

---

### 1. Capacity ($C$): The "Global Speed" Knob

Mathematical Role:

Capacity acts as a scalar multiplier for the drift rate ($v$).

$$v_i = C \times \frac{w_i}{\sum w}$$

**Theoretical Influence:**

- **On RT Mean:** Increasing $C$ makes **all** decisions faster. The cars drive faster.
    
- **On RT Variance (The Shape):** This is the critical part. In diffusion/race logic, **Variance scales with $1/C^2$**.
    
    - **High $C$:** The distribution becomes **tall and pencil-thin**. The car is so fast it finishes at almost the exact same time every trial.
        
    - **Low $C$:** The distribution becomes **short, fat, and smeared**. The car is slow, so random noise has a huge effect, causing some trials to be fast and others very slow.
        

**Why your fit got stuck:** The optimizer refused to increase $C$ (to match the peak) because doing so would make the curve too thin to cover the slow trials in the tail.

---

### 2. Threshold ($k$): The "Caution" Knob

Mathematical Role:

Threshold defines how much evidence is needed to stop.

$$RT \propto \frac{k}{v}$$

**Theoretical Influence:**

- **On RT Mean:** Increasing $k$ increases RT linearly. A longer track takes longer to finish.
    
- **On RT Shape (Skewness):** This distinguishes Single vs. Dual cues.
    
    - **Low $k$ (Reflex):** The distribution is **Highly Skewed (Exponential)**. It rises vertically and has a long tail. This matches your **Single Cue** data.
        
    - **High $k$ (Deliberate):** The distribution becomes **Symmetrical (Gaussian/Normal)**. The "Law of Large Numbers" kicks in; noise cancels out over the long distance. This matches your **Dual Cue** data.
        
- **On Accuracy:** Increasing $k$ improves accuracy. It gives the "better" car (higher weight) more time to separate itself from the "worse" car.
    

**Analysis for P3:** This participant likely uses a **Low $k$** for single cues (reflexive, skewed shape) and a **High $k$** for dual cues (cautious, symmetrical shape).

---

### 3. Weights ($w$): The "Steering" Knob

Mathematical Role:

Weights determine the ratio of speeds between competitors.

$$P(Choice_A) = \frac{v_A}{v_A + v_B} = \frac{w_A}{w_A + w_B}$$

**Theoretical Influence:**

- **On RT:** Higher weight = Faster RT for that specific item.
    
- **On Accuracy:** This is the primary driver of choice.
    
    - If $w_A \gg w_B$: Accuracy is ~100%.
        
    - If $w_A \approx w_B$: Accuracy is ~50% (Random guessing).
        

**Analysis for P3:** Your fit showed $w_2 \approx 11$ and $w_3 \approx 17$. This is a "close race." Mathematically, this forces the model to predict low accuracy (many errors). Since P3 actually had high accuracy, the model is theoretically "broken" unless you allow a much higher **Threshold ($k$)** for these conflict trials to let the slightly faster car win.

---

### 4. Non-Decision Time ($t_0$): The "Shift" Knob

Mathematical Role:

This is an additive constant.

$$RT_{total} = RT_{decision} + t_0$$

**Theoretical Influence:**

- **On RT:** Linearly shifts the _entire_ distribution left or right.
    
- **On Shape:** It does **not** change the shape (height/width). It only changes the start point.
    

**Constraint Danger:** If $t_0$ is set even 1ms greater than the fastest observed reaction time, the probability of that fast trial becomes **Zero** ($-\infty$ log likelihood). This forces the optimizer to be very conservative with $t_0$.

---

### Summary: How to "Read" the Discrepancy

Use this lookup table to analyze your plots:

|**Observation in Plot**|**Theoretical Cause**|**Parameter to Change**|
|---|---|---|
|**Predicted Peak is too far Right**|Model thinks prep time is too long.|Decrease **$t_0$**|
|**Predicted Peak is too Short/Fat**|Model thinks processing is too slow/noisy.|Increase **$C$** (but beware the tail!)|
|**Predicted Curve is too Skewed**|Model assumes a threshold that is too low.|Increase **$k$** (Threshold)|
|**Predicted Accuracy is too Low**|Model thinks the weights are too similar.|**$w$** ratio is too small OR **$k$** is too low.|

For Participant 3:

The combination of "Sharp/Skewed RTs" in single cues (requires Low $k$, High $C$) and "Accurate Choices" in dual cues (requires High $k$) is why a single set of shared parameters cannot fit the data. Theoretically, the system is changing states.