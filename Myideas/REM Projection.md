**Title:** A Projection-Based Interpretation of the Environmental Base Rate in REM

---

### 1. Conceptual Overview

The **Retrieving Effectively from Memory (REM)** model traditionally assumes that each feature of an item is encoded with a probability determined by a geometric distribution, and that the likelihood of a match during retrieval depends on how diagnostic that feature is within the environment. The _environmental base rate_ $P_{env}(f)$ represents the prior probability of observing a given feature value in the world. Recognition strength is computed as a likelihood ratio comparing the probability of the probe given the stored traces to the probability of the probe given the environment.

In the **projection-based reinterpretation**, the environmental base rate is not an external property of the environment per se but a **projection (pushforward)** of the long-term memory (LTM) representational manifold onto the observable feature space. This means that the uneven distribution of features in perception (the 'environmental folds') reflects the internal semantic and phonological structure of memory itself. Familiarity judgments thus operate as Bayesian inference over this projected field rather than as direct feature overlap comparisons.

---

### 2. Mathematical Framework

Let $P_{LTM}(x)$ denote the probability density over long-term semantic representations $x \in \mathcal{M}_{LTM}$. A mapping $\Phi: \mathcal{M}_{LTM} \to \mathcal{F}$ projects these latent representations into the observable feature space $\mathcal{F}$, generating the environmental base rate:

$$  
P_{env}(f) = \Phi_{\#} P_{LTM}(f) = \int_{\mathcal{M}_{LTM}} p(f|x) P_{LTM}(x) , dx.  
$$

Each stored memory trace is represented by features $f_i \sim p(f|x_i)$. During retrieval, the familiarity of a probe $f_p$ is computed as:

$$  
\Lambda(f_p) = \sum_i \frac{p(f_p | x_i)}{P_{env}(f_p)}.  
$$

This contrasts with a **direct-coding model**, where familiarity is based purely on feature overlap:

$$  
\Lambda_{direct}(f_p) = \sum_i p(f_p | x_i).  
$$

Both formulations are implemented within the same REM architecture; the only difference lies in whether the normalization by $P_{env}(f)$ is applied.

---

### 3. Theoretical Implications

1. **Diagnosticity Encoding:** The normalization by $1/P_{env}(f)$ means that rare (low-probability) feature combinations contribute more strongly to familiarity. This aligns with observed _mirror effects_, where rare or distinctive items show both higher hit rates and lower false alarms.
    
2. **Semantic Projection:** Because $P_{env}(f)$ is generated from $P_{LTM}(x)$, the base-rate structure implicitly carries information about semantic and phonological organization. Thus, semantic clusters in LTM create corresponding 'folds' in the perceptual probability field.
    
3. **Unified Framework:** Both direct semantic encoding and probabilistic projection can be seen as two levels of the same process: the first operating within $\mathcal{M}_{LTM}$ (semantic manifold), the second on its pushforward distribution $\Phi_{#}P_{LTM}$ in $\mathcal{F}$.
    

---

### 4. Model Comparison

**Direct-Coding Model:**  
$$  
F_{direct}(i) = \beta_0 + \beta_1 e^{-d_i^2/\sigma^2},  
$$  
where $d_i$ is semantic distance between probe and stored item.

**Projection-Based Model:**  
$$  
F_{push}(i) = \beta_0 + \beta_1 \frac{e^{-d_i^2/\sigma^2}}{P_{env}(f_i)}.  
$$

Both models share identical parameters and structure; only the normalization term differs. The projection model predicts asymmetric familiarity distributions and sensitivity to both semantic similarity and base-rate rarity, while the direct model predicts linear dependence on similarity alone.

Model comparison can be performed via likelihood-based fitting or information criteria (AIC/BIC). If normalization significantly improves fits to behavioral data (e.g., DRM false-memory ROCs), it supports the projection hypothesis.

---

### 5. Empirical Testing with Existing Data

Existing Deese–Roediger–McDermott (DRM) datasets already provide sufficient structure to test the two formulations because they include:

- **Semantic relatedness** (associative norms between studied items and lures),
    
- **Word frequency measures** (proxy for $P_{env}(f)$), and
    
- **Hit/false-alarm rates** across conditions.
    

Using these datasets, both models can be fitted to the same data. The projection model predicts that semantic clustering and word frequency will jointly influence familiarity, reproducing mirror effects without additional assumptions.

---

### 6. Predictions and Interpretation

|Prediction|Direct-Coding|Projection-Based|
|---|---|---|
|Familiarity increases with semantic similarity|Yes|Yes|
|Familiarity modulated by environmental frequency|No|Yes|
|Mirror effect (high hit & low FA for rare items)|No|Yes|
|Nonlinear dependence on similarity|Weak|Strong|

If the projection model outperforms the direct model, this implies that what REM calls the _environmental base rate_ is actually the probabilistic shadow of LTM structure rather than an independent environmental prior.

---

### 7. Broader Implications

This reinterpretation bridges REM with models of semantic organization and probabilistic inference. It suggests that recognition operates not by comparing items in a purely feature-based space, but by inferring how a probe fits into a probability field shaped by the mind’s own representational geometry. It provides a unified view where _semantic memory projects onto episodic encoding_, producing the apparent environmental regularities that REM leverages during retrieval.

---

### 8. Next Steps

1. Implement both retrieval operators within the existing REM code.
    
2. Fit them to open DRM datasets (e.g., Malmberg et al.).
    
3. Compare model fits via ROC and mirror-effect metrics.
    
4. If successful, extend the model to continuous or high-dimensional embeddings (e.g., word2vec spaces) to quantify $P_{env}(f)$ directly from semantic corpora.
    

---

### **Summary**

The projection-based REM reframes the environmental base rate as an emergent property of the mind's own long-term structure, turning REM into a dual-level inference system: Bayesian normalization over the projected semantic manifold. This reinterpretation maintains REM's mathematical elegance while expanding its explanatory reach to semantic and frequency-driven effects in recognition memory.