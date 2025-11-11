The **OSCAR (Oscillator-based Associative Recall)** model mathematically encodes and recalls sequences through **dynamic context vectors driven by oscillators**.  
Here’s a condensed mathematical summary of how encoding → recall works:

---

### 🧩 Core Mechanism (Encoding → Recall Flow)

**Conclusion:**  
OSCAR encodes each item $i_t$ by associating it with the oscillatory context state $\mathbf{c}_t$, and recalls by regenerating $\mathbf{c}_t$ through oscillator dynamics to cue back $i_t$.

---

### 1. **Item and Context Representation**

- Each list item is represented by a **vector** $\mathbf{i}_t \in \mathbb{R}^{16}$.
    
- The **context** is also a 16-dimensional vector $\mathbf{c}_t$, determined by the output of multiple sinusoidal oscillators.
    

$$
\mathbf{c}_t = \big[ \prod_{k=1}^{4} f_{1k}(t), \prod_{k=1}^{4} f_{2k}(t), \dots, \prod_{k=1}^{4} f_{16k}(t) \big]
$$

where  
$f_{jk}(t) \in \{\sin(\theta_{jk}(t)), \cos(\theta_{jk}(t))\}$ are oscillator outputs with different frequencies.

Each oscillator phase evolves as:

$$
\theta_{n}(t+1) = \theta_{n}(t) + \Delta_n, \quad \Delta_n = D \cdot 2^n \cdot \epsilon_n
$$

with $D$ controlling distinctiveness and $\epsilon_n \sim \mathcal{N}(0,1)$ introducing noise.

---

### 2. **Encoding (Learning)**

Item–context associations are learned Hebbian-style:

$$
W = \sum_{t} \mathbf{i}_t \mathbf{c}_t^\top
$$

so that the connection matrix $W$ encodes which item occurred in which context.

Intuitively,  
each item vector $\mathbf{i}_t$ is "bound" to the oscillatory state $\mathbf{c}_t$ at its presentation time.

---

### 3. **Recall (Regeneration of Context → Cueing)**

- Start recall by resetting oscillators to their initial state $\mathbf{c}_1$.
    
- Let the oscillators evolve autonomously:  
    $$
    \mathbf{c}_{t+1} = F(\mathbf{c}_t)
    $$  
    where $F$ is the deterministic evolution from oscillator phase updates.
    
- Each regenerated $\mathbf{c}_t$ serves as cue to retrieve its associated item:
    

$$
\hat{\mathbf{i}}_t = W \mathbf{c}_t
$$

- The recalled item corresponds to the item vector with **maximum similarity** (dot product) to $\hat{\mathbf{i}}_t$.
    

---

### 4. **Similarity and Order Errors**

Because nearby contexts are similar:

$$
\text{sim}(\mathbf{c}_t, \mathbf{c}_{t+\Delta}) = \mathbf{c}_t^\top \mathbf{c}_{t+\Delta} \approx \cos(\omega \Delta)
$$

items with nearby serial positions have overlapping cues → local transpositions (the "movement gradient").

---

### 5. **Hierarchical and Long-term Encoding**

Slow vs. fast oscillators produce **nested temporal scales**:  
$$
\mathbf{c}_t = g(\sin(\omega_1 t), \sin(\omega_2 t), \dots)
$$  
Slow oscillators encode higher-level (group/list) structure; faster ones encode within-group order.

---

### 6. **Distinctiveness**

Temporal distinctiveness comes from angular distance:  
$$
d(t_1, t_2) = 1 - \mathbf{c}_{t_1}^\top \mathbf{c}_{t_2}
$$  
Items with closer context states (smaller $d$) are harder to discriminate → predicts U-shaped serial-position curves.

---

### Summary Table

|Stage|Mathematical Operation|Cognitive Meaning|
|---|---|---|
|Encoding|$W \mathrel{+}= \mathbf{i}_t \mathbf{c}_t^\top$|Bind item to context|
|Context evolution|$\mathbf{c}_{t+1} = F(\mathbf{c}_t)$ via oscillators|Internal clock dynamics|
|Recall cue|$\mathbf{c}_t$ regenerated|Context reinstatement|
|Retrieval|$\hat{\mathbf{i}}_t = W \mathbf{c}_t$|Cue probes memory|
|Selection|$\arg\max_i (\hat{\mathbf{i}}_t \cdot \mathbf{i}_i)$|Output item with highest match|

---

Would you like me to write out the **explicit Julia code version** that simulates the encode–recall process (oscillators, context, Hebbian storage, recall loop)?