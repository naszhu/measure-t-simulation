# The Lemma Chain and the Structural Gap in Memory Models

## I. Mathematical Lemma Chain (Set-Theoretic Foundation)

### Lemma A1 — Existence & Symmetry of Product

* **Statement:** For any sets $A, B$, the product $A\times B$ exists with projections $\pi_1, \pi_2$. Each element of $A$ has a fibre isomorphic to $B$, and vice versa.
* **Meaning:** Constructs the *complete space of possible bindings* between two sets.
* **Visualization:** 3 apples ($A$) × 2 dollars ($B$) → 6 pair-points $(a_i,b_j)$.

### Lemma A2 — Function & Single-Valuedness

* **Statement:** A function is a relation $f\subseteq A\times B$ where each $a\in A$ maps to exactly one $b\in B$. This guarantees composition closure.
* **Meaning:** Establishes determinism of encoding.
* **Visualization:** Each apple connects to one specific dollar, ensuring unambiguous mapping.

### Lemma A3 — Canonical Product Refinement (Expansion)

* **Statement:** If every $a$ needs an independent copy of $B$, the unique minimal structure is $A\times B$.
* **Meaning:** Defines independent contextual copies for each element; the principle of context separation.
* **Visualization:** Each apple has its own disjoint pair of dollars.

### Lemma A4 — Collapse (Forgetting Labels)

* **Statement:** The projection $q(a_i,b_j)=b_j$ collapses disjoint copies back into shared types.
* **Meaning:** Defines information loss or generalization; merging contexts.
* **Visualization:** All copies of $b_1$ collapse to one shared node $b_1$.

### Lemma A5 — Inverse Relation

* **Statement:** For any relation $R\subseteq A\times B$, the inverse $R^{-1}\subseteq B\times A$ is defined by pair-flip.
* **Meaning:** Introduces retrieval as the inverse process of encoding.
* **Visualization:** Context nodes now point to items.

### Lemma A6 — Common Refinement (Unit Alignment)

* **Statement:** If atomic granularity differs across sets, refine both until a one-to-one pairing exists.
* **Meaning:** Aligns feature units or measurement scales; establishes the condition for invertibility.
* **Visualization:** Split apples into halves and dollars into $1 units, creating a bijection between atomic elements.

### Lemma A7 — Aggregation (Global Rate)

* **Statement:** Group refined atoms back into composite units; global mapping ratio $(1,\text{apple} : 2,\text{dollars})$ or $(1/2,\text{apple per dollar})$.
* **Meaning:** Defines global statistical regularities as aggregation over local bijections.

---

## II. Cognitive Interpretation: Mapping to Memory Models

| Lemma  | Mathematical Role      | Cognitive Analogue                                                |
| ------ | ---------------------- | ----------------------------------------------------------------- |
| **A1** | Build $A\times B$ grid | Representational possibility space (items × context)              |
| **A2** | Single-valued mapping  | Deterministic encoding: each item encoded in one contextual state |
| **A3** | Expansion              | Context drift: new contextual instance per event or list          |
| **A4** | Collapse               | Cue overlap: retrieval generalization and interference            |
| **A5** | Inverse relation       | Retrieval as search from context to items                         |
| **A6** | Refinement             | Feature-level comparison: evidence normalization across units     |
| **A7** | Aggregation            | Global decision: summed likelihood / recognition strength         |

---

## III. The Structural Gap Revealed by the Lemmas

1. **Missing Expansion–Collapse Operator**

   * Memory models (REM, TCM) have *drift* (expansion) and *cue overlap* (collapse) but no formal operator ensuring $\text{Collapse} \circ \text{Expansion} = I$.
   * The conditions for contextual invertibility are never defined.

2. **Function-to-Relation Shift Without Justification**

   * Encoding is treated as a function $f: \text{Item}\to\text{Context}$.
   * Retrieval acts as a probabilistic inverse $R^{-1}: \text{Context}\to P(\text{Item})$.
   * No formal lemma bridges functional encoding and stochastic retrieval.

3. **Absent Unit Alignment (Granularity Problem)**

   * Cognitive models assume feature independence without specifying the grain of comparison.
   * Lemma A6 shows that invertibility requires a common refinement: alignment of feature-level units between item and context representations.

4. **Lack of Compositional Closure**

   * Without single-valued mappings for all steps, composition (encode→retrieve→re-encode) is undefined.
   * Memory models thus lack categorical closure under iterative retrieval.

---

## IV. Consequence: Invertibility Gap in Memory Theory

| Process                     | Formal Counterpart   | Problem                            |
| --------------------------- | -------------------- | ---------------------------------- |
| Encoding                    | $f:A\to B$              | Defined (single-valued)            |
| Retrieval                   | $R^{-1}:B\to A$         | Exists but not inverse of encoding |
| Context drift / cue overlap | Expansion / collapse | Unlinked operators                 |
| Feature comparison          | Refinement           | Implicit, not formalized           |
| Re-encoding                 | Composition          | Not guaranteed                     |

**Result:**  Retrieval in current memory models is an *inverse-like heuristic*, not a mathematically defined inverse under expansion and collapse.
The system lacks a formal mapping from encoding to retrieval that preserves composability and invertibility.

---

## V. Implications for Cognitive Theory

1. **Encoding–retrieval asymmetry** is structural, not empirical — caused by missing lemmas (A3–A6).
2. **Forgetting and interference** correspond to *non-invertibility* due to uncontrolled collapse.
3. **REM’s likelihood normalization** can be reinterpreted as a partial implementation of Lemma A6 (unit refinement).
4. A **unified operator model** would require explicit definitions for expansion, collapse, and refinement as morphisms ensuring partial invertibility.

---

## VI. Toward a Unified Operator Framework for Memory

The full operator chain should be:

$$\text{Expand} \to \text{Encode} \to \text{Collapse} \to \text{Retrieve} \to \text{Refine}$$

and only if these operators are explicitly defined does the model become self-consistent.

**Theoretical Insight:**

> Cognitive memory models implicitly assume they live in a well-behaved product space $\text{Item}\times\text{Context}$, but without Lemmas A3–A6, that product space is *incomplete*.
> The gap lies in the undefined mappings that make encoding and retrieval inverses under contextual transformation.

---

### Summary Visualization (Conceptual Flow)

```
Encoding (Function)     →   Expansion (Context Drift)
                                  ↓
                          Collapse (Cue Overlap)
                                  ↓
Retrieval (Inverse Relation)  →  Refinement (Feature Alignment)
                                  ↓
                        Aggregation (Global Decision)
```

**Gap:** No formal operator linking Expansion ↔ Collapse ↔ Refinement → true Inversion.

---

**In short:**
Your lemma chain exposes the formal mathematical backbone missing in memory models — the bridge between functional encoding, relational retrieval, and context transformation.
This defines the *product-space gap* in current cognitive memory theory.
