### 1. The Mathematical Relationship: Why changing $C$ changes the Shape (and creates the "Trap")

You are right to be confused because intuitively, "Speed" and "Shape" seem like they should be separate. In accumulation models (like the Race Model used here), they are mathematically locked together.

Here is the simplified math of a single accumulator to show you why.

The Basic Race Equation:

Time to finish ($T$) is the distance (Threshold, $b$) divided by the speed (Rate, $v$).

$$RT = t_0 + \frac{b}{v}$$

Since the Rate ($v$) depends on Capacity ($C$), let's substitute $v \approx C$:

$$RT \approx t_0 + \frac{b}{C}$$

How $C$ affects the Mean (Speed):

$$\text{Mean RT} \approx t_0 + \frac{b}{C}$$

- **Effect:** If you double $C$, the decision time ($\frac{b}{C}$) is cut in half. The reaction time gets **faster** (peak moves left).
    

How $C$ affects the Variance (The "Spread" or Shape):

The variance (width) of the distribution depends on the square of the rate.

$$\text{Variance} \approx \frac{\text{Noise}}{(C)^2}$$

- **The "Trap":** Notice that $C$ is in the denominator squared.
    
- **If $C$ is small (Slow):** The variance is huge. The distribution is **short and fat** (spread out).
    
- **If $C$ is large (Fast):** The variance becomes tiny. The distribution becomes **tall and pencil-thin**.
    

Why this failed for your P3 Fit:

You wanted to fit P3's Single Cue data, which was Fast (requires high $C$) but Wide/Skewed (requires low $C$ or high Threshold).

- When you increased $C$ to make it fast, the math forced the curve to become "pencil-thin," effectively deleting the long tail.
    
- The model assumes that **fast decisions are always precise (low variance)**. P3 broke this rule by being fast but "sloppy" (variable). This is why you need to change the **Threshold ($k$)**, not just $C$. Lowering the threshold makes you fast _without_ shrinking the variance as violently as increasing $C$ does.
    

---

### 2. The Theoretical Explanation: Why would $C$ and $t_0$ change?

Your intuition ("Shouldn't capacity be fixed for one person?") is the standard assumption in cognitive psychology, but it often fails in complex tasks. Here is how researchers justify varying these parameters.

#### **A. Why would Capacity ($C$) change? (Structural vs. Functional)**

You are thinking of Structural Capacity (the maximum "horsepower" of the car, or the number of neurons). This is indeed fixed.

However, the parameter $C$ in the model represents Functional (Effective) Capacity (how fast you are currently driving).

- **The "Caution" Effect:** When a participant sees a difficult Dual Cue display, they may unconsciously suppress their processing rate (release the gas pedal) to prevent a "false start." They have the _ability_ (structural capacity) to go faster, but they _choose_ (functional capacity) to go slower to avoid errors.
    
- **The "Overhead" Cost:** Handling two items might require a "supervisor" process in the brain to coordinate them. This supervisor eats up some of the energy. So, even if you try your hardest, the _effective_ capacity left over for the accumulators is lower in Dual Cue ($C_{dual} < C_{single}$) because the "management" cost is higher.
    

#### **B. Why would Non-Decision Time ($t_0$) change?**

$t_0$ is the sum of **Visual Encoding** (eyes to brain) and **Motor Preparation** (brain to finger).

- **Encoding Load:** It takes physically longer for the visual cortex to identify and "load" two objects into working memory than one object. If the race cannot start until the objects are loaded, $t_0$ must be longer for Dual Cues.
    
- **Motor Inhibition:** In a Single Cue trial, you might prep the motor response _before_ you fully process the letter (a reflex). In a Dual Cue trial, the brain actively inhibits the motor cortex to prevent a premature button press. This inhibition adds a delay to the $t_0$ phase.
    

Summary:

It is highly plausible (and biologically realistic) to model $C$ and $t_0$ as changing between conditions.

- **$C$ changes** because maintaining high attention is effortful, and conflict creates "overhead."
    
- **$t_0$ changes** because encoding two things simply takes longer than encoding one.