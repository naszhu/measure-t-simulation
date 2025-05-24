# **From Signal Detection to Measure-Theoretic Memory: A Unified Framework**

---

## 1. Introduction: From Familiarity Distributions to Measure Transformations

Signal Detection Theory (SDT) has been the foundational framework for recognition memory for over half a century (Green & Swets, 1966; Macmillan & Creelman, 2005). At its core, SDT interprets recognition judgments as comparing two probability distributions: the **familiarity distribution for old items** $P_{old}(f)$ and the **familiarity distribution for new items** $P_{new}(f)$. The decision to respond "old" or "new" depends on whether the observed familiarity value falls above or below a criterion threshold.

This paper argues that SDT's simple but powerful structure—**comparing two probability measures**—can be generalized to encompass all of memory theory. Recognition, recall, forgetting, and context-dependent retrieval all emerge as **transformations of measures** between content space (items, features) and context space (temporal positions, contextual states). SDT's familiarity distributions are **marginal measures** of a richer joint structure; memory models differ not in their fundamental ontology, but in **which measure transformations they employ** and **where these transformations are applied**.

### 1.1 The Central Thesis

**All memory processes (encoding, retrieval, forgetting, generalization) can be expressed as transformations of probability measures between content and context spaces—generalizing SDT's measure-comparison structure through richer transformations (push-forward, kernel, density change).**

This measure-theoretic perspective provides:
- **Theoretical grounding:** SDT provides the simplest measure-comparison form; all memory models extend this structure
- **Unification:** A common mathematical language linking SDT to TCM, REM, SIMPLE, CRU, and other models
- **Generativity:** A framework for constructing new models by combining transformation types
- **Geometric intuition:** Memory judgments as measure comparisons across representational manifolds

### 1.2 From SDT to General Memory Models

SDT considers only **one dimension** (familiarity) and compares two **marginal measures** (old vs. new). Memory models extend this structure by:

1. **Adding context dimension:** Joint measures $\mu(x, \psi)$ over content × context space
2. **Richer transformations:** Push-forward (deterministic drift), kernel (stochastic retrieval), density change (attentional weighting)
3. **Temporal dynamics:** Measures evolve over time via transformation sequences
4. **Conditional retrieval:** Recall emerges as conditional measures $\mu(x|\psi)$ given specific contexts

**The Unified Claim:** SDT is the **1D marginal limit** of a general measure-transformation framework. All memory models are **extensions** of SDT's measure-comparison structure to higher-dimensional spaces and richer transformations.

---

## 2. SDT as Measure Comparison

### 2.1 Formal Definition of SDT

**Definition 2.1** (Signal Detection Theory). In SDT, recognition memory is modeled by:

1. **Two probability measures** on a **familiarity space** $\Omega_F$:
   - $\mu_{old}$: Probability measure for old (studied) items
   - $\mu_{new}$: Probability measure for new (unstudied) items

2. **Decision rule:** Respond "old" if the observed familiarity value $f$ satisfies:

$$\frac{d\mu_{old}}{d\mu_{new}}(f) > c$$

where $c$ is the decision criterion (likelihood ratio threshold).

**Assumptions:**

- Both measures are **absolutely continuous** with respect to a base measure (typically Lebesgue measure)
- They have **densities** $p_{old}(f) = \frac{d\mu_{old}}{df}$ and $p_{new}(f) = \frac{d\mu_{new}}{df}$
- The decision rule is based on the **likelihood ratio** $\frac{p_{old}(f)}{p_{new}(f)}$

### 2.2 SDT's Geometric Structure

**Geometric Interpretation:**

SDT compares two measures along a **single axis** (familiarity). The decision corresponds to:

1. **Measuring familiarity** $f$ for the test probe
2. **Comparing densities** $p_{old}(f)$ vs. $p_{new}(f)$
3. **Threshold decision** based on likelihood ratio

**Visualization:**

The classic SDT plot shows two **overlapping distributions** along the familiarity axis:
- $p_{old}(f)$: typically shifted to the right (higher familiarity)
- $p_{new}(f)$: typically centered at lower familiarity values
- **Criterion $c$:** vertical line separating "old" and "new" responses

### 2.3 SDT as Marginal Measure Comparison

**Key Insight:** SDT's measures $\mu_{old}$ and $\mu_{new}$ are **marginal measures** of a richer joint structure.

**Joint Measure Construction:**

Suppose memory is encoded as a **joint measure** $\mu_{study}(x, \psi)$ over content space $\Omega_{\mathcal{F}}$ (items, features) and context space $\Omega_{\mathcal{C}}$ (temporal positions, contextual states).

**Marginal Measures:**

- **Old items:** $\mu_{old}(dx) = \int_{\Omega_{\mathcal{C}}} d\mu_{study}(x, \psi)$ (marginal over context for studied items)
- **New items:** $\mu_{new}(dx) = \int_{\Omega_{\mathcal{C}}} d\mu_{unstudied}(x, \psi)$ (marginal for unstudied items)

**SDT's Recognition Decision:**

Recognition becomes a comparison of these marginal measures:

$$\text{Respond "old" if } \frac{d\mu_{old}}{d\mu_{new}}(f) > c$$

where $f$ is the familiarity value computed from the probe.

### 2.4 SDT as Limit Case of Joint Measures

**Theorem 2.1** (SDT as Marginal Projection). SDT's familiarity comparison is the **marginal projection** of a joint measure-comparison structure when:

1. Context space $\Omega_{\mathcal{C}}$ is **one-dimensional** (or collapsed to a single point)
2. The joint measure factors as: $\mu_{study}(dx, d\psi) = \mu_{\mathcal{F}}(dx) \otimes \mu_{\mathcal{C}}(d\psi)$ (separable)
3. Recognition operates on **marginal familiarity**: $f = \int_{\Omega_{\mathcal{C}}} \langle probe, x \rangle \, d\mu_{study}(x, \psi)$

**Proof Sketch:**

When context space is trivial ($\Omega_{\mathcal{C}} = \{point\}$), the joint measure reduces to:

$$\mu_{study}(dx, d\psi) = \mu_{\mathcal{F}}(dx) \otimes \delta_{point}(d\psi) = \mu_{old}(dx)$$

Recognition becomes:

$$\text{Recognition} = \int_{\Omega_{\mathcal{F}}} \langle probe, x \rangle \, d\mu_{old}(x)$$

which is exactly SDT's familiarity computation. The decision rule:

$$\text{Respond "old" if } \frac{d\mu_{old}}{d\mu_{new}}(f) > c$$

follows directly from the likelihood ratio test.

**Conclusion:** SDT is the **1D marginal case** of a general measure $\mu(x, \psi)$ when context is ignored or collapsed.

---

## 3. Extending SDT to Context–Content Measure Space

### 3.1 Measurable Spaces for Memory

**Definition 3.1** (Memory Space Structure). Extend SDT's one-dimensional familiarity space to a **joint measurable space**:

- **Content space:** $(\Omega_{\mathcal{F}}, \mathcal{B}_{\mathcal{F}})$ representing items, features, or stimuli
- **Context space:** $(\Omega_{\mathcal{C}}, \mathcal{B}_{\mathcal{C}})$ representing temporal positions, contextual states, or episodic markers
- **Joint space:** $(\Omega_{\mathcal{F}} \times \Omega_{\mathcal{C}}, \mathcal{B}_{\mathcal{F}} \otimes \mathcal{B}_{\mathcal{C}})$

**SDT Correspondence:**

- SDT's familiarity space = **1D projection** of $\Omega_{\mathcal{F}}$
- SDT ignores context = **marginalization** over $\Omega_{\mathcal{C}}$

### 3.2 Joint Encoding Measure

**Definition 3.2** (Study-Phase Measure). During study, a sequence of items $\{x_t\}_{t=1}^{T}$ is encoded, producing:

- **Item vectors:** $\{f_t\}$ in $\Omega_{\mathcal{F}}$
- **Context vectors:** $\{\psi_t\}$ in $\Omega_{\mathcal{C}}$

The **study-phase measure** $\mu_{study}$ is defined on $\Omega_{\mathcal{F}} \times \Omega_{\mathcal{C}}$ as:

$$\mu_{study}(A \times B) = \sum_{t=1}^{T} \gamma_t \mathbb{1}_A(f_t) \mathbb{1}_B(\psi_t)$$

where $\gamma_t$ is the encoding strength at time $t$, and $\mathbb{1}_A$ is the indicator function.

**For continuous models:** $\mu_{study}$ may have a density:

$$d\mu_{study}(f, \psi) = w(f, \psi) \, d(f, \psi)$$

where $w(f, \psi)$ is the Radon–Nikodym derivative with respect to a base measure (e.g., Lebesgue or counting measure).

### 3.3 Recognition as Measure Comparison

**Extension of SDT's Decision Rule:**

In SDT, recognition compares two marginal measures: $\mu_{old}$ vs. $\mu_{new}$.

**Generalized Recognition:**

Recognition now compares:
- **Study measure:** $\mu_{study}(f, \psi)$ (joint measure over content × context)
- **Test measure:** $\mu_{test}(f, \psi) = T_{\#}\mu_{study}(f, \psi)$ (transformed study measure via push-forward $T$)

**Decision Criterion:**

Instead of simple likelihood ratio, recognition uses **measure divergence**:

$$\text{Respond "old" if } D(\mu_{study}, \mu_{test}) < \text{threshold}$$

where $D$ is a divergence measure (e.g., KL divergence, Wasserstein distance, total variation).

**SDT as Special Case:**

When context is collapsed and test measure = study measure:

$$\mu_{test} = \mu_{study} = \mu_{old}$$

Then recognition becomes:

$$\text{Respond "old" if } \frac{d\mu_{old}}{d\mu_{new}}(f) > c$$

which is exactly SDT's likelihood ratio rule.

### 3.4 Psychological Concepts as Measure-Theoretic Objects

| Psychological Concept | Mathematical Object | SDT Analogue |
|---------------------|-------------------|--------------|
| **Familiarity** | Marginal density overlap: $\int_{\mathcal{C}} d\mu_{study}(f, \psi)$ | $p_{old}(f)$ vs. $p_{new}(f)$ |
| **Context reinstatement** | Push-forward of measure: $T_{\#}\mu_{study}$ | Shift in familiarity distribution |
| **Retrieval similarity** | Kernel inner product: $\int K(\text{cue}, d\psi) \, d\mu_{study}(f, \psi)$ | Expectation under familiarity kernel |
| **Forgetting** | Reduction of measure overlap or total mass: $\|\mu_{study} - \mu_{test}\|$ | Divergence of $p_{old}$ from original form |
| **Recognition** | Comparison of marginal measures | Likelihood ratio comparison |
| **Recall** | Conditional measure restriction: $\mu(f \mid \psi = \psi(\text{cue}))$ | Restricted SDT on conditional familiarity |

### 3.5 From SDT to Unified Framework

**SDT's Structure:**
- **Two measures:** $\mu_{old}$, $\mu_{new}$ on familiarity space
- **Decision:** Likelihood ratio comparison

**Generalized Framework:**
- **Joint measures:** $\mu_{study}(f, \psi)$, $\mu_{test}(f, \psi)$ on content × context space
- **Transformations:** Push-forward, kernel, density change
- **Decision:** Measure divergence comparison

**Key Insight:** SDT provides the **simplest form** of measure comparison; all memory models extend this structure by:
1. Adding context dimension
2. Using richer transformations
3. Considering temporal dynamics

---

## 4. Three Measure Transformations in Memory

SDT's simple measure comparison (likelihood ratio) can be generalized to three fundamental **measure transformation types**. These transformations govern how the study-phase measure evolves during encoding, retrieval, and forgetting.

### 4.1 Push-Forward (Deterministic Context Change)

**Definition 4.1** (Push-Forward Transformation). Given a measurable map $T: \Omega \to \Omega'$ and a measure $\mu$ on $\Omega$, the **push-forward measure** $T_{\#}\mu$ on $\Omega'$ is defined as:

$$(T_{\#}\mu)(B) = \mu(T^{-1}(B))$$

for all measurable sets $B \subseteq \Omega'$.

**Psychological Interpretation:** Push-forward transformations represent **deterministic context evolution**—context drift, encoding mappings, or spatial transformations of representations.

**SDT Connection:** In SDT, familiarity distributions are static. Push-forward allows these distributions to **shift and evolve** over time.

**Memory Applications:**

1. **TCM (Temporal Context Model):**
   - Context drift: $\psi_{t+1} = T_t(\psi_t) = \rho\psi_t + \eta f_t$
   - Push-forward: $\mu_{t+1} = (T_t)_{\#}\mu_t + \delta_{(f_{t+1}, \psi_{t+1})}$
   - **SDT Analogue:** Old distribution shifts over time as context drifts

2. **CRU (Context Retrieval and Updating):**
   - Context as mixture: $\psi_t = \sum_{k<t} \alpha_{tk} f_k = T_t(\{f_j\}_{j<t})$
   - Push-forward: $\mu_t = (T_t)_{\#}\mu_{t-1} + \delta_{(f_t, T_t(\{f_j\}_{j<t}))}$
   - **SDT Analogue:** Distribution shape changes as context becomes weighted combination of items

3. **SIMPLE (Temporal Compression):**
   - Temporal log-transform: $T: t \mapsto \log(t)$
   - Push-forward: $\mu_{compressed} = (\log)_{\#}\mu_{temporal}$
   - **SDT Analogue:** Familiarity distribution rescaled via metric distortion

**Formal Connection to SDT:**

In SDT, old and new distributions are **fixed**. Push-forward allows the **old distribution to evolve**:

$$\mu_{old}(t) = (T_t)_{\#}\mu_{old}(0)$$

where $T_t$ represents context drift or transformation up to time $t$. Recognition then compares:

$$\text{Respond "old" if } \frac{d\mu_{old}(t)}{d\mu_{new}}(f) > c$$

### 4.2 Kernel Transformation (Probabilistic Retrieval)

**Definition 4.2** (Kernel Transformation). A **kernel transformation** maps a measure $\mu$ to a new measure $\nu$ via a transition kernel $K(x, \cdot)$:

$$\nu(A) = \int_{\Omega} K(x, A) \, d\mu(x)$$

where $K(x, \cdot)$ is a probability measure on $\Omega$ for each $x$.

**Psychological Interpretation:** Kernel transformations represent **stochastic retrieval processes**—probabilistic sampling from similarity distributions, retrieval noise, or context-dependent activation.

**SDT Connection:** SDT's familiarity distributions are **deterministic**. Kernel transformations allow **probabilistic retrieval**—each retrieval samples from a distribution over possible familiarity values.

**Memory Applications:**

1. **REM (Retrieving Effectively from Memory):**
   - Similarity-based sampling: $K_\sigma(\psi(\text{cue}), d\psi') = \mathcal{N}(\psi(\text{cue}), \sigma^2 I)(d\psi')$
   - Kernel transformation: $\nu = \int K_\sigma(\psi(\text{cue}), d\psi) \, d\mu_{study}(f, \psi)$
   - **SDT Analogue:** Familiarity computed as **expectation over samples** from similarity distribution

2. **EBRW (Exemplar-Based Random Walk):**
   - Similarity kernel: $K_s(f_i, df) = s(f_i, f) \, d\mu_{items}(f)$
   - Evidence accumulation: $\nu_n(df) = \sum_{m=1}^{n} K_s(f_{probe}, df)$
   - **SDT Analogue:** Familiarity accumulates stochastically via similarity-weighted sampling

3. **Global Matching Models:**
   - Global familiarity: $F = \int K(\text{probe}, df) \, d\mu_{study}(f, \psi)$
   - **SDT Analogue:** Familiarity is kernel-smoothed expectation over entire study measure

**Formal Connection to SDT:**

In SDT, familiarity is **deterministic** given the probe. Kernel transformation makes it **probabilistic**:

$$F \sim \int K(\text{probe}, df) \, d\mu_{old}(f)$$

Recognition decision becomes:

$$\text{Respond "old" if } \mathbb{E}[F] = \int f \cdot K(\text{probe}, df) \, d\mu_{old}(f) > \text{threshold}$$

As kernel bandwidth $\sigma^2 \to 0$, kernel becomes Dirac delta, recovering SDT's deterministic case.

### 4.3 Density Change (Attention / Decay)

**Definition 4.3** (Density Change / Radon–Nikodym Derivative). Given two measures $\mu$ and $\nu$ on $(\Omega, \mathcal{B})$ where $\nu \ll \mu$ (absolute continuity), the **Radon–Nikodym derivative** $w = \frac{d\nu}{d\mu}$ satisfies:

$$\nu(A) = \int_A w(x) \, d\mu(x)$$

**Psychological Interpretation:** Density changes represent **attentional weighting**, **rehearsal effects**, or **selective emphasis**—reweighting the importance of different parts of the measure.

**SDT Connection:** In SDT, old and new distributions have **fixed shapes**. Density changes allow distributions to **shift mass**—some items become more salient (higher density), others fade (lower density).

**Memory Applications:**

1. **SOB (Serial Order in a Box):**
   - Novelty-weighted encoding: $\gamma_t = n_t$ (novelty of item $t$)
   - Density change: $d\mu_{weighted}(f, \psi) = n(f, \psi) \cdot d\mu_{study}(f, \psi)$
   - **SDT Analogue:** Old distribution shape changes—novel items get higher density, repeated items get lower density

2. **Page & Norris Primacy Model:**
   - Primacy gradient: $\gamma_t = e^{-\lambda t}$
   - Density change: $d\mu_{primacy}(f, \psi) = e^{-\lambda t(f, \psi)} \cdot d\mu_{study}(f, \psi)$
   - **SDT Analogue:** Old distribution weighted by position—early items get higher density

3. **Trace Decay Models:**
   - Exponential decay: $d\mu_{decayed}(f, \psi) = e^{-\lambda(T-t)} \cdot d\mu_{study}(f, \psi)$
   - **SDT Analogue:** Old distribution **shrinks** (total mass decreases) over time

**Formal Connection to SDT:**

In SDT, old distribution $p_{old}(f)$ is **fixed**. Density change allows it to **evolve**:

$$p_{old}(f, t) = w(f, t) \cdot p_{old}(f, 0)$$

where $w(f, t)$ is the weight function. Recognition compares:

$$\text{Respond "old" if } \frac{w(f, t) \cdot p_{old}(f, 0)}{p_{new}(f)} > c$$

Total mass of old distribution: $\|\mu_{old}(t)\| = \int w(f, t) \, d\mu_{old}(f, 0)$ decreases if $w(f, t) < 1$ (decay).

### 4.4 Composition of Transformations

Memory processes often involve **compositions** of the three transformation types:

**Example 4.1** (TCM with Retrieval Noise). Push-forward (context drift) followed by kernel (stochastic retrieval):

$$\mu_{retrieval} = K_\sigma(\psi(\text{cue}), \cdot) \circ (T_T \circ \cdots \circ T_1)_{\#}\mu_0$$

**SDT Interpretation:** Old distribution evolves via context drift, then retrieval samples stochastically from this evolved distribution.

**Example 4.2** (Weighted Sampling). Density change (novelty weighting) followed by kernel (sampling):

$$d\mu_{sampled}(f, \psi) = K(\psi(\text{cue}), d\psi) \cdot w(f, \psi) \, d\mu_{study}(f, \psi)$$

**SDT Interpretation:** Old distribution weighted by novelty, then familiarity computed via kernel sampling.

### 4.5 Summary: Transformations and SDT

| Transformation Type | SDT Analogue | Memory Process | Representative Models |
|-------------------|--------------|----------------|---------------------|
| **Push-Forward** | Distribution shift | Context drift, encoding mapping | TCM, CRU, SIMPLE |
| **Kernel** | Probabilistic sampling | Stochastic retrieval | REM, EBRW, Global-matching |
| **Density Change** | Distribution reshaping | Attention, decay, weighting | SOB, Primacy, Trace decay |

**Key Insight:** SDT's simple measure comparison becomes a **rich algebra of transformations** when extended to joint content × context space.

---

## 5. Classical Models as Measure Transformations

This section shows how major memory models extend SDT's measure-comparison structure through different transformation types.

### 5.1 REM / EBRW: Kernel Transform on Measure

**REM (Retrieving Effectively from Memory):**

**Measure Structure:**
- Study measure: $\mu_{study}(df, d\psi) = \sum_{t=1}^{T} \gamma_t \delta_{f_t}(df) \delta_{\psi_t}(d\psi)$
- Retrieval kernel: $K_\sigma(\psi(\text{cue}), d\psi') = \mathcal{N}(\psi(\text{cue}), \sigma^2 I)(d\psi')$

**Transformation:**
- Kernel transformation: $\nu = \int K_\sigma(\psi(\text{cue}), d\psi) \, d\mu_{study}(f, \psi)$
- Familiarity: $F = \int \langle probe, f \rangle \, d\nu(f)$

**SDT Analogue:**
- Old distribution = study measure marginalized over context
- Retrieval samples stochastically via kernel: $F \sim \int K_\sigma(\psi(\text{cue}), d\psi) \, d\mu_{old}(f, \psi)$
- Recognition: Compare expectation $\mathbb{E}[F]$ against threshold

**Extension beyond SDT:**
- SDT: Familiarity is **deterministic** given probe
- REM: Familiarity is **probabilistic** (expectation over kernel samples)
- As $\sigma^2 \to 0$, kernel becomes Dirac delta → recovers SDT

**EBRW (Exemplar-Based Random Walk):**

**Measure Structure:**
- Study measure: $\mu_{study}(df) = \sum_{t=1}^{T} \delta_{f_t}(df)$ (item-only measure)
- Similarity kernel: $K_s(f_i, df) = s(f_i, f) \, d\mu_{study}(f)$

**Transformation:**
- Evidence accumulation: $\nu_n(df) = \sum_{m=1}^{n} K_s(f_{probe}, df)$
- Decision: Compare $\|\nu_n\|$ against threshold

**SDT Analogue:**
- Old distribution = $\mu_{study}$ on item space
- Familiarity accumulates via similarity-weighted sampling
- Recognition: Compare accumulated familiarity against criterion

**Extension beyond SDT:**
- SDT: Single familiarity value per probe
- EBRW: **Dynamic accumulation** of familiarity over time (RT model)

### 5.2 SIMPLE: Density Scaling in Temporal Metric

**SIMPLE (Scale-Invariant Memory, Perception, and Learning):**

**Measure Structure:**
- Study measure: $\mu_{study}(df, dt) = \sum_{t=1}^{T} \gamma_t \delta_{f_t}(df) \delta_{t}(dt)$ (item × time measure)
- Temporal metric: $d_\lambda(t_i, t_j) = e^{-\lambda|\log t_i - \log t_j|}$

**Transformation:**
- Density scaling: $d\mu_{compressed}(f, t) = d_\lambda(t_{probe}, t) \cdot d\mu_{study}(f, t)$
- Familiarity: $F = \int \langle probe, f \rangle \, d\mu_{compressed}(f, t)$

**SDT Analogue:**
- Old distribution: $p_{old}(f, t)$ on familiarity × time
- Temporal compression: Distribution rescaled by temporal distance metric
- Recognition: Compare compressed distribution against new distribution

**Extension beyond SDT:**
- SDT: Familiarity distributions are **static** (no temporal dimension)
- SIMPLE: Distributions **rescale** based on temporal distance
- Forgetting = reduction in distribution overlap due to temporal compression

### 5.3 TCM / CRU: Push-Forward of Measure Under Context Drift

**TCM (Temporal Context Model):**

**Measure Structure:**
- Initial measure: $\mu_0(df, d\psi)$
- Context evolution: $T_t(\psi) = \rho\psi + \eta f_t$

**Transformation:**
- Push-forward: $\mu_{t+1} = (T_t)_{\#}\mu_t + \delta_{(f_{t+1}, T_t(\psi_t))}$
- Final measure: $\mu_T = (T_T \circ \cdots \circ T_1)_{\#}\mu_0 + \sum_{t=1}^{T} \delta_{(f_t, \psi_t)}$

**SDT Analogue:**
- Old distribution: $p_{old}(f, \psi)$ on familiarity × context
- Context drift: Distribution shifts via push-forward: $p_{old}(f, \psi, t+1) = (T_t)_{\#}p_{old}(f, \psi, t)$
- Recognition: Compare evolved distribution against new distribution

**Extension beyond SDT:**
- SDT: Distributions are **static** (no context drift)
- TCM: Distributions **evolve** via deterministic push-forward
- Captures sequential dependencies and contiguity effects

**CRU (Context Retrieval and Updating):**

**Measure Structure:**
- Context as mixture: $\psi_t = \sum_{k<t} \alpha_{tk} f_k$
- Defines linear transformation: $T_t: \mathcal{F}^{t-1} \to \mathcal{C}$

**Transformation:**
- Push-forward: $\mu_t = (T_t)_{\#}\mu_{t-1} + \delta_{(f_t, T_t(\{f_j\}_{j<t}))}$

**SDT Analogue:**
- Old distribution shape changes as context becomes weighted combination of items
- Distribution evolution: $p_{old}(f, \psi, t) = (T_t)_{\#}p_{old}(f, \psi, t-1)$

**Extension beyond SDT:**
- SDT: Distributions have **fixed shape**
- CRU: Distributions **reshape** as context updates

### 5.4 SAM / Associative Models: Direct Self-Associative Operator

**SAM (Search of Associative Memory):**

**Measure Structure:**
- Self-associative measure: $\mu_{assoc}(df_i, df_j) = \sum_{t} \gamma_t \delta_{f_t \otimes f_t}(df_i, df_j)$
- Item-item measure on product space $\mathcal{F} \times \mathcal{F}$

**Transformation:**
- Direct associative retrieval: $F = \int \langle probe, f_i \rangle \langle probe, f_j \rangle \, d\mu_{assoc}(f_i, f_j)$

**SDT Analogue:**
- Old distribution: $p_{old}(f_i, f_j)$ on item-item space
- Familiarity: Self-associative strength (diagonal of distribution)
- Recognition: Compare associative strength against threshold

**Extension beyond SDT:**
- SDT: Unidimensional familiarity
- SAM: **Bidimensional** familiarity (item × item associations)

### 5.5 Connectionist / SOB: Recurrent Push-Forward with Feedback Kernel

**SOB (Serial Order in a Box):**

**Measure Structure:**
- Study measure: $\mu_{study}(df, d\psi) = \sum_{t=1}^{T} n_t \delta_{f_t}(df) \delta_{\psi_t}(d\psi)$
- Novelty weights: $\gamma_t = n_t$ (novelty of item $t$)

**Transformation:**
- Density change: $d\mu_{weighted}(f, \psi) = n(f, \psi) \cdot d\mu_{study}(f, \psi)$
- Context evolution: $\psi_{t+1} = T_t(\psi_t, f_t)$ (feedback)
- Push-forward: $\mu_{t+1} = (T_t)_{\#}\mu_t + n_{t+1} \delta_{(f_{t+1}, \psi_{t+1})}$

**SDT Analogue:**
- Old distribution: $p_{old}(f, \psi)$ weighted by novelty
- Distribution shape changes as context updates with feedback
- Recognition: Compare novelty-weighted distribution against new

**Extension beyond SDT:**
- SDT: Distributions have **fixed weights**
- SOB: Distributions **reweight** based on novelty
- Captures similarity effects and serial position curves

### 5.6 Summary Table: Models as SDT Extensions

| Model Family | Transformation Type | SDT Analogue | Extension |
|-------------|-------------------|--------------|-----------|
| **REM / EBRW** | Kernel transform on $\mu$ | Probabilistic likelihood comparison | Stochastic sampling, RT accumulation |
| **SIMPLE** | Density scaling in temporal metric | Variance rescaling of SDT distributions | Temporal compression, scale invariance |
| **TCM / CRU** | Push-forward of $\mu$ under context drift | Shift of old distribution in context dimension | Sequential dependencies, contiguity |
| **SAM** | Direct self-associative operator | Measure on item-item manifold | Bidimensional associations |
| **SOB / Connectionist** | Recurrent push-forward with feedback kernel | Time-evolving SDT manifold | Novelty weighting, similarity effects |

**Key Insight:** All models extend SDT's measure-comparison structure by:
1. Adding context dimension (joint measures)
2. Using richer transformations (push-forward, kernel, density change)
3. Considering temporal dynamics (measure evolution)

---

## 6. From Recognition to Recall: Conditional Measure Restriction

### 6.1 Recognition: Global Measure Comparison

**SDT's Recognition:**

In SDT, recognition compares two **marginal measures**:

$$\text{Respond "old" if } \frac{d\mu_{old}}{d\mu_{new}}(f) > c$$

where $f$ is familiarity computed from the probe, and measures are **marginalized over all contexts**.

**Generalized Recognition:**

With joint measures $\mu_{study}(f, \psi)$ and $\mu_{test}(f, \psi)$, recognition compares:

$$\text{Respond "old" if } \frac{\int_{\mathcal{C}} d\mu_{study}(f, \psi)}{\int_{\mathcal{C}} d\mu_{new}(f, \psi)} > c$$

This integrates over **all possible contexts** $\psi \in \mathcal{C}$.

### 6.2 Recall: Conditional Measure Restriction

**Definition 6.1** (Conditional Measure). Given a joint measure $\mu$ on $\Omega_{\mathcal{F}} \times \Omega_{\mathcal{C}}$ and a specific context value $\psi(\text{cue}) \in \Omega_{\mathcal{C}}$, the **conditional measure** $\mu(\cdot \mid \psi = \psi(\text{cue}))$ on $\Omega_{\mathcal{F}}$ is defined as:

$$\mu(A \mid \psi = \psi(\text{cue})) = \frac{\mu(A \times \{\psi(\text{cue})\})}{\mu_{\mathcal{C}}(\{\psi(\text{cue})\})}$$

where $\mu_{\mathcal{C}}$ is the context marginal.

**Recall Decision:**

Recall operates on the **conditional measure** given the cue context:

$$\text{Recall item $i$ if } \int_{\mathcal{F}} \langle f_i, f \rangle \, d\mu_{study}(f \mid \psi = \psi(\text{cue})) > \text{threshold}$$

This restricts to **only items associated with context $\psi(\text{cue})$**.

### 6.3 Recall as Restricted SDT

**Theorem 6.1** (Recall as Conditional SDT). Recall is a **restricted SDT** where the decision is made on the conditional measure instead of the marginal one.

**Formal Statement:**

**Recognition (SDT):**
$$\text{Respond "old" if } \frac{d\mu_{old}}{d\mu_{new}}(f) > c$$
where $\mu_{old}(df) = \int_{\mathcal{C}} d\mu_{study}(f, \psi)$ (marginal over all contexts).

**Recall:**
$$\text{Recall item $i$ if } \frac{d\mu_{study}(\cdot \mid \psi(\text{cue}))}{d\mu_{new}(\cdot \mid \psi(\text{cue}))}(f_i) > c$$
where $\mu_{study}(\cdot \mid \psi(\text{cue}))$ is conditional on specific context.

**Proof:**

Recognition integrates over all contexts:
$$\mu_{old}(df) = \int_{\mathcal{C}} d\mu_{study}(f, \psi)$$

Recall conditions on specific context:
$$\mu_{study}(df \mid \psi(\text{cue})) = \frac{\mu_{study}(df \times \{\psi(\text{cue})\})}{\mu_{\mathcal{C}}(\{\psi(\text{cue})\})}$$

If $\mu_{\mathcal{C}}(\{\psi(\text{cue})\}) > 0$, then:
$$\mu_{study}(df \mid \psi(\text{cue})) = \lim_{\sigma \to 0} \frac{\int K_\sigma(\psi(\text{cue}), d\psi) \, d\mu_{study}(f, \psi)}{\int K_\sigma(\psi(\text{cue}), d\psi) \, d\mu_{\mathcal{C}}(\psi)}$$

where $K_\sigma(\psi(\text{cue}), \cdot)$ is a kernel with bandwidth $\sigma^2$.

As $\sigma^2 \to 0$, the kernel approaches Dirac delta, and:
$$\mu_{study}(df \mid \psi(\text{cue})) = \frac{\delta_{\psi(\text{cue})} \circ \mu_{study}(df)}{\mu_{\mathcal{C}}(\{\psi(\text{cue})\})}$$

Recognition uses marginal measure; recall uses conditional measure. QED.

### 6.4 Kernel Bandwidth and Contextual Resolution

**Definition 6.2** (Kernel Bandwidth). The **kernel bandwidth** $\sigma^2$ controls the **contextual resolution** of retrieval:

- **Large $\sigma^2$ (broad kernel):** Low resolution, many contexts contribute → **recognition**
- **Small $\sigma^2$ (narrow kernel):** High resolution, few contexts contribute → **recall**
- **$\sigma^2 \to 0$ (Dirac kernel):** Perfect resolution, single context → **pure recall**

**Kernel-Based Retrieval:**

$$\text{Activation}(i|\text{cue}) = \int_{\mathcal{F} \times \mathcal{C}} \langle f_i, f \rangle K_\sigma(\psi(\text{cue}), d\psi) \, d\mu_{study}(f, \psi)$$

**Limit Behavior:**

As $\sigma^2 \to 0$:
$$\lim_{\sigma \to 0} \int K_\sigma(\psi(\text{cue}), d\psi) \, d\mu_{study}(f, \psi) = \int_{\mathcal{F}} \langle f_i, f \rangle \, d\mu_{study}(f \mid \psi(\text{cue}))$$

which is exactly recall activation.

**SDT Curve Dependence on Bandwidth:**

The SDT curve (ROC curve) depends on contextual resolution:

- **Recognition ($\sigma^2 > 0$):** Broad kernel → many items contribute → high hit rate but high false alarm rate
- **Recall ($\sigma^2 \to 0$):** Narrow kernel → few items contribute → lower hit rate but lower false alarm rate

### 6.5 Recognition–Recall Continuum

**Proposition 6.1** (Recognition–Recall Continuum). Recognition and recall are **the same operation** at different kernel bandwidths:

$$\text{Recognition}(\sigma^2 > 0) \to \text{Recall}(\sigma^2 \to 0)$$

**Formal Statement:**

$$\text{Activation}(i|\text{cue}, \sigma^2) = \int_{\mathcal{F} \times \mathcal{C}} \langle f_i, f \rangle K_\sigma(\psi(\text{cue}), d\psi) \, d\mu_{study}(f, \psi)$$

is a **continuous function** of $\sigma^2$:

- At $\sigma^2 = \infty$: Uniform kernel → pure item-based recognition (no context)
- At $\sigma^2 > 0$: Broad kernel → context-mediated recognition
- At $\sigma^2 \to 0$: Dirac kernel → pure recall (context-specific)

**Empirical Prediction:**

Tasks requiring **precise context matching** (recall) should show:
- Lower hit rates (fewer items match narrow context)
- Lower false alarm rates (fewer distractors match narrow context)
- Higher precision (items that match are more likely correct)

**Tasks requiring broad matching** (recognition) should show:
- Higher hit rates (more items match broad context)
- Higher false alarm rates (more distractors match broad context)
- Lower precision (matches are less selective)

---

## 7. Forgetting as Measure Divergence

### 7.1 Forgetting: Increasing Divergence Between Measures

**Core Principle:** Forgetting arises from **increasing divergence** between study-phase and test-phase measures.

**Definition 7.1** (Measure Divergence). Given two measures $\mu_{study}$ and $\mu_{test}$ on the same measurable space, **forgetting** can be quantified as:

$$\text{Forgetting}(\Delta t) = D(\mu_{study}, \mu_{test}(\Delta t))$$

where $D$ is a divergence measure (e.g., KL divergence, total variation, Wasserstein distance) and $\Delta t = t_{test} - t_{study}$.

**SDT Connection:**

In SDT, forgetting manifests as:
- **Shift** of old distribution (trace decay)
- **Compression** of old distribution (distinctiveness loss)
- **Overlap** between old and new distributions (interference)

All of these can be quantified as **divergence measures**.

### 7.2 Forms of Forgetting as Specific Transformations

#### 7.2.1 Trace Decay: Scaling of Measure Mass

**Mathematical Form:**
$$\mu_{decayed}(\Delta t)(A) = e^{-\lambda \Delta t} \mu_{study}(A)$$

**Divergence:**
$$D(\mu_{study}, \mu_{decayed}(\Delta t)) = |1 - e^{-\lambda \Delta t}| \cdot \|\mu_{study}\|$$

**SDT Analogue:**
- Old distribution **shrinks** (total mass decreases)
- Likelihood ratio $\frac{p_{old}(f, \Delta t)}{p_{new}(f)} = e^{-\lambda \Delta t} \cdot \frac{p_{old}(f, 0)}{p_{new}(f)}$ decreases
- Recognition accuracy decreases as $\Delta t$ increases

**Empirical Forgetting Function:**
$$F(\Delta t) = e^{-\lambda \Delta t}$$

Exponential decay of memory strength.

#### 7.2.2 Interference: Non-Orthogonality of Supports

**Mathematical Form:**

Forgetting via interference occurs when:
$$\text{support}(\mu_{study}) \cap \text{support}(\mu_{competitors}) \neq \emptyset$$

**Divergence:**

Total variation distance:
$$D(\mu_{study}, \mu_{test}) = \|\mu_{study} - \mu_{test}\|_{\text{TV}} = \sup_{A} |\mu_{study}(A) - \mu_{test}(A)|$$

where $\mu_{test}$ includes competitors from new lists.

**SDT Analogue:**
- Old distribution **overlaps** with competitor distributions
- Likelihood ratio decreases due to overlap: $\frac{p_{old}(f)}{p_{new}(f)} \approx \frac{p_{old}(f)}{p_{old}(f) + p_{competitors}(f)}$
- Recognition accuracy decreases as overlap increases

**Empirical Forgetting Function:**
$$F(\Delta t) = \frac{\|\mu_{study}\|}{\|\mu_{study}\| + \|\mu_{competitors}(\Delta t)\|}$$

Forgetting rate depends on amount of interference.

#### 7.2.3 Distinctiveness Loss: Compression of Metric → Density Diffusion

**Mathematical Form:**

Temporal compression (SIMPLE-type):
$$d\mu_{compressed}(f, t) = d_\lambda(t_{probe}, t) \cdot d\mu_{study}(f, t)$$

where $d_\lambda(t_i, t_j) = e^{-\lambda|\log t_i - \log t_j|}$ is temporal distance metric.

**Divergence:**

Wasserstein distance:
$$D(\mu_{study}, \mu_{compressed}) = \inf_{\gamma} \int c(f, f') \, d\gamma(f, f')$$

where $c$ is transport cost (e.g., $c(f, f') = \|f - f'\|^2$).

**SDT Analogue:**
- Old distribution **compresses** in temporal dimension
- Distributions become less discriminable (density diffuses)
- Recognition accuracy decreases as temporal distance increases

**Empirical Forgetting Function:**
$$F(\Delta t) = \left(1 + \frac{\Delta t}{t_0}\right)^{-\alpha}$$

Power-law forgetting (SIMPLE prediction).

#### 7.2.4 Context Drift: Push-Forward Divergence

**Mathematical Form:**

Context evolution (TCM-type):
$$\mu_{test}(\Delta t) = (T_{\Delta t})_{\#}\mu_{study}$$

where $T_{\Delta t}(\psi) = \rho^{\Delta t}\psi + \eta \sum_{k=1}^{\Delta t} \rho^{\Delta t - k} f_k$ represents context drift.

**Divergence:**

KL divergence:
$$D(\mu_{study}, \mu_{test}(\Delta t)) = \text{KL}(\mu_{study} \| \mu_{test}(\Delta t)) = \int \log\left(\frac{d\mu_{study}}{d\mu_{test}(\Delta t)}\right) \, d\mu_{study}$$

**SDT Analogue:**
- Old distribution **shifts** in context dimension
- Distribution shape changes via push-forward
- Recognition accuracy decreases as context drift increases

**Empirical Forgetting Function:**
$$F(\Delta t) = \rho^{\Delta t} + \eta \sum_{k=1}^{\Delta t} \rho^{\Delta t - k} \langle f_{study}, f_k \rangle$$

Forgetting rate depends on drift parameter $\rho$.

### 7.3 Unified Forgetting Framework

**Theorem 7.1** (Unified Forgetting Principle). All forms of forgetting arise from **measure divergence** $D(\mu_{study}, \mu_{test}(\Delta t))$, where different forgetting mechanisms correspond to different **divergence metrics** and **transformation types**.

**Formal Statement:**

1. **Trace Decay:** $D = \text{total variation}$, transformation = density scaling
2. **Interference:** $D = \text{total variation}$, transformation = measure overlap
3. **Distinctiveness Loss:** $D = \text{Wasserstein distance}$, transformation = metric compression
4. **Context Drift:** $D = \text{KL divergence}$, transformation = push-forward

All forgetting functions $F(\Delta t)$ can be expressed as:

$$F(\Delta t) = 1 - \frac{D(\mu_{study}, \mu_{test}(\Delta t))}{\|\mu_{study}\|}$$

**SDT Connection:**

In SDT, forgetting manifests as changes in the **old distribution**:
- Shift: $p_{old}(f, \Delta t) = p_{old}(f - \delta(\Delta t), 0)$
- Compression: $p_{old}(f, \Delta t) = \frac{1}{\sigma(\Delta t)} p_{old}(\frac{f}{\sigma(\Delta t)}, 0)$
- Mass reduction: $\|\mu_{old}(\Delta t)\| = e^{-\lambda \Delta t} \|\mu_{old}(0)\|$

All can be quantified via divergence: $D(\mu_{old}(0), \mu_{old}(\Delta t))$.

### 7.4 Empirical Forgetting Functions

**Proposition 7.1** (Forgetting Function Forms). Different forgetting mechanisms produce different forgetting function forms:

1. **Exponential:** $F(\Delta t) = e^{-\lambda \Delta t}$ (trace decay, exponential interference)
2. **Power-law:** $F(\Delta t) = (1 + \frac{\Delta t}{t_0})^{-\alpha}$ (distinctiveness loss, SIMPLE)
3. **Context-dependent:** $F(\Delta t) = \rho^{\Delta t} + \eta \sum_{k} \rho^{\Delta t - k} \langle f_{study}, f_k \rangle$ (context drift, TCM)
4. **Hyperbolic:** $F(\Delta t) = \frac{1}{1 + \lambda \Delta t}$ (interference-based)

All emerge as different parameterizations of **measure divergence** over time.

**SDT Prediction:**

Forgetting curves in recognition tasks should follow these forms, with parameters depending on:
- Transformation type (decay, drift, compression, interference)
- Measure structure (separable, joint, probabilistic)
- Task demands (recognition vs. recall)

---

## 8. General Theorem: SDT as the Limit Case of the Unified Operator

### 8.1 The Unified Operator Equation

From the Unified Operator framework, all memory models can be expressed as:

$$W = \sum_{t=1}^{T}\gamma_t f_t \otimes \psi_t, \quad a(i|\text{cue}) = f_i^\top W\psi(\text{cue})$$

This operator defines a **discrete measure** on the product space:

$$\mu_{study}(A \times B) = \sum_{t=1}^{T} \gamma_t \mathbb{1}_A(f_t) \mathbb{1}_B(\psi_t)$$

### 8.2 Main Theorem: SDT as Limit Case

**Theorem 8.1** (SDT as Limit of Unified Operator). When:

1. Context manifold collapses to a single dimension: $\dim(\Omega_{\mathcal{C}}) = 1$
2. Retrieval kernel is Gaussian with fixed bandwidth: $K_\sigma(\psi(\text{cue}), \cdot) = \mathcal{N}(\psi(\text{cue}), \sigma^2)$
3. Measures are separable: $\mu_{study}(df, d\psi) = \mu_{\mathcal{F}}(df) \otimes \mu_{\mathcal{C}}(d\psi)$

Then the unified operator retrieval:

$$a(i|\text{cue}) = f_i^\top W\psi(\text{cue}) = \int_{\mathcal{F} \times \mathcal{C}} \langle f_i, f \rangle K_\sigma(\psi(\text{cue}), d\psi) \, d\mu_{study}(f, \psi)$$

reduces to SDT's likelihood ratio test:

$$\text{Respond "old" if } \frac{d\mu_{old}}{d\mu_{new}}(f_i) > c$$

where $\mu_{old}(df) = \int_{\mathcal{C}} d\mu_{study}(f, \psi)$ and $\mu_{new}(df)$ is the new-item measure.

**Proof:**

**Step 1: Unified Operator as Measure Integral**

From the operator equation:
$$a(i|\text{cue}) = f_i^\top W\psi(\text{cue}) = \sum_{t=1}^{T} \gamma_t \langle f_i, f_t \rangle \langle \psi(\text{cue}), \psi_t \rangle$$

This can be written as:
$$a(i|\text{cue}) = \int_{\mathcal{F} \times \mathcal{C}} \langle f_i, f \rangle \langle \psi(\text{cue}), \psi \rangle \, d\mu_{study}(f, \psi)$$

**Step 2: Kernel Transformation**

With retrieval kernel $K_\sigma(\psi(\text{cue}), \cdot)$:
$$a(i|\text{cue}) = \int_{\mathcal{F} \times \mathcal{C}} \langle f_i, f \rangle K_\sigma(\psi(\text{cue}), d\psi) \, d\mu_{study}(f, \psi)$$

**Step 3: Context Collapse**

As context dimension collapses ($\dim(\Omega_{\mathcal{C}}) \to 1$) and kernel bandwidth becomes large ($\sigma^2 \to \infty$), kernel becomes uniform:

$$\lim_{\sigma \to \infty} K_\sigma(\psi(\text{cue}), d\psi) = \frac{1}{\|\Omega_{\mathcal{C}}\|} d\psi$$

Then:
$$a(i|\text{cue}) \to \int_{\mathcal{F}} \langle f_i, f \rangle \, d\mu_{\mathcal{F}}(f)$$

where $\mu_{\mathcal{F}}(df) = \int_{\mathcal{C}} d\mu_{study}(f, \psi)$ is the marginal measure.

**Step 4: SDT Likelihood Ratio**

For recognition, compare $a(i|\text{probe})$ for studied vs. unstudied items:

$$\frac{a(i|\text{probe, old})}{a(i|\text{probe, new})} = \frac{\int_{\mathcal{F}} \langle probe, f \rangle \, d\mu_{old}(f)}{\int_{\mathcal{F}} \langle probe, f \rangle \, d\mu_{new}(f)}$$

If item vectors $\{f_t\}$ are normalized and probe = item $i$, then:

$$\frac{a(i|\text{probe, old})}{a(i|\text{probe, new})} = \frac{\frac{d\mu_{old}}{df}(f_i)}{\frac{d\mu_{new}}{df}(f_i)} = \frac{d\mu_{old}}{d\mu_{new}}(f_i)$$

**Step 5: Decision Rule**

Respond "old" if:
$$\frac{d\mu_{old}}{d\mu_{new}}(f_i) > c$$

which is exactly SDT's likelihood ratio test. QED.

### 8.3 Corollaries

**Corollary 8.1** (SDT as Marginal Projection). SDT is the **marginal projection** of the unified operator framework when context is marginalized.

**Corollary 8.2** (Recognition–Recall Continuum). Recognition and recall are the same operation at different kernel bandwidths:
- **Recognition:** $\sigma^2 > 0$ (broad kernel, marginal measure)
- **Recall:** $\sigma^2 \to 0$ (narrow kernel, conditional measure)

**Corollary 8.3** (Model Hierarchy). All memory models form a hierarchy from SDT:
- **Level 0:** SDT (1D marginal, static measures)
- **Level 1:** Models with context dimension (joint measures)
- **Level 2:** Models with transformations (push-forward, kernel, density change)
- **Level 3:** Models with temporal dynamics (measure evolution)

**Corollary 8.4** (Theoretical Integration). SDT, recognition models (REM, EBRW), and recall models (TCM, CRU) are all **special cases** of the unified operator framework, differing only in:
- Context dimensionality
- Transformation type
- Kernel bandwidth

---

## 9. Discussion and Implications

### 9.1 Continuous Hierarchy of Measure Transformations

**Key Insight:** SDT and all modern memory models form a **continuous hierarchy** of measure transformations:

1. **SDT (Foundation):** Compare two probability measures on 1D familiarity space
2. **Recognition Models (REM, EBRW):** Kernel transformations on joint measures
3. **Temporal Models (TCM, CRU):** Push-forward transformations on evolving measures
4. **Attention Models (SOB, Primacy):** Density changes on weighted measures
5. **Full Unified Framework:** Composition of all transformation types

**Geometric Foundation:**

Recognition, recall, forgetting, and context drift are different **directions of measure deformation** in the same space:
- **Recognition:** Measure comparison along familiarity axis
- **Recall:** Conditional measure restriction along context axis
- **Forgetting:** Measure divergence over time
- **Context Drift:** Measure push-forward in context space

### 9.2 Experimental Paradigms as Measure Transformations

**Implication:** Experimental paradigms manipulate **transformations of $\mu$**, not separate "processes."

**Examples:**

1. **Recognition Task:** Compare $\mu_{study}$ vs. $\mu_{new}$ (marginal measures)
2. **Cued Recall:** Conditional measure $\mu_{study}(\cdot \mid \psi(\text{cue}))$
3. **Free Recall:** Sequential sampling from conditional measures
4. **Forgetting Paradigm:** Measure divergence $D(\mu_{study}, \mu_{test}(\Delta t))$
5. **Interference Paradigm:** Measure overlap $\text{support}(\mu_{study}) \cap \text{support}(\mu_{competitors})$

**Unified Prediction:**

All paradigms are **measure comparisons** with different:
- **Dimensions:** Familiarity (1D) vs. content × context (2D+)
- **Kernel bandwidths:** Recognition (broad) vs. recall (narrow)
- **Transformation types:** Push-forward, kernel, density change

### 9.3 Bridge to Perception, Decision Theory, and Bayesian Inference

**Perception as Measure Transformation:**

Perception = transport map from physical to psychological space:
$$\mu_{psychological} = T_{\#}\mu_{physical}$$

**Decision Theory as Measure Comparison:**

Decision = comparison of expected utility measures:
$$\text{Choose action $a$ if } \int U(x) \, d\mu_a(x) > \int U(x) \, d\mu_b(x)$$

**Bayesian Inference as Conditional Measure:**

Posterior = conditional measure given data:
$$\mu(\theta \mid \text{data}) = \frac{\mu(\text{data} \mid \theta) \cdot \mu(\theta)}{\int \mu(\text{data} \mid \theta) \, d\mu(\theta)}$$

**Unified Framework:**

All cognitive processes involve **measure transformations**:
- **Perception:** Push-forward from physical to psychological
- **Memory:** Transformations within psychological space
- **Decision:** Comparison of transformed measures
- **Inference:** Conditional measures given evidence

### 9.4 Theoretical Integration

**Connection to Unified Operator Framework:**

The measure-theoretic framework from SDT **complements** the Unified Operator framework:
- **Unified Operator:** Algebraic structure (operators, compositions)
- **Measure Theory:** Probabilistic structure (measures, transformations)

Together, they provide:
1. **Algebraic foundation:** How memory processes compose (operators)
2. **Probabilistic foundation:** How memory states evolve (measures)

**Connection to Existing Models:**

All major memory models can be expressed as:
1. **Measure construction:** How study measure $\mu_{study}$ is formed
2. **Transformation type:** Push-forward, kernel, or density change
3. **Decision rule:** How transformed measure is compared

### 9.5 Empirical Predictions

**Prediction 1: Kernel Bandwidth Hypothesis**

Recognition–recall differences should correlate with contextual precision (kernel bandwidth $\sigma^2$):
- **High $\sigma^2$:** Recognition-like behavior (broad matching)
- **Low $\sigma^2$:** Recall-like behavior (narrow matching)

**Prediction 2: Measure Divergence Hypothesis**

Forgetting rate should correlate with measure divergence $D(\mu_{study}, \mu_{test}(\Delta t))$:
- **Exponential decay:** $D = \text{total variation}$ (trace decay)
- **Power-law decay:** $D = \text{Wasserstein distance}$ (distinctiveness loss)
- **Context drift:** $D = \text{KL divergence}$ (TCM-type)

**Prediction 3: Transformation Type Hypothesis**

Different forgetting mechanisms (decay, drift, interference) should produce different forgetting function forms but same underlying **measure misalignment**.

**Prediction 4: Model Hierarchy Hypothesis**

Models should transition between levels as task demands change:
- **SDT level:** Simple recognition (1D familiarity)
- **Recognition level:** Context-mediated recognition (2D content × context)
- **Recall level:** Conditional retrieval (narrow kernel bandwidth)

---

## 10. Conclusion

### 10.1 Memory Judgments as Measure Comparisons

**Central Claim:** Memory judgments = measure comparisons across representational manifolds.

**SDT Foundation:** SDT provides the **simplest measure-comparison form**—comparing two probability measures on 1D familiarity space.

**General Framework:** The Unified Operator extends SDT into a **general algebra of measure transformation**:
- Joint measures over content × context space
- Three transformation types: push-forward, kernel, density change
- Temporal dynamics via measure evolution

### 10.2 Geometry of Measure Transformations

**Key Insight:** Memory can be defined not by its mechanisms, but by the **geometry of its measure transformations**.

**Geometric Structure:**
- **Recognition:** Measure comparison along familiarity axis
- **Recall:** Conditional measure restriction along context axis
- **Forgetting:** Measure divergence over time
- **Context Drift:** Measure push-forward in context space

**Unified Perspective:** All memory processes are **different directions of measure deformation** in the same space.

### 10.3 Theoretical Contributions

1. **Unification:** SDT and all memory models are special cases of measure-transformation framework
2. **Generativity:** Framework enables construction of new models by combining transformation types
3. **Clarity:** Separates what memory models do (transform measures) from how they do it (specific mechanisms)
4. **Integration:** Links memory to perception, decision theory, and Bayesian inference

### 10.4 Future Directions

1. **Optimal Transport:** Binding as optimal transport between marginal measures
2. **Information Geometry:** Forgetting as entropy increase under measure diffusion
3. **Category Theory:** Memory processes as morphisms in category of measurable spaces
4. **Differential Geometry:** Context evolution as flows on manifolds

### 10.5 Final Statement

**SDT → Unified Framework:**

SDT's simple but powerful structure—**comparing two probability measures**—provides the foundation for a complete theory of memory. By extending SDT's measure-comparison structure to higher-dimensional spaces and richer transformations, we reveal that all memory processes (encoding, retrieval, forgetting, generalization) are **measure transformations** between content and context spaces.

Memory is not defined by its mechanisms, but by the **geometry of its measure transformations**.

---

## References

[To be added: citations to SDT (Green & Swets, 1966; Macmillan & Creelman, 2005), TCM, REM, SIMPLE, CRU, and related measure-theoretic and optimal transport literature]

---

**Key Notation Summary:**

- $\mu_{old}$, $\mu_{new}$: SDT's old and new probability measures
- $\mu_{study}$, $\mu_{test}$: Joint measures on content × context space
- $K_\sigma(\psi, \cdot)$: Retrieval kernel with bandwidth $\sigma^2$
- $T_{\#}\mu$: Push-forward of measure $\mu$ via map $T$
- $\frac{d\nu}{d\mu}$: Radon–Nikodym derivative (density change)
- $D(\mu, \nu)$: Measure divergence (KL, total variation, Wasserstein)
- $\mu(\cdot \mid \psi)$: Conditional measure given context $\psi$


