# Evaluation of the SEM Analysis in  
**“The Influence of Game Aesthetics on Game Engagement and Retention”**  
(*Methods correctness review*)

---

## 1. Overall Judgement
The analysis is **methodologically weak and partially incorrect**.  
The model is **conceptually unclear**, **statistically underspecified**, and **the mediation/moderation claims (H3, H4)** are **not tested correctly**.

---

## 2. Major Problems (Conceptual + Statistical)

### **2.1. No clear latent–indicator structure for “Game Aesthetics”**
The paper treats *Game Aesthetics* as a **latent factor** with six indicators.  
But they do **not report**:

- [[CFA Confirmatory Factor Analysis]] model  
- factor correlations  
- item loadings for all constructs  
- AVE, composite reliability, discriminant validity  
- model modifications  

They only show loadings for *Game Aesthetics*, not for *Engagement* or *Retention*.

This means the latent structure is **not validated**, but they continue to run SEM.

---

### **2.2. Engagement and Retention constructs are not validated**
Both are latent constructs but the paper **never reports**:

- factor loadings  
- number of items per construct  
- whether a second-order factor model was tested (flow, presence, immersion, absorption)

They simply assert reliability (Cronbach α > .70) and skip all CFA steps.

This makes the SEM model **unreliable**, because SEM requires validated measurement models.

---

### **2.3. Hypotheses H3–H4 (mediation & moderation) are not tested properly**

#### **H3: Engagement → Retention (mediation structure)**
To test mediation, they would need:

- indirect effect: $\text{Aesthetics} \to \text{Engagement} \to \text{Retention}$
- path coefficients: $a$, $b$, $c$, $c'$  
- **[[bootstrap]] CI** for the indirect effect

But the paper **does none of this**.

They simply regress Retention on Engagement (β = .045, p = .857) and conclude “no relationship.”  
This is **not a mediation test**.

#### **H4: Engagement moderates the effect of Aesthetics on Retention**
Moderation requires:

- an interaction term: $(\text{Aesthetics} \times \text{Engagement})$  
- OR multi-group SEM

The paper **does neither**.

Yet they claim to test “moderation,” but the statistical model contains **no interaction path**.

Thus H4 is **not tested at all**.

---

### **2.4. The sample and model complexity are mismatched**
They use:

- 400 cases  
- 6 indicators for aesthetics  
- 4 indicators for engagement  
- 3 indicators for retention  

This is borderline OK for SEM, but they do not report **degrees of freedom for CFA**, **sample-to-parameter ratio**, or **model constraints**, making it unclear whether the model is properly identified.

---

### **2.5. Overinterpretation of path coefficients**
They conclude:

> “Aesthetics significantly predicts engagement AND retention.”

But they do not consider:
- common method bias  
- multicollinearity between aesthetics and engagement  
- causal direction mistakes (cross-sectional data cannot infer causality)

The model is **descriptive correlation**, but the discussion treats it as causal.

---

## 3. Minor Technical Issues

### **3.1. Fit indices reported but not justified**
RMSEA = .058  
CFI = .988  
NFI = .983

Although acceptable, they never report alternative models, chi-square, or modification indices.

### **3.2. Missing details in measurement**
Lavaan syntax is not provided.  
Item wording is not shown.  
Loadings for engagement/retention are absent.  
Thus the measurement portion of SEM is **incomplete**.

---

## 4. What **should** have been done (correct SEM workflow)

### **Step 1 — CFA for each latent variable**
Validate:
- factor loadings  
- AVE & CR  
- discriminant validity  

### **Step 2 — Structural model**
Estimate paths:
- Aesthetics → Engagement  
- Aesthetics → Retention  
- Engagement → Retention

### **Step 3 — Mediation test**
Compute:
- indirect effect $ab$  
- bootstrap CI  

### **Step 4 — Moderation test**
Add interaction term:
$$
\text{Retention} = b_1(\text{Aesthetics}) + b_2(\text{Engagement}) + b_3(\text{Aesthetics} \times \text{Engagement})
$$
Or use multi-group SEM.

None of these were done.

---

## 5. Final Evaluation

| Component | Correct? | Comment |
|----------|----------|---------|
| Measurement model | ❌ | No CFA for 2 constructs; partial reporting only |
| SEM structural paths | ⚠️ | Basic regressions are correct, but incomplete |
| Mediation test | ❌ | Not done; indirect effect not estimated |
| Moderation test | ❌ | No interaction term; hypothesis not tested |
| Interpretation of results | ❌ | Causal language used with cross-sectional data |
| Model fit reporting | ⚠️ | Fit indices ok, but model unvalidated |

**Overall:**  
The statistical analysis is **not rigorous**, **does not test the key hypotheses**, and lacks necessary SEM validation steps.

---

## 6. If you want
I can create a separate file:

- **A corrected SEM model** for this study  
- Proper diagrams  
- Full Lavaan code  
- Proper mediation & moderation tests  
- A “better” academic presentation slide summarizing the flaws  

