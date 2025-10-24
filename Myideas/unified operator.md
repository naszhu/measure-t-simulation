# **Unified Operator Framework for Short-Term Memory Models**

## 1. The General STM Paradigm

Short-term memory (STM) tasks follow a common two-phase structure:

1. **Study phase:** a sequence of items is presented, each associated with a temporal or contextual position.
2. **Test phase:** one or more probes are presented, requiring recall or recognition of items in order or by cue.

### Core Cognitive Processes

| Process         | Function                                        | Mathematical Representation                                  |                                           |
| --------------- | ----------------------------------------------- | ------------------------------------------------------------ | ----------------------------------------- |
| **Encoding**    | Transform stimuli into internal representations | $f_t = \Phi_{item}(x_t)$, $\psi_t = \Phi_{context}(y_t)$     |                                           |
| **Maintenance** | Sustain or transform context                    | $\psi_{t+1} = A_t\psi_t + B_t f_t + \eta_t$                  |                                           |
| **Retrieval**   | Access items using cue/context                  | $a(i\|\text{cue}) = f_i^\top W\psi(\text{cue})$ |                                           |
| **Updating**    | Revise stored weights after output              | $W \leftarrow (1 - \lambda)W + \lambda f_{out} \otimes \psi$ |                                           |

### Representational Domains

* **Physical space:** external features (stimuli, percepts).
* **Psychological space:** internal representations of items and contexts.

---

## 2. The Unified Operator Equation

All memory models can be represented by a shared encoding–retrieval operator:

$$W = \sum_{t=1}^{T}\gamma_t f_t \otimes \psi_t, \quad a(i|\text{cue}) = f_i^\top W\psi(\text{cue})$$

where:

* $f_t$ = item vector,
* $\psi_t$ = context vector,
* $\gamma_t$ = encoding strength,
* $W$ = item–context binding operator.

This operator defines a multidimensional functional space from which all major STM models can be derived as constrained forms.

---

## 2.1 Model-Specific Mappings to the Unified Operator Equation

Each major STM model can be expressed as a specific instantiation of the unified operator equation $W = \sum_{t=1}^{T}\gamma_t f_t \otimes \psi_t$ with particular forms for $f_t$, $\psi_t$, and $\gamma_t$:

[[REM in operator]]
### TCM (Temporal Context Model)
**Unified Form:**
- $f_t$ = item vector (orthogonal or similarity-based)
- $\psi_t$ = temporal context vector with drift: $\psi_{t+1} = \rho\psi_t + \eta f_t$
- $\gamma_t$ = 1 (constant encoding)
- $W = \sum_{t=1}^{T} f_t \otimes \psi_t$

**Key Features:** Context drift parameter $\rho$ controls forgetting; $\eta$ controls item-context binding strength.

### CRU (Context Retrieval and Updating)
**Unified Form:**
- $f_t$ = item vector
- $\psi_t$ = context as mixture of previous items: $\psi_t = \sum_{k<t} \alpha_{tk} f_k$
- $\gamma_t$ = encoding strength
- $W = \sum_{t=1}^{T} \gamma_t f_t \otimes \psi_t$

**Key Features:** Context explicitly modeled as weighted combination of previous items; links recall and recognition.

### SIMPLE (Scale-Invariant Memory, Perception, and Learning)
**Unified Form:**
- $f_t$ = temporal position vector
- $\psi_t$ = temporal context (log-transformed time)
- $\gamma_t$ = temporal discriminability: $e^{-\lambda|\log t_i - \log t|}$
- $W = \sum_{t=1}^{T} \gamma_t f_t \otimes \psi_t$

**Key Features:** Temporal distance metric in log space; predicts recency and list-length effects.

### OSCAR (Oscillator-based Associative Recall)
**Unified Form:**
- $f_t$ = item vector
- $\psi_t$ = oscillatory context: $[\cos(\omega_k t), \sin(\omega_k t)]_k$ for multiple frequencies
- $\gamma_t$ = 1 (constant encoding)
- $W = \sum_{t=1}^{T} f_t \otimes \psi_t$

**Key Features:** Multiple oscillatory frequencies capture rhythmic grouping and temporal structure.

### Burgess-Hitch Model (SEM)
**Unified Form:**
- $f_t$ = item vector
- $\psi_t$ = positional context vector $e_{p(t)}$ (unit vector for position $p(t)$)
- $\gamma_t$ = encoding strength
- $W = \sum_{t=1}^{T} \gamma_t f_t \otimes e_{p(t)}$

**Key Features:** Explicit positional coding; captures positional errors and protrusion gradients.

### Davelaar et al. Model
**Unified Form:**
- $f_t$ = item vector
- $\psi_t$ = context vector with decay: $\psi_t = \rho^t \psi_0 + \sum_{k=1}^{t} \rho^{t-k} f_k$
- $\gamma_t$ = decay-weighted encoding: $\rho^{T-t}$
- $W = \sum_{t=1}^{T} \rho^{T-t} f_t \otimes \psi_t$

**Key Features:** Exponential decay of both context and encoding strength; predicts recency effects.

### Page & Norris Primacy Model
**Unified Form:**
- $f_t$ = item vector
- $\psi_t$ = positional context (primacy-weighted)
- $\gamma_t$ = primacy gradient: $e^{-\lambda t}$ (stronger encoding for early items)
- $W = \sum_{t=1}^{T} e^{-\lambda t} f_t \otimes \psi_t$

**Key Features:** Primacy gradient in encoding strength; explains better recall of early list items.

### Lewandowsky 2008 SOB (Serial Order in a Box)
**Unified Form:**
- $f_t$ = item vector
- $\psi_t$ = context vector with novelty weighting
- $\gamma_t$ = novelty-weighted encoding: $n_t$ (novelty of item $t$)
- $W = \sum_{t=1}^{T} n_t f_t \otimes \psi_t$

**Key Features:** Novelty-gated encoding; explains similarity effects and serial position curves.

### Henson Start-End Model
**Unified Form:**
- $f_t$ = item vector
- $\psi_t$ = dual context: $[\psi_{start}, \psi_{end}]$ where $\psi_{start} = \sum_{k=1}^{t} f_k$ and $\psi_{end} = \sum_{k=t}^{T} f_k$
- $\gamma_t$ = 1 (constant encoding)
- $W = \sum_{t=1}^{T} f_t \otimes [\psi_{start}, \psi_{end}]$

**Key Features:** Dual positional coding (start and end anchors); explains positional effects and transposition gradients.

---

## 2.2 Mathematical Space Categorization of STM Models

Each model can be classified according to the mathematical space structure it employs:

### Product Space (Separable Item × Context)
**Mathematical Structure:** $a(i|\text{cue}) = \sum_t \gamma_t \langle f_i,f_t\rangle \langle \psi(\text{cue}),\psi_t\rangle$

**Models:**
- **Burgess-Hitch (SEM):** $\psi_t = e_{p(t)}$ (unit vectors)
- **OSCAR:** $\psi_t = [\cos(\omega_k t),\sin(\omega_k t)]_k$ (oscillatory)
- **Henson Start-End:** $\psi_t = [\psi_{start}, \psi_{end}]$ (dual anchors)

**Characteristics:** Explicit positional coding, bilinear retrieval, separable item-context spaces.

### Embedding Space (Context → Item Space)
**Mathematical Structure:** $a(i|\text{cue}) = f_i^\top E\psi(\text{cue})$ where $E: \mathcal{C} \to \mathcal{F}$

**Models:**
- **Page & Norris Primacy:** $E\psi(\text{cue}) = \text{primacy-weighted position}$

**Characteristics:** Context absorbed into item similarity metric, unary retrieval.

### Joint Embedding Space (Co-evolving Item–Context)
**Mathematical Structure:** $\psi_{t+1} = \rho\psi_t + \eta f_t + \epsilon_t$

**Models:**
- **TCM:** $\psi_{t+1} = \rho\psi_t + \eta f_t$
- **CRU:** $\psi_t = \sum_{k<t} \alpha_{tk} f_k$ (context as item mixture)
- **REM:** $\psi_{t+1} = \rho\psi_t + \eta f_t$ (with stochastic sampling)
- **Lewandowsky SOB:** $\psi_t$ with novelty weighting $\gamma_t = n_t$

**Characteristics:** Dynamic context evolution, captures sequential dependencies.

### Pure Summation Space (Additive Accumulation)
**Mathematical Structure:** $a(i|\text{cue}) = \sum_t \gamma_t f_i^\top f_t$

**Models:**
- **Davelaar et al.:** $\gamma_t = \rho^{T-t}$ (exponential decay)
- **Basic EBRW:** Pure similarity accumulation

**Characteristics:** No explicit context representation, direct item-item similarity.

### Hilbert Space (Infinite-Dimensional Functional)
**Mathematical Structure:** $a(i|\text{cue}) = \langle f_i, W\psi(\text{cue})\rangle_{\mathcal{H}}$

**Models:**
- **Advanced REM variants:** High-dimensional feature spaces
- **Connectionist models:** Neural network representations

**Characteristics:** Infinite-dimensional representations, kernel-based similarity.

### Tensor Product Space (Multi-dimensional Binding)
**Mathematical Structure:** $W = \sum_t \gamma_t f_t \otimes \psi_t \otimes \phi_t$ (higher-order tensors)

**Models:**
- **Multi-modal STM:** Visual + auditory + semantic binding
- **Hierarchical models:** Multiple levels of representation

**Characteristics:** Multi-dimensional binding, hierarchical structure.

### Probabilistic Space (Stochastic Operators)
**Mathematical Structure:** $a(i|\text{cue}) = \mathbb{E}[f_i^\top W\psi(\text{cue})]$ where $W$ is stochastic

**Models:**
- **REM:** Stochastic sampling from similarity distributions
- **Monte Carlo STM:** Probabilistic retrieval processes

**Characteristics:** Stochastic retrieval, uncertainty quantification.

### Metric Space (Distance-Based)
**Mathematical Structure:** $a(i|\text{cue}) = d(f_i, \psi(\text{cue}))$ where $d$ is a metric

**Models:**
- **SIMPLE:** $d(f_i, \psi(\text{cue})) = e^{-\lambda|\log t_i - \log t|}$
- **MDS-based models:** Multidimensional scaling approaches

**Characteristics:** Distance-based similarity, geometric interpretation.

### Summary: Model Classification by Mathematical Space

| Model | Primary Space | Secondary Features | Mathematical Signature |
|-------|---------------|-------------------|----------------------|
| **Burgess-Hitch (SEM)** | Product Space | Unit vectors | $\psi_t = e_{p(t)}$ |
| **OSCAR** | Product Space | Oscillatory | $\psi_t = [\cos(\omega_k t),\sin(\omega_k t)]_k$ |
| **Henson Start-End** | Product Space | Dual anchors | $\psi_t = [\psi_{start}, \psi_{end}]$ |
| **SIMPLE** | Metric Space | Temporal distance | $d(f_i, \psi) = e^{-\lambda\|\log t_i - \log t\|}$ |
| **Page & Norris Primacy** | Embedding Space | Primacy gradient | $\gamma_t = e^{-\lambda t}$ |
| **TCM** | Joint Embedding | Context drift | $\psi_{t+1} = \rho\psi_t + \eta f_t$ |
| **CRU** | Joint Embedding | Item mixture | $\psi_t = \sum_{k<t} \alpha_{tk} f_k$ |
| **REM** | Probabilistic Space | Stochastic sampling | $\mathbb{E}[f_i^\top W\psi]$ |
| **Lewandowsky SOB** | Joint Embedding | Novelty weighting | $\gamma_t = n_t$ |
| **Davelaar et al.** | Pure Summation | Exponential decay | $\gamma_t = \rho^{T-t}$ |

### Complete Model Inventory by Space Category

**Product Space (3 models):**
- Burgess-Hitch (SEM)
- OSCAR  
- Henson Start-End

**Embedding Space (1 model):**
- Page & Norris Primacy

**Joint Embedding Space (3 models):**
- TCM
- CRU
- Lewandowsky SOB

**Pure Summation Space (1 model):**
- Davelaar et al.

**Probabilistic Space (1 model):**
- REM

**Metric Space (1 model):**
- SIMPLE

**Total: 10 models across 6 mathematical space categories**

### Space Hierarchy and Relationships

The mathematical spaces form a hierarchy from simple to complex:

1. **Pure Summation** → **Metric Space** → **Embedding Space** → **Product Space** → **Joint Embedding** → **Probabilistic Space** → **Hilbert Space** → **Tensor Product Space**

Each level adds computational complexity but also increases representational power and psychological realism.

---

## 3. Mathematical Branching: The Three Integration Regimes

### 3.1 Product Space (Separable Item × Context)

**Derivation:**
$$a(i|\text{cue}) = \sum_t \gamma_t \langle f_i,f_t\rangle \langle \psi(\text{cue}),\psi_t\rangle$$

**Interpretation:** Item and context are separate spaces; retrieval is bilinear.

**Examples:**

* **SEM / Burgess–Hitch (1992–2006):** $\psi_t = e_{p(t)}$; captures positional errors, protrusion gradients.
* **OSCAR (Brown et al., 2000):** $\psi_t = [\cos(\omega_k t),\sin(\omega_k t)]_k$; explains rhythmic grouping.
* **Farrell (2012):** hierarchical positional codes; explains chunking.

**Abstractly:** Retrieval similarity = $s = s_f(i,t) \cdot s_\psi(t)$. Separable spaces enable explicit positional coding but lack contiguity asymmetry.

---

### 3.2 Embedding (Context Absorbed into Item Space)

**Derivation:** Let $E: \mathcal{C} \to \mathcal{F}$ and $W=I$. Then:
$$a(i|\text{cue}) = f_i^\top E\psi(\text{cue})$$

**Interpretation:** Retrieval is unary; context collapsed into item metric.

**Examples:**

* **SIMPLE (Brown et al., 2007):** forgetting via temporal distance metric $s(i,t) = e^{-\lambda|\log t_i - \log t|}$; predicts recency and list-length effects.
* **EBRW (Nosofsky, 1991; Shiffrin & Steyvers, 1997):** accumulation of similarity-based evidence; predicts recognition RT and set-size effects.

**Abstractly:** retrieval operates purely on feature similarity; context is implicit in the probe.

---

### 3.3 Joint Embedding (Co-evolving Item–Context)

**Derivation:** Context evolves dynamically with items:
$$\psi_{t+1} = \rho\psi_t + \eta f_t + \epsilon_t$$

Then:
$$W = \sum_t \gamma_t f_t \otimes (\rho^{t-1}\psi_1 + \eta \sum_{k<t}\rho^{t-k-1} f_k)$$

**Examples:**

* **TCM (Howard & Kahana, 2002):** $\psi_{t+1} = \rho\psi_t + \eta f_t$; predicts lag-CRP asymmetry.
* **CRU (Logan, 2021):** context as item mixture; links recall and recognition.
* **SOB (Johnson et al., 2022):** novelty-weighted $\gamma_t$; predicts similarity–novelty interplay.

**Abstractly:** retrieval depends on full item–context trajectory; captures sequential dynamics but lacks explicit positional coding.

---

## 4. Unified Mathematical Divergences

Starting from $a(i|\text{cue})=f_i^\top W\psi(\text{cue})$, model families diverge along three orthogonal axes:

| Axis                  | Mathematical Difference                                             | Psychological Meaning                                            |
| --------------------- | ------------------------------------------------------------------- | ---------------------------------------------------------------- |
| **Spatial coupling**  | Relation between item and context spaces (product, embedded, joint) | Independence vs. integration of item and context representations |
| **Temporal coupling** | Dynamics of $\psi_t$: static, oscillatory, drifting                 | Encoding–retrieval stability and contiguity                      |
| **Decision coupling** | Mapping of activation $a(i)$ to response                            | Single- vs. multi-stage retrieval, confidence, RT                |

These axes define a *continuous model manifold*. Most existing models occupy only discrete corners.

---

## 5. The Unified Treatment of Forgetting and Maintenance

### 5.1 Core insight

All forms of forgetting—decay, interference, distinctiveness loss—arise from *reducing overlap* between study and test contexts. The difference lies in **where the loss is applied** within the operator equation.

$$a(i|\text{cue}) = f_i^\top (D_f W D_\psi)\psi(\text{cue})$$
where decay operators $D_f,D_\psi$ act on items, contexts, or both.

### 5.2 Placement variants

| Level              | Mathematical Form                    | Typical Model | Conceptual Meaning                 |        |                                  |
| ------------------ | ------------------------------------ | ------------- | ---------------------------------- | ------ | -------------------------------- |
| Temporal metric    | $D_\psi = e^{-\lambda                \| t_i - t_j     \| }$                                 | SIMPLE | Time-based discriminability loss |
| Context drift      | $\psi_{t+1} = \rho\psi_t + \eta f_t$ | TCM           | Gradual context decorrelation      |        |                                  |
| Encoding weight    | $\gamma_t = n_t$ (novelty gating)    | SOB           | Attention/novelty-driven loss      |        |                                  |
| Decision weighting | $a_t = e^{-\lambda t}$               | EBRW          | Evidence decay during accumulation |        |                                  |
| Weight decay       | $W_{t+1} = (1-\lambda)W_t+\dots$     | ACT-R, SAM    | Connection-strength decay          |        |                                  |

Each represents the same formal process: *loss of representational alignment* between item and context spaces.

### 5.3 Maintenance–Forgetting Trade-offs

Study-phase stability: $\psi_{t+1}^{study} = \rho\psi_t + \eta f_t$.
Test-phase updating: $\psi_{n+1}^{test} = (1-\lambda)\psi_n + \lambda f_{retrieved}$.

Trade-off surface:
$$R(\rho,\lambda) = \langle \psi_T^{study}, \psi_N^{test}\rangle = \rho^T (1-\lambda)^N + \eta\lambda\sum_{t,n}\langle f_t,f_n\rangle$$

High $\rho$: stable encoding, poor list separation.
High $\lambda$: strong contiguity, high output interference.

---

## 6. Historical Treatment of Forgetting in the Memory Field

| Theoretical Tradition                          | Mechanism            | Mathematical Locus      | Trade-off Focus                           |
| ---------------------------------------------- | -------------------- | ----------------------- | ----------------------------------------- |
| **Multi-store (Atkinson & Shiffrin, 1968)**    | Trace decay          | magnitude of $W$        | Capacity vs. flexibility                  |
| **Interference / Cue overload**                | Competition          | overlap of $f_t,\psi_t$ | Cue specificity vs. interference          |
| **Context drift (Mensink & Raaijmakers, TCM)** | Drift in $\psi_t$    | context evolution       | Within-list coherence vs. list separation |
| **Distinctiveness (SIMPLE)**                   | Temporal compression | metric distortion       | Scale invariance vs. order information    |
| **Sampling / REM**                             | Stochastic retrieval | operator expectation    | Retrieval variability vs. speed           |
| **Connectionist (SOB, ACT-R)**                 | Weight decay         | synaptic weight $W$     | Stability vs. adaptability                |

These traditions differ not in substance but in *placement* of the same mathematical loss operator.

---

## 7. Fundamental Structures Revealed by the Framework

### 7.1 Operator Compositionality

All memory dynamics—encoding, drift, decay, decision—are compositions of operators within $\mathcal{M} = \{W, D_f, D_\psi, \mathcal{D}\}$. This defines an algebra of memory processes.

### 7.2 Trade-off Manifold

Continuous surface $R(\rho,\lambda)$ formalizes verbal trade-offs between maintenance and interference as quantitative manifolds.

### 7.3 Duality Between Similarity and Sampling

Deterministic similarity models and stochastic sampling models are dual: similarity = expectation over samples. This explains why REM and TCM predict similar trends under different formalisms.

---

## 8. The Operator Placement Framework for Forgetting

This framework allows modelers to *insert* forgetting deliberately where desired, using unified notation. Each placement yields predictable consequences for behavior, RT, and interference patterns.

$$a(i|\text{cue}) = f_i^\top (D_f W D_\psi)\psi(\text{cue})$$
with optional dynamic drift or diffusion on $\psi$.

| Placement                      | Psychological Interpretation | Predictive Consequence         |
| ------------------------------ | ---------------------------- | ------------------------------ |
| On metric (SIMPLE-type)        | Temporal distinctiveness     | Recency, time-scale invariance |
| On context (TCM-type)          | Context drift                | Lag-CRP asymmetry, contiguity  |
| On decision (EBRW-type)        | Evidence decay               | RT distributions               |
| On encoding weights (SOB-type) | Novelty modulation           | Similarity effects             |
| On operator (ACT-R type)       | Connection decay             | Long-term forgetting curves    |

---

## 9. Implications

1. **Revealed structure:** Forgetting, interference, and maintenance are unified as operator placements in the same equation.
2. **New model space:** Empty regions correspond to hybrid placements (e.g., time + context decay) not yet explored.
3. **Empirical leverage:** Enables predictions of how moving the decay locus changes observable forgetting functions.
4. **Theoretical integration:** Connects episodic models (REM, TCM, SIMPLE) to classical STM and decision frameworks.

This is not a summary—it’s a structural synthesis that exposes the algebraic skeleton of memory models, quantifies classical trade-offs, and creates a generative space for new theory development.
