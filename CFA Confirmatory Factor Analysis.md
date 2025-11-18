# Confirmatory Factor Analysis (CFA)
A clean, concise explanation for SEM users

---

## 1. What is CFA?

**Confirmatory Factor Analysis (CFA)** is a statistical method used to test whether your data fit a **theoretical measurement model**—that is, whether the items you designed truly measure the latent constructs you claim they measure.

In SEM, CFA is used to **validate measurement models** before testing structural paths.

---

## 2. Why CFA is needed in SEM

SEM is built on two stages:

1. **Measurement model** (Are the latent variables valid?)  
2. **Structural model** (Are the paths between latent variables significant?)

CFA evaluates Stage 1.

If the latent variables are not validated by CFA, then any SEM path estimates (regression paths) are **not trustworthy**.

---

## 3. What CFA actually tests

CFA specifies **which items load on which latent factors**.

For example, suppose you have:

- Aesthetics → 6 items  
- Engagement → 4 items  
- Retention → 3 items

CFA explicitly tests:

- Do the Aesthetics items only load on the Aesthetics factor?  
- Do Engagement items load strongly on Engagement?  
- Is each loading large and significant?  
- Are the constructs distinct (discriminant validity)?  
- Are the items reliable (internal consistency)?  

---

## 4. The CFA Model Form (General)

For a latent factor $F$ and items $Y_1, Y_2, \dots, Y_k$:

$$
Y_i = \lambda_i F + \varepsilon_i
$$

Where:

- $\lambda_i$ = factor loading  
- $\varepsilon_i$ = unique error term  
- $F$ = latent variable  

A full CFA specifies the loading structure for all factors simultaneously.

---

## 5. What you must report in CFA

### **5.1 Factor loadings**
- Each item must load significantly on its intended factor.  
- Standardized loadings ideally > .50 or .60.

### **5.2 Model fit indices (e.g., for Lavaan/Mplus/AMOS)**
Common criteria:
- **CFI > .95**
- **TLI > .95**
- **RMSEA < .06**
- **SRMR < .08**

### **5.3 Reliability**
- Cronbach’s alpha  
- Composite Reliability (CR)  
- Values > .70 are acceptable

### **5.4 Convergent validity**
Using **Average Variance Extracted (AVE)**:
$$
\text{AVE} = \frac{\sum \lambda_i^2}{k}
$$
Criteria:
- AVE > .50

### **5.5 Discriminant validity**
Fornell–Larcker criterion:
$$
\sqrt{\text{AVE}_{A}} > \text{corr}(A, B)
$$
for every pair of factors A and B.

This checks whether your constructs are **distinct**.

---

## 6. Example CFA model (conceptual)

