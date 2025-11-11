Excellent — that's the exact complementary question.  
You've already grasped how context vectors $\mathbf{c}_t$ evolve.  
Now we'll formalize **what the content (item) representations $\mathbf{i}_t$** look like in each model, how they differ, and how they interact with context.

---

## **Conclusion**

In all these models, the **content vectors $\mathbf{i}_t$** represent the features of studied items — but each framework treats what those features _mean_ and _how they are used_ differently:

- **Baseline:** unique orthogonal identifiers.
    
- **TCM/Davelaar/CMR:** feature-based, often overlapping (semantic structure).
    
- **OSCAR:** temporal slots or “item nodes” associated with oscillator phases.
    

Below are explicit vector forms for each, matched to the same 3-item example.

---

## **1. Simple Orthogonal Content (Baseline)**

### Rule

Each item is an orthogonal basis vector:  
$$
\mathbf{i}_1 = [1,0,0], \quad \mathbf{i}_2 = [0,1,0], \quad \mathbf{i}_3 = [0,0,1].
$$

**Properties**

- Independent, no similarity.
    
- $\mathbf{i}_m^\top \mathbf{i}_n = 0$ if $m\neq n$.
    
- Retrieval from context yields a one-hot match (no generalization).
    

**Interpretation**  
Pure symbolic coding — no structure between items.

---

## **2. Temporal Context Model (TCM; Howard & Kahana 2002)**

### Rule

Same orthogonal base as above, but their functional role differs:  
$$
\mathbf{i}_t = \text{fixed item feature vector (orthogonal or semantic)}.
$$  
Encoding binds each $\mathbf{i}_t$ to its context:  
$$
M^{CF} \mathrel{+}= \mathbf{c}_t \mathbf{i}_t^{\top}.
$$

### Example (orthogonal case)

$$
\begin{aligned}
\mathbf{i}_1 &= [1,0,0],\\
\mathbf{i}_2 &= [0,1,0],\\
\mathbf{i}_3 &= [0,0,1].
\end{aligned}
$$  
So same as baseline, but used as _additive drivers_ for context drift:  
$$
\mathbf{c}_t = \rho\mathbf{c}_{t-1} + \beta\mathbf{i}_t.
$$

**If semantic similarity included:**  
$\mathbf{i}_t$ vectors are **not orthogonal**, e.g.  
$$
\begin{aligned}
\mathbf{i}_1 &= [1,0,0],\\
\mathbf{i}_2 &= [0.8,0.6,0],\\
\mathbf{i}_3 &= [0.2,0.8,0.6].
\end{aligned}
$$  
Then $\mathbf{i}_i^\top \mathbf{i}_j > 0$ encodes semantic overlap.

**Interpretation**  
Items may share feature structure; this structure influences how context drifts and reinstates.

---

## **3. Davelaar et al. (2005)**

They retained the TCM/CMR item representation but added **activation dynamics**:  
Each item has an _activation state_ $a_i(t)$ governed by a leaky integrator:  
$$
\tau \frac{da_i}{dt} = -a_i + f(W^{CI}\mathbf{c}_t),
$$  
where $W^{CI}$ is the context→item weight matrix (Hebbian).

**Item vectors** themselves are still discrete identity codes,  
but **activations** evolve continuously in time, giving rise to recency and short-term persistence.

### Example

At encoding, the feature vector for item 2 might be $[0,1,0]$,  
but its _activation level_ remains partly active into item 3's presentation (short-term trace).

**Interpretation**  
So here the _content representation_ has two levels:

1. A static vector $\mathbf{i}_t$ (identity of the item).
    
2. A dynamic activation $a_i(t)$ (its short-term strength).
    

---

## **4. CMR (Sederberg et al., 2008)**

### Rule

Each item has both:

- A **temporal feature vector** $\mathbf{i}_t^T$ — orthogonal or partially overlapping.
    
- A **semantic vector** $\mathbf{i}_t^S$ — shared across conceptually similar words.
    

These are concatenated or weighted:  
$$
\mathbf{i}_t = [\lambda_T \mathbf{i}_t^T; \lambda_S \mathbf{i}_t^S].
$$

### Example

If items "cat," "dog," "apple":  
$$
\begin{aligned}
\mathbf{i}_{\text{cat}} &= [1,0,0; 0.9,0.8,0],\\
\mathbf{i}_{\text{dog}} &= [0,1,0; 0.8,0.9,0],\\
\mathbf{i}_{\text{apple}} &= [0,0,1; 0.2,0.3,1].
\end{aligned}
$$

**Interpretation**  
Part of each vector is temporal (for list position), part semantic (for meaning).  
Hence, context can reinstate both recent and semantically related items.

---

## **5. OSCAR (Brown, Preece & Hulme 2000)**

### Rule

Items are represented as **unit vectors or sets of item nodes** that are associated with the oscillator-defined context:  
$$
W \mathrel{+}= \mathbf{i}_t \mathbf{c}_t^{\top}.
$$  
Unlike TCM, item vectors don't enter the context update directly; the context evolves independently by oscillators.

### Example

$$
\begin{aligned}
\mathbf{i}_1 &= [1,0,0],\\
\mathbf{i}_2 &= [0,1,0],\\
\mathbf{i}_3 &= [0,0,1].
\end{aligned}
$$

Each item node becomes linked to its oscillator-phase vector $\mathbf{c}_t$.  
During recall, the re-created oscillator state cues whichever item had that phase.

**Interpretation**  
Items are _static discrete symbols_; temporal structure comes entirely from oscillators, not item similarity.

---

## **6. Comparison Summary**

|Model|Content vector $\mathbf{i}_t$|Overlap structure|Enters context update?|Role|
|---|---|---|---|---|
|Orthogonal baseline|one-hot basis|none|no|unique identifier|
|TCM|orthogonal or semantic feature vector|possible semantic overlap|✅ yes ($\beta\mathbf{i}_t$)|drives context drift|
|Davelaar et al.|same as TCM + dynamic activation $a_i(t)$|possible overlap|✅ yes|drives STM dynamics|
|CMR|concatenated temporal + semantic|strong overlap|✅ yes|integrates multiple contexts|
|OSCAR|discrete item node|none|❌ no|linked by oscillatory phase only|

---

### **Intuitive picture**

- **Baseline:** content = label.
    
- **TCM/Davelaar/CMR:** content = vector of item features (identity ± semantic).
    
- **OSCAR:** content = node connected to specific phase of oscillation.
    

So across models, the _mathematical form of content vectors_ changes from **static identifiers** to **feature carriers** to **phase-linked symbols**,  
reflecting each model’s view of how memory traces store “what” information.