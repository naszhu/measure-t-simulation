# Integrating the Lemma Chain with the Unified Operator Framework

## I. Bridging Mathematical Lemmas to Cognitive Operators

The lemma chain from the *set-theoretic product construction* exposes the logical scaffolding underlying memory operators in the unified short-term memory (STM) framework. Each lemma specifies a structural property that corresponds to an operator-level transformation in the cognitive model.

| Lemma  | Mathematical Principle             | Cognitive Operator                                                               | Function in STM Equation                                                         |
| ------ | ---------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| **A1** | Existence & Symmetry of Product    | **Encoding space construction**                                                  | Defines the total representational manifold ($A \times B = f_t \otimes \psi_t$). |
| **A2** | Function & Single-valuedness       | **Encoding operator** ($f_t = \Phi_{item}(x_t)$, $\psi_t = \Phi_{context}(y_t)$) | Guarantees well-defined one-to-one mapping at encoding.                          |
| **A3** | Canonical product refinement       | **Context drift operator** ($\psi_{t+1} = A_t\psi_t + B_t f_t$)                  | Expands context per event; creates disjoint subspaces.                           |
| **A4** | Collapse / projection              | **Cue overlap operator**                                                         | Defines retrieval cue generalization (collapse of drifted contexts).             |
| **A5** | Inverse relation                   | **Retrieval operator** ($a(i \mid \text{cue}) = f_i^\top W\psi(\text{cue})$)     | Inverts encoding to recover items given contextual cues.                         |
| **A6** | Common refinement / unit alignment | **Feature normalization / similarity metric**                                    | Ensures comparability of feature grains between item and context spaces.         |
| **A7** | Aggregation                        | **Decision or accumulation operator** (EBRW, REM)                                | Integrates local evidence into global retrieval probability.                     |

Together, these lemmas form the *operator logic* of the STM equation:

$$a(i|\text{cue}) = f_i^\top (D_f W D_\psi) \psi(\text{cue})$$

---

## II. Mapping Lemmas onto the Unified STM Framework

The Unified Operator Framework defines memory as transformations in a product space of item and context representations. The lemma chain clarifies how each transformation should arise naturally from the logic of sets, functions, and inverses.

### 1. Lemma A1 → The Operator Foundation

Defines the existence of the product space ($f_t \otimes \psi_t$), which in STM models becomes the *binding operator* ($W = \sum_t \gamma_t f_t \otimes \psi_t$). This guarantees that all models share a common representational substrate.

### 2. Lemma A2 → Deterministic Encoding

Encoding operators ($\Phi_{item},\Phi_{context}$) act as single-valued functions mapping external stimuli to internal features. This is the formal justification for the function constraint needed for operator composition.

### 3. Lemma A3 → Context Drift as Canonical Refinement

Expansion in Lemma A3 mirrors context drift: each event produces a disjoint contextual subspace ($\psi_t$). This refinement ensures that interference is controlled through contextual independence.

### 4. Lemma A4 → Cue Overlap and Context Collapse

The projection operator in Lemma A4 corresponds to cue overlap: retrieval collapses context instances into a shared cue space ($\psi(\text{cue})$). This is the source of *non-invertibility* — retrieval merges distinct encodings.

### 5. Lemma A5 → Retrieval as Inverse Mapping

The inverse relation formalizes retrieval as the reverse operator of encoding: ($R^{-1} : \psi \to f$). In cognitive terms, this corresponds to reconstructing item likelihoods from context cues.

### 6. Lemma A6 → Feature Alignment and Similarity Normalization

Refinement guarantees that item and context spaces are aligned at the correct granularity for comparison. This provides a mathematical foundation for REM’s featurewise likelihood normalization and TCM’s similarity computations.

### 7. Lemma A7 → Decision Aggregation

Aggregation across refined feature correspondences produces global retrieval strength. This matches the evidence accumulation or decision phase in REM, EBRW, and SAM.

---

## III. Revealing the Product-Space Gap in Cognitive Models

The Unified Operator Framework assumes that $f_t$ (item) and $\psi_t$ (context) coexist in a separable product space. The lemma chain reveals that this assumption implicitly requires the presence of operators corresponding to **A3–A6** to maintain invertibility.

| Missing Lemma       | Cognitive Consequence                       | Gap in Framework                                               |
| ------------------- | ------------------------------------------- | -------------------------------------------------------------- |
| **A3 (Expansion)**  | Context drift undefined at structural level | No operator ensuring independent contextual copies per event.  |
| **A4 (Collapse)**   | Cue overlap heuristic                       | Collapse not explicitly modeled as projection operator.        |
| **A5 (Inverse)**    | Retrieval treated as heuristic sampling     | Retrieval inverse not formally derived from encoding operator. |
| **A6 (Refinement)** | Misaligned feature granularity              | Feature normalization implicit, not defined as operator.       |

Thus, the “product space” used in current STM formulations is *incomplete*: it lacks the transformation rules (expansion, collapse, refinement) that guarantee invertibility between encoding and retrieval.

---

## IV. Operator Reformulation Using Lemma Logic

We can rewrite the unified STM operator as a full composition sequence:

$$\text{Retrieve} = D_f^{-1} \circ (\text{Collapse} \circ \text{Encode} \circ \text{Expand})^{-1} \circ D_\psi^{-1}$$

To make this invertible, each component must satisfy:

1. **Expand:** context copies disjoint (no interference).
2. **Encode:** single-valued mapping (deterministic binding).
3. **Collapse:** linear projection with known loss (controlled generalization).
4. **Refine:** measure alignment across item and context features.
5. **Aggregate:** integrate normalized evidence into decision output.

These define a **complete morphism chain** ensuring functional consistency from encoding to retrieval.

---

## V. Implications for Theoretical Development

1. **Operator completeness:** The lemma chain supplies the missing operators that make the unified STM model mathematically closed.
2. **Invertibility as memory fidelity:** Forgetting and interference can be reframed as loss of invertibility due to uncontrolled collapse or unaligned refinement.
3. **New prediction domain:** By explicitly defining these operators, we can model how representational grain and context separation interact to produce empirical forgetting curves.
4. **Mathematical unification:** The operator algebra implied by Lemmas A1–A7 turns verbal constructs (drift, cue overlap, interference) into formally composable transformations.

---

## VI. Summary Diagram (Conceptual Integration)

```
Encoding (A2)  →  Expansion (A3)  →  Collapse (A4)
                              ↓             ↓
               Retrieval (A5) ← Refinement (A6) ← Aggregation (A7)
```

**Gap:** A3–A6 operators not fully instantiated in current STM models.

---

### Core Insight

> The lemma chain provides the missing logical foundation that makes the Unified Operator Framework self-consistent. Without explicit expansion, collapse, and refinement operators, current cognitive models operate in an incomplete product space where encoding and retrieval are not true inverses but heuristic approximations of one another.
