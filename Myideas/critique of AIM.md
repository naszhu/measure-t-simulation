# Key issues to fix before submission

## 1) Make the core math standard and minimal

Right now the “invertibility condition” mixes necessary/sufficient ideas and introduces “exchangeability” in a non-standard way.

**Recommended refactor (drop “exchangeability”):**

- **Spaces & measures.** Let (ΩX,FX,μX)(\Omega_X,\mathcal F_X,\mu_X)(ΩX​,FX​,μX​), (ΩY,FY,μY)(\Omega_Y,\mathcal F_Y,\mu_Y)(ΩY​,FY​,μY​) be _standard Borel_ probability spaces (normalize mass to 1; “mass conservation” then is automatic).
    
- **Encoding as Markov kernel.** Kt(x,A)K_t(x, A)Kt​(x,A) measurable in xxx, a probability measure over A⊆ΩYA\subseteq \Omega_YA⊆ΩY​. Define the **Markov operator** Ft\*:P(ΩX)→P(ΩY)F_t^\* : \mathcal P(\Omega_X)\to \mathcal P(\Omega_Y)Ft\*​:P(ΩX​)→P(ΩY​) by pushforward
    
    μY(A)=(Ft\*μX)(A)=∫Kt(x,A) dμX(x).\mu_Y(A)=(F_t^\*\mu_X)(A)=\int K_t(x,A)\, d\mu_X(x).μY​(A)=(Ft\*​μX​)(A)=∫Kt​(x,A)dμX​(x).
- **Nonsingularity vs invertibility.**
    
    - If Kt(x,⋅)=δft(x)K_t(x,\cdot)=\delta_{f_t(x)}Kt​(x,⋅)=δft​(x)​ a.e. with ftf_tft​ bijective (mod 0) and bi-measurable, then Ft\*F_t^\*Ft\*​ is invertible on measures and the inverse is (ft−1)#(f_t^{-1})_\#(ft−1​)#​.
        
    - If KtK_tKt​ has **density** kt(y∣x)k_t(y|x)kt​(y∣x) w.r.t. a base λY\lambda_YλY​ and the **forward operator** Tt:L1(μX)→L1(λY)T_t: L^1(\mu_X)\to L^1(\lambda_Y)Tt​:L1(μX​)→L1(λY​) given by g↦∫kt(⋅∣x)g(x) dμX(x)g\mapsto \int k_t(\cdot|x)g(x)\,d\mu_X(x)g↦∫kt​(⋅∣x)g(x)dμX​(x) is injective and well-conditioned, then an inverse exists on its range; otherwise only **regularized inverses** make sense.
        
- **Metric regularity.** Your bi-Lipschitz statement in W2W_2W2​ is good, but phrase it as a **stability condition**:
    
    c Wp(μ,ν) ≤ Wp(Ft\*μ,Ft\*ν) ≤ C Wp(μ,ν),p ⁣∈ ⁣[1,2].c\, W_p(\mu,\nu)\ \le\ W_p(F_t^\*\mu,F_t^\*\nu)\ \le\ C\, W_p(\mu,\nu), \quad p\!\in\![1,2].cWp​(μ,ν) ≤ Wp​(Ft\*​μ,Ft\*​ν) ≤ CWp​(μ,ν),p∈[1,2].
    
    This ensures well-posed inversion (condition number C/cC/cC/c). It’s closer to standard inverse-problem language than “exchangeability”.
    
- **Compression operator.** DtD_tDt​ another Markov operator that contracts in WpW_pWp​: Wp(Dtα,Dtβ)≤ρtWp(α,β)W_p(D_t\alpha,D_t\beta)\le \rho_t W_p(\alpha,\beta)Wp​(Dt​α,Dt​β)≤ρt​Wp​(α,β) with ρt<1\rho_t<1ρt​<1. That single inequality turns into immediate lemmas about **forgetting** and **output interference**.
    

> **Actionable change:** Replace the current “invertibility iff mass-preserving + exchangeability + bi-Lipschitz” with: _Invertibility (mod 0) holds if and only if Ft\*F_t^\*Ft\*​ is induced by a bi-measurable bijection; otherwise retrieval is an ill-posed inverse problem requiring regularization. Stability is governed by the WpW_pWp​ Lipschitz bounds._

---

## 2) Tighten retrieval as an inverse problem

You already write

Gt(μY)=arg⁡min⁡νDKL(μY∥Ft\*ν)+λR(ν).G_t(\mu_Y)=\arg\min_{\nu} D_{\mathrm{KL}}(\mu_Y\Vert F_t^\*\nu)+\lambda \mathcal R(\nu).Gt​(μY​)=argνmin​DKL​(μY​∥Ft\*​ν)+λR(ν).

Great. Make it concrete:

- Note this is **generalized deconvolution** / **variational inverse** of a Markov operator.
    
- Point to **Tikhonov** (R(ν)=∥∇ν∥2\mathcal R(\nu)=\|\nabla \nu\|^2R(ν)=∥∇ν∥2), **entropic OT/Schrödinger bridge** (if you replace KL with cross-entropy under a diffusion prior), or **score-based** priors (denoising view of retrieval).
    
- Add a **consistency inequality**: if Ft\*F_t^\*Ft\*​ is CCC-Lipschitz and DtD_tDt​ has contraction ρ\rhoρ, then expected reconstruction error obeys
    
    Wp(Gtμt,μX,t) ≳ κ(C,ρ,λ,noise)W_p(G_t\mu_t,\mu_{X,t}) \ \gtrsim\ \kappa(C,\rho,\lambda,\text{noise})Wp​(Gt​μt​,μX,t​) ≳ κ(C,ρ,λ,noise)
    
    (state as a bound; you don’t need a full proof in the main text).
    

---

## 3) Remove/clarify “exchangeability”

“Exchangeability of sub-measures” is non-standard here and reads like independence. If you intend a _symmetry_ that leaves the inverse unaffected (e.g., permutations within an equivalence class of features), define a **group action** π∈G \pi\in \mathcal Gπ∈G on ΩY\Omega_YΩY​ with Ft\*=π∘Ft\*F_t^\*=\pi\circ F_t^\*Ft\*​=π∘Ft\*​ for all π\piπ in a subgroup. Then you can say: inverse is unique **up to group symmetries**. That’s cleaner and audience-friendly.

---

## 4) Connect explicitly to known operators

Add a short subsection mapping AIM objects to established ones:

- Ft\*F_t^\*Ft\*​: **Perron–Frobenius/transfer operator** (forward density evolution).
    
- UtU_tUt​: optional **Koopman** operator on observables (useful for linking to neural readouts).
    
- DtD_tDt​: **coarse-graining / information bottleneck** or **rate–distortion** step.
    
- Retrieval GtG_tGt​: **regularized inverse** / **backward kernel** (Doob hhh-transform or Schrödinger bridge under diffusion).
    

That mapping will help reviewers from ML/neuro theory see where you sit.

---

## 5) Predictions: make at least one quantitatively _decisive_

You list good qualitative effects. Turn two of them into **necessary tests**:

1. **List-length effect from support overlap (OT angle).**  
    Define overlap O=∫min⁡{dμY(i),dμY(j)}O=\int \min\{d\mu_{Y}^{(i)},d\mu_{Y}^{(j)}\}O=∫min{dμY(i)​,dμY(j)​}. Show that expected discriminability d′d'd′ (or AUC) decreases monotonically with OOO when GtG_tGt​ is a 1-Lipschitz inverse. Provide a **closed-form bound** or a tight simulation that beats REM/TCM fit with one fewer free parameter.
    
2. **Context drift as metric mismatch.**  
    Let the kernel’s ground metric change from dtd_tdt​ to dt+Δd_{t+\Delta}dt+Δ​. Derive that inverse stability scales with the **Gromov–Wasserstein** discrepancy GW(dt,dt+Δ)GW(d_t,d_{t+\Delta})GW(dt​,dt+Δ​), giving a _quantitative_ bias term in recall. That’s a unique AIM prediction.
    
3. **Neural entropy oscillation.**  
    Operationalize with multivariate entropy HtH_tHt​ on population activity using kNN or Gaussian-copula estimators. Predict **phase-locked increases at encoding (R_t), decreases at retrieval/decompression**; preregister the effect size vs. list length or delay. Provide a power analysis.
    

---

## 6) Provide a minimal, runnable instantiation

A tiny but complete pipeline will de-risk the paper:

- **Spaces:** ΩX=Rd\Omega_X=\mathbb R^dΩX​=Rd (stimulus features), ΩY=Rm\Omega_Y=\mathbb R^mΩY​=Rm (memory code).
    
- **Encoding kernel:** Gaussian channel Kt(y∣x)=N(y;Wtx,Σe)K_t(y|x)=\mathcal N(y; W_t x, \Sigma_e)Kt​(y∣x)=N(y;Wt​x,Σe​).
    
- **Compression:** DtD_tDt​ = additive Gaussian + sparsifying shrinkage or a learned contractive map.
    
- **Retrieval:** solve your KL-regularized inverse (or L2 inverse with Tikhonov) and evaluate W2W_2W2​-error and behavioral accuracy on synthetic lists.
    

This shows: (i) identifiability with/without compression, (ii) list-length and output-interference curves from first principles, (iii) invertibility-consistency (IC) tracking accuracy.

_(You don’t ask for code here; if you later want it, I’ll give a compact JAX/Julia implementation with OT utilities and evaluation plots.)_

---

# Specific line edits / math tweaks

- **2.1 “Each item is a measurable subset”:**  
    Prefer items as _probability measures_ (or Dirac masses) on ΩX\Omega_XΩX​. Subsets are fine for exposition but muddy when you move to kernels and mixture superposition.  
    → “Each event iii is represented by μX,i∈P(ΩX)\mu_{X,i}\in\mathcal P(\Omega_X)μX,i​∈P(ΩX​); a list is μX=∑iwiμX,i\mu_X=\sum_i w_i \mu_{X,i}μX​=∑i​wi​μX,i​.”
    
- **2.2 “human-defined alignment”:**  
    Reviewers will balk. Say: the alignment is **learned** as the Markov kernel KtK_tKt​ parameterized by θt\theta_tθt​; learning increases mutual information I(X;Y)I(X;Y)I(X;Y) under resource constraints (link to rate–distortion/information bottleneck).
    
- **3.2 Lemma (Invertibility Condition):**  
    Replace with two lemmas:
    
    1. _(Exact invertibility)_ If Kt(x,⋅)=δft(x)K_t(x,\cdot)=\delta_{f_t(x)}Kt​(x,⋅)=δft​(x)​ with ftf_tft​ bijective (mod 0), then Ft\*F_t^\*Ft\*​ is invertible on P\mathcal PP with inverse (ft−1)#(f_t^{-1})_\#(ft−1​)#​.
        
    2. _(Stability)_ If Ft\*F_t^\*Ft\*​ is ccc-strongly expansive and CCC-Lipschitz in WpW_pWp​, then the inverse problem is well-conditioned with condition number κ=C/c\kappa=C/cκ=C/c.
        
- **4. Table entries:**  
    “Functorial inverse” → clarify as an **adjunction** Gt⊣Ft\*G_t\dashv F_t^\*Gt​⊣Ft\*​ on appropriate categories (e.g., probability measures with Markov morphisms) _only when_ a free-energy functional defines both maps as primal/dual solutions. Otherwise, call it “regularized inverse”.
    
- **5. Retrieval objective:**  
    Add existence/uniqueness: convexity in ν\nuν if Ft\*F_t^\*Ft\*​ is linear in measures and R\mathcal RR is convex; provide conditions when the minimizer exists and is unique.
    
- **6. Forgetting function:**  
    Your E[a(μt+1,μt)]≈e−cσt2E[a(\mu_{t+1},\mu_t)] \approx e^{-c\sigma_t^2}E[a(μt+1​,μt​)]≈e−cσt2​ is interesting—anchor a(⋅,⋅)a(\cdot,\cdot)a(⋅,⋅) as a concrete similarity (e.g., Hellinger affinity or overlap integral) and show the approximation for Gaussian compression with variance σt2\sigma_t^2σt2​. This can be a 5-line derivation in the appendix.
    
- **7. REM integration:**  
    Make the mapping explicit: REM’s feature-wise likelihood ratio equals an **inner product in L2(λ)L^2(\lambda)L2(λ)**; show how REM’s encoding matrix WtW_tWt​ recovers the Gaussian-channel kernel case, and how **IC** equals −DKL(μY∥Ft\*GtμY)-D_{\mathrm{KL}}(\mu_Y\Vert F_t^\*G_t\mu_Y)−DKL​(μY​∥Ft\*​Gt​μY​) which bounds retrieval error by **Pinsker** in W1W_1W1​.
    

---

# What to add for empirical credibility

1. **One clear disconfirmation test.** E.g., manipulate _compression strength_ (secondary task load or time-dependent consolidation) while holding _overlap_ constant; AIM predicts a specific rotation of ROC isometrics (criterion-free) that trace WpW_pWp​-distance rather than just drift rate changes. Competing models don’t naturally give that geometry.
    
2. **Neural link.** Tie entropy oscillations to a specific signal and estimator: multi-unit LFP/MEG with **coarse-grained entropy** at theta cycles; preregister: encoding ↑ entropy (refinement), retrieval ↓ entropy (decompression), magnitude scales with ρt\rho_tρt​ estimated from behavior.
    
3. **Model recovery on synthetic data.** Show that when data are generated by an AIM-like kernel+compression, REM/TCM fits produce systematic parameter distortions—but AIM recovers ground truth.
    

---

# Where to send it (and how to frame)

- **Psychological Review / Trends-style theory** if you push the math + cross-model unification and include one decisive, novel prediction.
    
- **BRM or Comp Brain & Behav** if you emphasize the computational instantiation and simulations.  
    Lead with: “Memory as an inverse problem over measures; REM/TCM/SAM are finite-dimensional discretizations; forgetting = contraction; retrieval = regularized inverse.”
    

---

# Minimal revised core (drop-in)

> **Definition (Encoding).** Ft\* ⁣:P(ΩX) ⁣→ ⁣P(ΩY)F_t^\*\!:\mathcal P(\Omega_X)\!\to\!\mathcal P(\Omega_Y)Ft\*​:P(ΩX​)→P(ΩY​) is the Markov operator induced by kernel Kt(y∣x)K_t(y|x)Kt​(y∣x).  
> **Definition (Compression).** DtD_tDt​ is a Markov operator with WpW_pWp​-contraction factor ρt<1\rho_t<1ρt​<1.  
> **Proposition (Exact invertibility).** If Kt(x,⋅)=δft(x)K_t(x,\cdot)=\delta_{f_t(x)}Kt​(x,⋅)=δft​(x)​ with ftf_tft​ a bi-measurable bijection (mod 0), then (Ft\*)−1=(ft−1)#(F_t^\*)^{-1}=(f_t^{-1})_\#(Ft\*​)−1=(ft−1​)#​.  
> **Proposition (Stability).** If cWp(μ,ν)≤Wp(Ft\*μ,Ft\*ν)≤CWp(μ,ν)c W_p(\mu,\nu)\le W_p(F_t^\*\mu,F_t^\*\nu)\le C W_p(\mu,\nu)cWp​(μ,ν)≤Wp​(Ft\*​μ,Ft\*​ν)≤CWp​(μ,ν), the inverse is well-posed with condition number κ=C/c\kappa=C/cκ=C/c.  
> **Definition (Retrieval).** Gt(μ)=arg⁡min⁡νDKL(μ∥Ft\*ν)+λR(ν)G_t(\mu)=\arg\min_{\nu} D_{\mathrm{KL}}(\mu\Vert F_t^\*\nu)+\lambda \mathcal R(\nu)Gt​(μ)=argminν​DKL​(μ∥Ft\*​ν)+λR(ν).  
> **Corollary (Forgetting).** If DtD_tDt​ has contraction ρt\rho_tρt​, then Wp(GtDtFt\*μX,μX)≥(1−ρt)⋅ϕ(κ,λ)W_p(G_t D_t F_t^\*\mu_X,\mu_X)\ge (1-\rho_t)\cdot \phi(\kappa,\lambda)Wp​(Gt​Dt​Ft\*​μX​,μX​)≥(1−ρt​)⋅ϕ(κ,λ) for some ϕ\phiϕ depending on regularization and conditioning.

These five statements + one concrete simulation will carry the paper.