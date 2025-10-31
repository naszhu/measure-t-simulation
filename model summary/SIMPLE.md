### Mathematical Summary of the SIMPLE (Temporal Ratio) Model  
**Brown, Neath, & Chater (2007, 2008)**

#### **1. Core Assumptions**
1. **Temporal representation:**  
   Each memory item is located on a *log-compressed temporal dimension*:  
   $M_i = \log(T_i)$,  
   where $T_i$ is the temporal distance from the current moment of recall.  
   → Recent items are more discriminable; older items are crowded.

2. **Retrieval as discrimination:**  
   Memory retrieval is a **discrimination problem** among items distributed in psychological (temporal) space.

3. **Similarity (confusability) function:**  
   Similarity between two memory traces $i$ and $j$:  
   $\eta_{i,j} = e^{-c |M_i - M_j|}$,  
   or equivalently, in ratio form:  
   $\eta_{i,j} = \left(\frac{\min(T_i, T_j)}{\max(T_i, T_j)}\right)^c$

   where $c$ controls how sharply similarity falls off with temporal distance.

4. **Local distinctiveness principle:**  
   Items are primarily interfered with by *near neighbors*, not all other traces globally.

---

#### **2. Discriminability and Recall Probability**

- **Discriminability of item $i$:**  
  $D_i = \frac{1}{\sum_{j=1}^n \eta_{i,j}}$

- **Recall probability (serial reconstruction):**  
  $P(R_i) = D_i = \frac{1}{\sum_{j=1}^n \eta_{i,j}}$

- **Alternative ratio formulation:**  
  $P(R_i) = \frac{1}{\sum_{j=1}^n (\text{Ratio}(T_i, T_j))^c}$  
  where $\text{Ratio}(T_i, T_j) = \frac{\min(T_i, T_j)}{\max(T_i, T_j)}$

- **With omissions (free recall):**  
  $P(R_i|D_i) = \frac{1}{1 + e^{-s(D_i - t)}}$  
  where $t$ = threshold, $s$ = slope (noise parameter).

---

#### **3. Structural and Conceptual Points**

| Component | Mathematical Form | Interpretation |
|------------|-------------------|----------------|
| **Temporal mapping** | $M_i = \log(T_i)$ | Time dimension compressed logarithmically; scale-invariance |
| **Similarity** | $\eta_{i,j} = e^{-c|M_i - M_j|}$ | Items closer in time are more confusable |
| **Retrieval** | $P(R_i) \propto 1 / \sum_j \eta_{i,j}$ | Retrieval governed by local crowding in temporal space |
| **Forgetting law** | $P \propto T^{-a}$ | Approximate power-law forgetting |
| **Scale similarity** | Performance invariant under temporal scaling | Same principles apply over short and long timescales |

---

#### **4. Comparison to Traditional Models**

| Feature | SIMPLE | Context/Associative (e.g., TCM) |
|----------|---------|--------------------------------|
| Representation | Items in log-compressed temporal space | Items bound to context vector |
| Mechanism | Discriminability among temporal neighbors | Association between item and drifting context |
| Update | No weight storage; purely positional geometry | Additive outer products ($W_{t+1} = W_t + f_t \otimes \psi_t$) |
| Space type | Temporal–metric embedding | Product-space operator |
| Rationale | Memory loss = interference from temporal crowding | Memory = decay or context drift over encoded weights |

---

#### **5. Unified Operator Interpretation**

- SIMPLE can be formalized as an **operator in a metric (embedding) space**:
  $\mathcal{O}(t): M_i \mapsto P(R_i)$  
  where $\mathcal{O}$ measures discriminability rather than performs associative mapping.

- It thus belongs to the **embedding-space regime** of the unified operator framework:
  - No stored $W$ (as in product space)  
  - No evolving $h_t$ (as in Hilbert space)  
  - Memory = *geometry of temporal embedding* under ratio metric.

---

#### **6. Key Insight**

> SIMPLE converts memory from a problem of **contextual binding** to one of **temporal geometry**,  
> replacing additive trace storage with **scale-invariant discriminability** across time.
