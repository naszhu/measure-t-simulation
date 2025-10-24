### <b>REM (Retrieving Effectively from Memory)</b>

<b>Unified Form (in operator space):</b><br>
REM occupies the <i>probabilistic operator space</i> of the unified framework, where stored associations are stochastic rather than deterministic bindings.

$$
W = \mathbb{E}\!\left[\sum_{t=1}^{T}\gamma_t f_t \otimes \psi_t \right], 
\qquad 
a(i|\text{cue}) = \mathbb{E}[\,f_i^\top W\,\psi(\text{cue})\,]
$$

<ul>
<li><b>f<sub>t</sub></b>: high-dimensional vector of discrete feature values representing the studied item.</li>
<li><b>ψ<sub>t</sub></b>: latent context vector (static or slowly drifting, e.g. ψ<sub>t+1</sub> = ρψ<sub>t</sub> + ηf<sub>t</sub>).</li>
<li><b>γ<sub>t</sub></b>: encoding strength determined by storage probability u* and copy accuracy c.</li>
<li><b>W</b>: stochastic binding operator whose entries follow geometric base-rate distributions P[V=j]=(1−g)<sup>j−1</sup>g.</li>
</ul>

---

<b>Cognitive Process Interpretation</b>



<li><b>Representation</b> – Each word is a vector of features; base-rate parameter g determines environmental commonness.</li>
<li><b>Storage</b> – An episodic image is a noisy, incomplete copy of the studied vector: each feature stored with probability u* and copied correctly with probability c.</li>
<b>Retrieval</b> – The probe vector is matched in parallel to all stored images.  
For each image E<sub>j</sub>, a <i>likelihood ratio</i> is computed:  
$$
\Lambda_j = \frac{P(D_j|\text{s-image})}{P(D_j|\text{d-image})}
$$  
where D<sub>j</sub> summarizes the pattern of feature matches/mismatches.  
Overall Bayesian odds of “old”:  
$$
\Phi = \frac{1}{n}\sum_{j=1}^{n}\Lambda_j
$$  
The model responds “old’’ when Φ>1.
<li><b>Decision Rule</b> – A single normative Bayesian criterion (odds = 1) governs all decisions; no criterion adjustment is required across conditions.</li>


---

<b>Mathematical Characterization in the Unified Framework</b>

<ul>
<li><b>Space type:</b> Probabilistic operator space</li>
<li><b>Retrieval mapping:</b> Expectation of stochastic item–context projection</li>
<li><b>Coupling:</b> Joint embedding of item and context features with uncertainty</li>
<li><b>Computation:</b> Bayesian likelihood comparison rather than deterministic similarity</li>
</ul>

$$
a(i|\text{cue}) \;\propto\; 
\mathbb{E}\!\left[\frac{P(D|\text{s-image})}{P(D|\text{d-image})}\right]
$$

---

<b>Psychological Signatures and Predicted Phenomena</b>

<table>
<thead>
<tr><th>Phenomenon</th><th>Mechanism in REM</th></tr>
</thead>
<tbody>
<tr><td><b>List-length effect</b></td><td>More stored images → higher chance matches → reduced discriminability d′.</td></tr>
<tr><td><b>List-strength effect</b></td><td>Strong items have more stored features → greater differentiation → no interference or slight facilitation for weak items.</td></tr>
<tr><td><b>Mirror effect</b></td><td>Bayesian criterion fixed at odds = 1 naturally yields higher hits and lower false alarms for strong conditions.</td></tr>
<tr><td><b>Normal ROC slope &lt; 1</b></td><td>Target odds distribution broader than distractor distribution.</td></tr>
<tr><td><b>Word-frequency effect</b></td><td>High-frequency words (large g) have common features → lower diagnosticity → lower d′.</td></tr>
</tbody>
</table>

---

<b>Summary</b><br>
REM formalizes recognition as <i>probabilistic Bayesian retrieval</i> from a set of noisy episodic feature copies.<br>
Within the unified operator framework, it represents the <b>stochastic limit</b> of item–context models: retrieval is the expected projection of a random binding operator rather than a fixed mapping, making REM the bridge between global-matching similarity models and normative Bayesian inference approaches to memory.
