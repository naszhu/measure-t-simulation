# **From Operators to Measures: Revealing the Hidden Gap in Memory Models**

## 1. Motivation

Current memory models—from TCM and SIMPLE to REM—share a deep structural unity, as shown in the *Unified Operator Framework for Short-Term Memory Models*. Yet they implicitly assume that the cognitive system operates on *sets of states* rather than *measures over representational spaces*. This assumption leads to a conceptual gap: the models capture *which representations exist* (sets, vectors) but not *how representational density or granularity evolves* (measures, refinements).

In mathematical terms, most models treat memory as **functions on discrete sets**, while empirical phenomena (drift, generalization, forgetting) reveal behavior that is inherently **measure-preserving or measure-distorting**. The gap lies between *operator composition* (mapping structures) and *measure transformation* (density dynamics).

---

## 2. Identified Gap: Lack of Measure-Theoretic Treatment

| Level                     | Typical Model | Mathematical Nature                       | Missing Element                             |
| ------------------------- | ------------- | ----------------------------------------- | ------------------------------------------- |
| **Item-context operator** | TCM, SEM, SOB | Linear operator on vectors                | No notion of representational density       |
| **Similarity metric**     | SIMPLE, GCM   | Deterministic distance measure            | No conservation or diffusion of mass        |
| **Sampling framework**    | REM, SAM      | Probabilistic over discrete memory traces | No continuous measure or refinement mapping |

Thus, all models implicitly fix representational *granularity*. They cannot describe what happens when the system *refines* or *coarsens* its units of representation—that is, when the *measure of representation changes*.

---

## 3. Conceptual Bridge: The Measure–Operator Duality

### 3.1 Definition

Let memory be a measure space $(\Omega, \mathcal{F}, \mu)$, where $\mu$ quantifies representational density (activation, precision, or available cognitive resource).

Encoding and retrieval then act as **measure-transforming operators**:
$$\mu_{t+1} = T_t \mu_t$$
where $T_t$ may preserve, contract, or redistribute the total measure.

### 3.2 Interpretation

* **Operator view (classic models):** memory evolves through vector transformations $(W, D_f, D_\psi)$.
* **Measure view (proposed):** memory evolves through density redistribution across representational space.

**Drift**, **forgetting**, and **interference** correspond not merely to vector changes but to changes in *the density measure* over representational states.

---

## 4. The Proposed Model: The Measure-Refinement Memory (MRM) Model

### 4.1 Core Principle

Memory dynamics are **measure-preserving refinements** followed by **operator-induced compressions**:

$$\mu_{t+1} = D_t (R_t \mu_t)$$

where:

* $R_t$: refinement operator (adds granularity, splits representational atoms),
* $D_t$: decay/compression operator (reduces total measure or merges subspaces).

### 4.2 Psychological Interpretation

* Encoding = refinement: adding distinctiveness (more microstates per item).
* Forgetting = compression: merging previously distinct microstates (loss of granularity).
* Interference = partial overlap between refined and compressed measures.

### 4.3 Relation to Existing Models

| Model          | Equivalent Mechanism      | In MRM terms                              |
| -------------- | ------------------------- | ----------------------------------------- |
| TCM            | Context drift             | gradual shift of measure centroid         |
| SIMPLE         | Temporal scaling          | metric compression along temporal axis    |
| REM            | Sampling variability      | stochastic redistribution of measure mass |
| MRM (proposed) | explicit measure dynamics | joint refinement + compression cycle      |

---

## 5. Formal Structure

Let each encoded trace be represented by a local measure patch $\mu_i$ with total mass $m_i$. Then:

1. **Encoding (refinement)**: $\mu_i^{enc} = R_i(\mu_{i-1}) = \mu_{i-1} \ast K_i$, where $K_i$ is a refinement kernel that increases representational resolution.
2. **Maintenance**: $\mu_i^{maint} = (1 - \lambda)\mu_i^{enc} + \lambda\eta$, conserving total mass but diffusing it.
3. **Retrieval**: similarity is defined as measure overlap:
   $$a(i|cue) = \int f_i(x) f_{cue}(x) \, d\mu(x)$$
4. **Forgetting (compression)**: $\mu_{t+1}^{comp} = D_t(\mu_t) = \int K_t(x,y) \, d\mu_t(y)$, with $K_t$ a contraction kernel.

---

## 6. Predictions

1. **Dynamic Granularity:** Representational units will vary in resolution across encoding and test. Neural representational similarity (RSA) matrices should show *progressive smoothing* with delay.
2. **Nonlinear Forgetting:** Forgetting curves follow *measure compression dynamics*, typically sub-exponential rather than power-law.
3. **List-Context Dependence:** Overlap between refined and compressed measures predicts asymmetric interference between short and long lists.
4. **Memory Capacity as Conservation Law:** Total representational mass $(\int d\mu)$ remains constant; only redistributed—explaining resource-like constraints.

---

## 7. Experimental Design

### 7.1 Behavioral Paradigm

* **Task:** delayed recognition with varying list lengths and interpolated noise contexts.
* **Manipulation:** noise corresponds to *measure diffusion*; more noise = higher diffusion parameter.
* **Prediction:** nonuniform forgetting across list positions; earlier items show stronger compression.

### 7.2 Neural Prediction

* Use **RSA or pattern entropy** over time (fMRI/EEG).
* Refinement phase: pattern differentiation increases (entropy up).
* Compression phase: pattern similarity increases (entropy down).
* Plot entropy trajectory as empirical estimate of measure dynamics.

### 7.3 Computational Simulation

* Simulate vector representations with Gaussian kernels.
* Apply alternating refinement and compression operators.
* Fit to human data; compare with SIMPLE (pure compression) and TCM (pure drift).

---

## 8. Broader Implications

### 8.1 Theoretical

The Measure-Refinement Memory model unifies:

* Discrete symbolic models (operators) and continuous metric models (measures).
* Forgetting, interference, and generalization as *measure-transforming* processes.

### 8.2 Methodological

This framework connects cognitive modeling with modern mathematical tools:

* Measure theory and transport (Wasserstein metrics, optimal transport)
* Information geometry (entropy-based capacity laws)
* Neural field theory (density dynamics in cortical space)

### 8.3 Conceptual

Cognition is not merely *mapping states* (set-based), but *redistributing density* (measure-based).
Memory is not storage; it is **measure flow** through representational space.

---

## 9. Conclusion

The *Measure-Refinement Memory (MRM)* model extends the Unified Operator Framework by embedding it in measure theory.
It exposes the missing layer of **representational granularity**, providing a bridge between discrete symbolic operators and continuous neural dynamics.
By viewing encoding and forgetting as **refinement–compression cycles** on a conserved representational measure, the model predicts new forms of forgetting, interference, and generalization—measurable both behaviorally and neurally.

This measure-based reformulation thus fills a long-standing theoretical gap: it turns the algebra of memory into a **dynamics of representational density**, reconciling classical memory theory with the mathematical language of modern dynamical systems and information geometry.
