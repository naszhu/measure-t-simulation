# **Unified Operator Framework for Short-Term Memory Models**

## 1. The General STM Paradigm

Short-term memory (STM) tasks follow a common two-phase structure:

1. **Study phase:** a sequence of items is presented, each associated with a temporal or contextual position.
2. **Test phase:** one or more probes are presented, requiring recall or recognition of items in order or by cue.

### Core Cognitive Processes

| Process         | Function                                        | Mathematical Representation                                  |                                           |
| --------------- | ----------------------------------------------- | ------------------------------------------------------------ | ----------------------------------------- |
| **Encoding**    | Transform stimuli into internal representations | (f_t = \Phi_{item}(x_t)), (\psi_t = \Phi_{context}(y_t))     |                                           |
| **Maintenance** | Sustain or transform context                    | (\psi_{t+1} = A_t\psi_t + B_t f_t + \eta_t)                  |                                           |
| **Retrieval**   | Access items using cue/context                  | (a(i                                                         | \text{cue}) = f_i^\top W\psi(\text{cue})) |
| **Updating**    | Revise stored weights after output              | (W \leftarrow (1 - \lambda)W + \lambda f_{out} \otimes \psi) |                                           |

### Representational Domains

* **Physical space:** external features (stimuli, percepts).
* **Psychological space:** internal representations of items and contexts.

---

## 2. The Unified Operator Equation

All memory models can be represented by a shared encoding–retrieval operator:

[W = \sum_{t=1}^{T}\gamma_t f_t \otimes \psi_t, \quad a(i|\text{cue}) = f_i^\top W\psi(\text{cue})]

where:

* (f_t) = item vector,
* (\psi_t) = context vector,
* (\gamma_t) = encoding strength,
* (W) = item–context binding operator.

This operator defines a multidimensional functional space from which all major STM models can be derived as constrained forms.

---

## 3. Mathematical Branching: The Three Integration Regimes

### 3.1 Product Space (Separable Item × Context)

**Derivation:**
[a(i|\text{cue}) = \sum_t \gamma_t \langle f_i,f_t\rangle \langle \psi(\text{cue}),\psi_t\rangle.]

**Interpretation:** Item and context are separate spaces; retrieval is bilinear.

**Examples:**

* **SEM / Burgess–Hitch (1992–2006):** (\psi_t = e_{p(t)}); captures positional errors, protrusion gradients.
* **OSCAR (Brown et al., 2000):** (\psi_t = [\cos(\omega_k t),\sin(\omega_k t)]_k); explains rhythmic grouping.
* **Farrell (2012):** hierarchical positional codes; explains chunking.

**Abstractly:** Retrieval similarity = (s = s_f(i,t)·s_\psi(t)). Separable spaces enable explicit positional coding but lack contiguity asymmetry.

---

### 3.2 Embedding (Context Absorbed into Item Space)

**Derivation:** Let (E: \mathcal C \to \mathcal F) and (W=I). Then:
[a(i|\text{cue}) = f_i^\top E\psi(\text{cue}).]

**Interpretation:** Retrieval is unary; context collapsed into item metric.

**Examples:**

* **SIMPLE (Brown et al., 2007):** forgetting via temporal distance metric (s(i,t) = e^{-\lambda|\log t_i - \log t|}); predicts recency and list-length effects.
* **EBRW (Nosofsky, 1991; Shiffrin & Steyvers, 1997):** accumulation of similarity-based evidence; predicts recognition RT and set-size effects.

**Abstractly:** retrieval operates purely on feature similarity; context is implicit in the probe.

---

### 3.3 Joint Embedding (Co-evolving Item–Context)

**Derivation:** Context evolves dynamically with items:
[\psi_{t+1} = \rho\psi_t + \eta f_t + \epsilon_t.]

Then:
[W = \sum_t \gamma_t f_t \otimes (\rho^{t-1}\psi_1 + \eta \sum_{k<t}\rho^{t-k-1} f_k).]

**Examples:**

* **TCM (Howard & Kahana, 2002):** (\psi_{t+1} = \rho\psi_t + \eta f_t); predicts lag-CRP asymmetry.
* **CRU (Logan, 2021):** context as item mixture; links recall and recognition.
* **SOB (Johnson et al., 2022):** novelty-weighted (\gamma_t); predicts similarity–novelty interplay.

**Abstractly:** retrieval depends on full item–context trajectory; captures sequential dynamics but lacks explicit positional coding.

---

## 4. Unified Mathematical Divergences

Starting from (a(i|\text{cue})=f_i^\top W\psi(\text{cue})), model families diverge along three orthogonal axes:

| Axis                  | Mathematical Difference                                             | Psychological Meaning                                            |
| --------------------- | ------------------------------------------------------------------- | ---------------------------------------------------------------- |
| **Spatial coupling**  | Relation between item and context spaces (product, embedded, joint) | Independence vs. integration of item and context representations |
| **Temporal coupling** | Dynamics of (\psi_t): static, oscillatory, drifting                 | Encoding–retrieval stability and contiguity                      |
| **Decision coupling** | Mapping of activation (a(i)) to response                            | Single- vs. multi-stage retrieval, confidence, RT                |

These axes define a *continuous model manifold*. Most existing models occupy only discrete corners.

---

## 5. The Unified Treatment of Forgetting and Maintenance

### 5.1 Core insight

All forms of forgetting—decay, interference, distinctiveness loss—arise from *reducing overlap* between study and test contexts. The difference lies in **where the loss is applied** within the operator equation.

[a(i|\text{cue}) = f_i^\top (D_f W D_\psi)\psi(\text{cue}),]
where decay operators (D_f,D_\psi) act on items, contexts, or both.

### 5.2 Placement variants

| Level              | Mathematical Form                    | Typical Model | Conceptual Meaning                 |        |                                  |
| ------------------ | ------------------------------------ | ------------- | ---------------------------------- | ------ | -------------------------------- |
| Temporal metric    | (D_\psi = e^{-\lambda                | t_i - t_j     | })                                 | SIMPLE | Time-based discriminability loss |
| Context drift      | (\psi_{t+1} = \rho\psi_t + \eta f_t) | TCM           | Gradual context decorrelation      |        |                                  |
| Encoding weight    | (\gamma_t = n_t) (novelty gating)    | SOB           | Attention/novelty-driven loss      |        |                                  |
| Decision weighting | (a_t = e^{-\lambda t})               | EBRW          | Evidence decay during accumulation |        |                                  |
| Weight decay       | (W_{t+1} = (1-\lambda)W_t+\dots)     | ACT-R, SAM    | Connection-strength decay          |        |                                  |

Each represents the same formal process: *loss of representational alignment* between item and context spaces.

### 5.3 Maintenance–Forgetting Trade-offs

Study-phase stability: (\psi_{t+1}^{study} = \rho\psi_t + \eta f_t).
Test-phase updating: (\psi_{n+1}^{test} = (1-\lambda)\psi_n + \lambda f_{retrieved}).

Trade-off surface:
[R(\rho,\lambda) = \langle \psi_T^{study}, \psi_N^{test}\rangle = \rho^T (1-\lambda)^N + \eta\lambda\sum_{t,n}\langle f_t,f_n\rangle.]

High (\rho): stable encoding, poor list separation.
High (\lambda): strong contiguity, high output interference.

---

## 6. Historical Treatment of Forgetting in the Memory Field

| Theoretical Tradition                          | Mechanism            | Mathematical Locus      | Trade-off Focus                           |
| ---------------------------------------------- | -------------------- | ----------------------- | ----------------------------------------- |
| **Multi-store (Atkinson & Shiffrin, 1968)**    | Trace decay          | magnitude of (W)        | Capacity vs. flexibility                  |
| **Interference / Cue overload**                | Competition          | overlap of (f_t,\psi_t) | Cue specificity vs. interference          |
| **Context drift (Mensink & Raaijmakers, TCM)** | Drift in (\psi_t)    | context evolution       | Within-list coherence vs. list separation |
| **Distinctiveness (SIMPLE)**                   | Temporal compression | metric distortion       | Scale invariance vs. order information    |
| **Sampling / REM**                             | Stochastic retrieval | operator expectation    | Retrieval variability vs. speed           |
| **Connectionist (SOB, ACT-R)**                 | Weight decay         | synaptic weight (W)     | Stability vs. adaptability                |

These traditions differ not in substance but in *placement* of the same mathematical loss operator.

---

## 7. Fundamental Structures Revealed by the Framework

### 7.1 Operator Compositionality

All memory dynamics—encoding, drift, decay, decision—are compositions of operators within (\mathcal{M} = {W, D_f, D_\psi, \mathcal{D}}). This defines an algebra of memory processes.

### 7.2 Trade-off Manifold

Continuous surface (R(\rho,\lambda)) formalizes verbal trade-offs between maintenance and interference as quantitative manifolds.

### 7.3 Duality Between Similarity and Sampling

Deterministic similarity models and stochastic sampling models are dual: similarity = expectation over samples. This explains why REM and TCM predict similar trends under different formalisms.

---

## 8. The Operator Placement Framework for Forgetting

This framework allows modelers to *insert* forgetting deliberately where desired, using unified notation. Each placement yields predictable consequences for behavior, RT, and interference patterns.

[a(i|\text{cue}) = f_i^\top (D_f W D_\psi)\psi(\text{cue}),]
with optional dynamic drift or diffusion on (\psi).

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
