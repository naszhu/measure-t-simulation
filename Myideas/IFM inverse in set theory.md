[[what can set memory theory solve]]
# The Invertible Function Memory ([[IFM]]) Model

## Abstract

The Invertible Function Memory (IFM) model reconstructs memory as a purely set-theoretic system of mappings between experiential and representational domains. Without invoking probability or measure, it defines encoding, retrieval, forgetting, and interference as structural properties of functions between finite sets. IFM serves as the discrete foundation of continuous models such as AIM, where measure-theoretic operators replace set mappings.

---

## 1. Foundations

Let  
(E_t): set of all experiences up to time (t).  
(R_t): set of all memory representations at time (t).  
Define functions:

[  
f_t:E_t\to R_t \quad \text{(encoding)}, \qquad g_t:R_t\to E_t \quad \text{(retrieval)}.  
]

Encoding is total (every experience is encoded). Retrieval approximates the inverse:  
(g_t\circ f_t \approx \mathrm{id}_{E_t}).

---

## 2. Core Quantities

### Recall Accuracy

[  
A_t = \frac{|{e\in E_t : g_t(f_t(e)) = e}|}{|E_t|}  
]  
Proportion of perfectly reconstructible experiences.

### Interference Index

[  
I_t = \frac{|{(e_1,e_2)\in E_t^2 : e_1\ne e_2, f_t(e_1)=f_t(e_2)}|}{|E_t|(|E_t|-1)}  
]  
Rate of representational collisions (non-injectivity).

### Accessibility

[  
S_t = \frac{|\mathrm{Im}(f_t)|}{|R_t|}  
]  
Fraction of representation space utilized.

---

## 3. Temporal Dynamics

### Encoding Update

New experience (e_{t+1}):  
[  
E_{t+1} = E_t \cup {e_{t+1}}, \quad f_{t+1}(e_{t+1}) = \operatorname{select}(R_t)  
]  
Rule of selection determines interference growth.

### Forgetting

Mapping stability:  
[  
F_t = \frac{| { e\in E_t : f_{t+\Delta t}(e)=f_t(e) } |}{|E_t|}  
]  
Forgetting rate ≈ (1-F_t).

---

## 4. Context and Cue Expansion

To restore injectivity, extend domains by contextual cues:  
[  
E_t' = E_t \times C_t, \quad R_t' = R_t \times C_t, \quad f_t'(e,c)=(f_t(e),c).  
]  
Then (f_t') is injective; cue reinstatement isolates equivalence classes during retrieval.

---

## 5. Lemmas

**Lemma 1 (Interference–Accuracy Tradeoff)**  
If (|R_t|<|E_t|), expected (I_t>0) and (A_t<1).  
Proof: Pigeonhole principle. □

**Lemma 2 (Context Enlargement Restores Bijection)**  
If (f_t) not injective, defining (f_t'(e,c)=(f_t(e),c)) with unique cues yields injectivity. □

**Lemma 3 (Stable Mapping Yields Perfect Recall)**  
If (f_t=f_{t+k}) and (g_t=f_t^{-1}) on (\mathrm{Im}(f_t)), then (A_{t+k}=1). □

---

## 6. Simulation Schema

A minimal computational form:

```julia
E = 1:100                # 100 experiences
R = 1:80                 # 80 memory traces
f = rand(R, length(E))   # encoding mapping
g = Dict(r => rand(E))   # retrieval guesses
accuracy = sum(g[f[e]] == e for e in E) / length(E)
interference = length(unique(f)) / length(E)
```

Simulation reproduces interference and recall accuracy from discrete set mappings.

---

## 7. Cognitive Mapping

|IFM Component|Cognitive Meaning|
|---|---|
|(f:E\to R)|Encoding of experience to representation|
|(g:R\to E)|Retrieval (approximate inverse)|
|Non-injectivity|Interference / confusion|
|Non-surjectivity|Cue failure / inaccessibility|
|Context expansion|Context reinstatement|
|(A_t,I_t,S_t)|Hit rate, interference, load|
|Mapping stability (F_t)|Retention over delay|

---

## 8. Relation to Other Models

|Model|IFM Interpretation|
|---|---|
|REM|IFM + probabilistic weights on (f,g)|
|SAM|IFM + associative retrieval structure|
|TCM|IFM + contextual product (E\times C)|
|AIM|Continuous measure-theoretic extension of IFM|

---

## 9. Summary

The IFM model shows that memory dynamics can be formalized through pure set theory:

- Forgetting = loss of injectivity
    
- Inaccessibility = loss of surjectivity
    
- Context reinstatement = domain expansion restoring bijection
    

It provides the discrete skeleton for continuous formulations like AIM, establishing a foundational logical model of memory invertib