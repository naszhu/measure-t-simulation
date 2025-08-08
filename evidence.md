In **[[evidence accumulation models]]**, “evidence” is the _state variable_S_t​, a noisy integrator whose _expected drift_ equals the desired statistic:

$\mathbb{E}[S_{t+\Delta}-S_t\mid x] \approx \mu(x)\Delta \;\propto\; \phi^\star(x).$

!!
[The noise $\eta_t$​ is **white** (i.i.d.) within a trial in canonical forms (DDM/LBA). Dependencies (LCA/DFT) come from **deterministic recurrence** (leak/inhibition), not from _sampling_ a posterior.]


In **ABS**, “evidence” is the **empirical functional** of **samples** from p(h∣x)p(h\mid x)p(h∣x). The randomness is **Monte Carlo error**:

$\operatorname{Var}(\hat{\phi}_m\mid x)\;\approx\; \frac{\sigma_\phi^2\,\tau_{\mathrm{int}}}{m}$

where τint=1+2∑k≥1ρk\tau_{\mathrm{int}}=1+2\sum_{k\ge1}\rho_kτint​=1+2∑k≥1​ρk​ is the **integrated autocorrelation time** of g(ht)g(h_t)g(ht​) under the chain. This is _colored_ (dependent) noise by construction.