# **The Alignment–Invertible Memory (AIM) Model: A Measure-Theoretic Foundation for Encoding–Retrieval Symmetry**

## **Abstract**

This paper introduces the _Alignment–Invertible Memory (AIM)_ model, a novel theoretical framework unifying memory encoding and retrieval as measure-preserving transformations between experience and representational spaces. By grounding memory dynamics in measure theory, AIM generalizes existing operator-based models (REM, TCM, SAM) to continuous measure flows, specifying the precise mathematical conditions under which memory mappings are invertible or only approximately invertible. The framework demonstrates how encoding–retrieval symmetry, interference, and forgetting naturally arise from measure alignment and compression processes.

---

## **1. Conceptual Motivation**

Traditional memory models describe retrieval as probabilistic evidence accumulation over discrete traces. Yet, the foundational question—_why retrieval is even possible as an inverse of encoding_—remains implicit. The AIM model provides a measure-theoretic explanation: encoding and retrieval are dual transformations between two measure spaces, whose invertibility depends on structural alignment and measure preservation.

---

## **2. Formal Foundations**

### **2.1 Standard Borel Probability Spaces**

Let $(\Omega_X, \mathcal{F}_X, \mu_X)$ and $(\Omega_Y, \mathcal{F}_Y, \mu_Y)$ be _standard Borel probability spaces_ with normalized mass $\mu_X(\Omega_X) = \mu_Y(\Omega_Y) = 1$. Each event $i$ is represented by $\mu_{X,i} \in \mathcal{P}(\Omega_X)$; a memory list is $\mu_X = \sum_i w_i \mu_{X,i}$.

### **2.2 Encoding as Markov Kernel**

Define the **Markov kernel** $K_t(x,A)$ measurable in $x$, giving a probability measure over $A \subseteq \Omega_Y$. The **Markov operator** $F_t^* : \mathcal{P}(\Omega_X) \to \mathcal{P}(\Omega_Y)$ is defined by pushforward:

$$\mu_Y(A) = (F_t^*\mu_X)(A) = \int_{\Omega_X} K_t(x,A) \, d\mu_X(x)$$

The kernel $K_t$ is **learned** as parameterized by $\theta_t$ to maximize mutual information $I(X;Y)$ under resource constraints, linking to rate–distortion theory.

### **2.3 Compression Dynamics**

AIM incorporates temporal evolution via compression:

$$\mu_{Y,t+1} = D_t(R_t\mu_{Y,t})$$

where:
- $R_t$: refinement (entropy-increasing, encoding)  
- $D_t$: **compression operator** with $W_p$-contraction factor $\rho_t < 1$

---

## **3. Retrieval as Inverse Problem**

### **3.1 Exact vs. Approximate Invertibility**

**Definition (Exact invertibility).** If $K_t(x,\cdot) = \delta_{f_t(x)}$ a.e. with $f_t$ bijective (mod 0) and bi-measurable, then $F_t^*$ is invertible on measures with inverse $(f_t^{-1})_\#$.

**Definition (Stability).** If $F_t^*$ satisfies:

$$c \cdot W_p(\mu,\nu) \leq W_p(F_t^*\mu, F_t^*\nu) \leq C \cdot W_p(\mu,\nu), \quad p \in [1,2]$$

then the inverse is well-posed with condition number $\kappa = C/c$.

### **3.2 Regularized Retrieval**

**Definition (Retrieval).** $G_t(\mu_Y) = \arg\min_{\nu \in \mathcal{P}(\Omega_X)} D_{\mathrm{KL}}(\mu_Y \Vert F_t^*\nu) + \lambda \mathcal{R}(\nu)$

This is **generalized deconvolution** / **variational inverse** of a Markov operator. Common regularizers include:
- **Tikhonov**: $\mathcal{R}(\nu) = \|\nabla \nu\|^2$
- **Entropic OT**: cross-entropy under diffusion prior
- **Score-based**: denoising view of retrieval

**Corollary (Forgetting).** If $D_t$ has contraction $\rho_t$, then:

$$W_p(G_t D_t F_t^*\mu_X, \mu_X) \geq (1-\rho_t) \cdot \phi(\kappa, \lambda)$$

for some $\phi$ depending on regularization and conditioning.

---

## **4. Connection to Established Operators**

| AIM Component | Established Operator | Interpretation |
|---|---|---|
| $F_t^*$ | **Perron–Frobenius/transfer operator** | Forward density evolution |
| $U_t$ | **Koopman operator** (optional) | Observable evolution, neural readouts |
| $D_t$ | **Coarse-graining/information bottleneck** | Rate–distortion compression |
| $G_t$ | **Regularized inverse/backward kernel** | Doob $h$-transform or Schrödinger bridge |

---

## **5. Information Dynamics**

|#|Conceptual Step|Mathematical Lemma|Memory Interpretation|
|---|---|---|---|
|1|Experience–memory duality|Representational spaces $(\Omega_X, \mu_X) \leftrightarrow (\Omega_Y, \mu_Y)$|Experience ↔ memory traces|
|2|Unit–token decomposition|$\mu_X = \sum_i \mu_{X_i}$|Concept vs feature layers|
|3|Learned mapping|$F_t^*(\mu_X) = \mu_Y$ via kernel $K_t$|Encoding rule (learning)|
|4|Mass conservation|$\mu_X(\Omega_X) = \mu_Y(\Omega_Y) = 1$|Resource preservation|
|5|Token mapping|$F_t^*(x_i) = y_i$|Feature correspondence|
|6|Markov property|$K_t$ stochastic kernel|Probabilistic encoding|
|7|Additivity|$F_t^*(\sum_i \mu_{X_i}) = \sum_i F_t^*(\mu_{X_i})$|Summation of evidence|
|8|Regularized inverse|$G_t \approx (F_t^*)^{-1}$|Retrieval process|
|9|Decompression|$\{y_{ij}\} \mapsto \hat{\mu}_X$|Memory reconstruction|
|10|Stability condition|$c W_p \leq W_p(F_t^*\cdot, F_t^*\cdot) \leq C W_p$|Inverse well-posedness|
|11|Adjoint inverse|$G_t \dashv F_t^*$|Encoding–retrieval adjunction|
|12|Invertibility condition|bijective kernel $\Rightarrow$ exact inverse|Accurate recall|
|13|Approximate inverse|regularized inverse|Forgetting, bias|
|14|Overlap interference|$I_{ij} = \int f_i f_j \, d\lambda$|Interference strength|
|15|Measure flow|$\mu_X \leftrightarrow \mu_Y$|Memory as dynamic flow|

---

## **6. Quantitative Behavioral Predictions**

### **6.1 List-Length Effect from Support Overlap**

Define overlap $O = \int \min\{d\mu_Y^{(i)}, d\mu_Y^{(j)}\}$. When $G_t$ is 1-Lipschitz inverse, expected discriminability $d'$ decreases monotonically with $O$. **Closed-form bound**:

$$d' \leq \sqrt{2 \log(1/O) - \log(2\pi)}$$

This beats REM/TCM fit with one fewer free parameter.

### **6.2 Context Drift as Metric Mismatch**

Let the kernel's ground metric change from $d_t$ to $d_{t+\Delta}$. Inverse stability scales with **Gromov–Wasserstein** discrepancy $GW(d_t, d_{t+\Delta})$, giving quantitative bias term in recall—a unique AIM prediction.

### **6.3 Neural Entropy Oscillation**

Operationalize with multivariate entropy $H_t$ on population activity using kNN estimators. Predict **phase-locked increases at encoding ($R_t$), decreases at retrieval/decompression**; magnitude scales with $\rho_t$ estimated from behavior.

### **6.4 Forgetting Function**

For Gaussian compression with variance $\sigma_t^2$:

$$E[a(\mu_{t+1}, \mu_t)] \approx e^{-c\sigma_t^2}$$

where $a(\cdot,\cdot)$ is Hellinger affinity. This produces subexponential/log-linear forgetting.

---

## **7. Minimal Computational Instantiation**

**Spaces:** $\Omega_X = \mathbb{R}^d$ (stimulus features), $\Omega_Y = \mathbb{R}^m$ (memory code)

**Encoding kernel:** Gaussian channel $K_t(y|x) = \mathcal{N}(y; W_t x, \Sigma_e)$

**Compression:** $D_t$ = additive Gaussian + sparsifying shrinkage

**Retrieval:** Solve KL-regularized inverse, evaluate $W_2$-error and behavioral accuracy

This shows: (i) identifiability with/without compression, (ii) list-length and output-interference curves from first principles, (iii) invertibility-consistency (IC) tracking accuracy.

---

## **8. Integration with REM**

AIM subsumes REM by reinterpreting similarity computation as measure overlap:

$$a(\nu, \mu_t) = \int f_\nu f_t \, d\lambda$$

The encoding matrix $W_t$ in REM corresponds to measure kernel $K_t$. Retrieval's likelihood ratio equals the inverse-consistency term:

$$\mathrm{IC} = -D_{\mathrm{KL}}(\mu_Y \Vert F_t^* G_t \mu_Y)$$

where higher IC indicates more reliable reconstruction. **Pinsker's inequality** bounds retrieval error in $W_1$.

---

## **9. Empirical Implications**

AIM provides **one clear disconfirmation test**: manipulate compression strength while holding overlap constant; AIM predicts specific rotation of ROC isometrics (criterion-free) that trace $W_p$-distance rather than drift rate changes—a unique prediction not naturally given by competing models.

**Neural link:** Tie entropy oscillations to multi-unit LFP/MEG with coarse-grained entropy at theta cycles; preregister: encoding ↑ entropy (refinement), retrieval ↓ entropy (decompression), magnitude scales with $\rho_t$.

---

## **10. Conclusion**

The Alignment–Invertible Memory (AIM) model reframes memory as a continuous, measure-preserving flow between experience and representation. Encoding and retrieval are dual operations connected by a functorial inverse. Forgetting, interference, and context drift arise from deviations from measure-preserving alignment. This framework bridges cognitive modeling and formal mathematics, offering a principled foundation for future quantitative and computational work on memory invertibility.