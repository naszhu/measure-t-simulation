# Goal Representations as Memory: A Unified Framework Perspective

---

## Slide 1: What Is Memory? (The Core Operator)

**Memory = binding between *what* (content) and *when/where* (context)**

Basic equation across all memory models:

$a(i|\text{cue}) = f_i^T W \psi(\text{cue})$

$W = \sum_{t=1}^{T} \gamma_t f_t \otimes \psi_t$

**Components:**
- $f_t$: content feature (the "what" - an item, a word, a stimulus)
- $\psi_t$: context feature (the "when/where" - temporal position, environmental context)
- $W$: memory operator (binds content to context)
- $\gamma_t$: encoding strength

**The retrieval process:**
1. Present a cue at test
2. Project it through $W$ to reactivate content
3. Content that matches both item features AND context wins

---

## Slide 2: Three Ways to Combine Context and Content

The key architectural choice: How do we relate context and content?

### **1. Product Space** (Separable)

$W = \sum_t f_t \otimes \psi_t \quad \text{(outer product)}$

$a_i = \sum_t \langle f_i, f_t \rangle \times \langle \psi_{\text{cue}}, \psi_t \rangle$

- Context and content are **independent dimensions**
- Memory stores their association as a matrix
- Examples: OSCAR (oscillatory phases), Burgess & Hitch (position markers)
- **Good for:** Serial order, positional precision
- **Bad for:** Requires discrete context codes, can't explain contiguity effects

### **2. Embedded Space** (Fused)

$\psi_t \to E(\psi_t) \text{ maps into item space}$

$a_i = \langle f_i, E(\psi_{\text{cue}}) \rangle$

- Context and content **merged into one representation**
- No separate binding operator needed
- Examples: SIMPLE (log-time embedding), EBRW (exemplar similarity)
- **Good for:** Temporal distinctiveness, recognition
- **Bad for:** Can't represent serial order or dependencies

### **3. Joint Embedding** (Co-evolving)

$\psi_{t+1} = \rho\psi_t + \eta f_t \quad \text{(context drifts with items)}$

$W = \sum_t f_t \otimes \psi_t$

- Context **accumulates traces of past items**
- Retrieval reinstates dynamic history
- Examples: TCM (Temporal Context Model)
- **Good for:** Contiguity, forward asymmetry
- **Bad for:** No explicit positional code

---

## Slide 3: Where Does MIS Fit?

**MIS intention representation:** $I = [S, R, G]$
- S = Stimulus feature
- R = Response feature  
- G = Goal state

**Key question:** Which is context, which is content?

### **My interpretation:**
- **Goal (G)** = **context** (defines the task frame, what's relevant now)
- **Stimulus-Response (S, R)** = **content** (the specific intention/action)

**Rewriting MIS in operator notation:**

$a_i = [S_i, R_i]^T \times W_G$

where $W_G$ should represent stored goal-action bindings

**But in current MIS:**
- No stored $W$ operator
- Activation is **direct sum**: $a_i = \sum_k B_k \times \omega_i \times \psi_i(k)$
- This is **factorized embedding** (or **direct-sum space**)

---

## Slide 4: What "Factorized Embedding" Means

**Factorized = separable into independent components**

$\text{MIS activation} = \sum_k (\text{component}_k \text{ weight} \times \text{intention strength} \times \text{component match})$

**Key properties:**
1. **No storage operator ($W$):** Intentions compete based on current activation, not retrieval from memory
2. **Parallel activation:** All components contribute simultaneously
3. **Context-free:** No temporal binding or sequential dependencies

**This means MIS currently models:**
- ✓ Competition among **active** intentions
- ✗ Retrieval from **stored** goal memories
- ✗ How goals are encoded with context
- ✗ How goals are reinstated later

**Comparison to memory models:**

| Property | TCM (episodic) | SIMPLE (episodic) | MIS (goals) |
|----------|----------------|-------------------|-------------|
| Storage operator W | ✓ | ✗ (embedded) | ✗ |
| Context-content binding | ✓ Product space | ✓ Temporal embedding | ✗ Direct sum |
| Retrieval process | Reinstate past context | Distance-based similarity | Parallel activation |
| Memory trace | Stored associations | Temporal coordinates | *No explicit trace* |

---

## Slide 5: Where Does MIS Fit in the Full Process?

**The complete goal cognition pipeline:**

```
1. LTM Storage → 2. Retrieval (LTM→WM) → 3. Selection/Competition (WM) → 4. Action
```

**MIS models step 3: Selection among already-active intentions**

This positioning clarifies several things:

| Question | Answer | Implication |
|----------|--------|-------------|
| Why capacity limited? | WM bottleneck between steps 2→3 | Only N intentions fit in WM after retrieval |
| Why competition-based? | Multiple retrieved intentions need selection | Biased competition resolves conflict |
| Why no storage operator? | Storage happens in step 1 (LTM) | MIS operates post-retrieval |
| What activates intentions? | Step 2 (retrieval) - *not modeled by MIS* | Gap: how do goals enter WM? |

**This means MIS is:**
- ✓ A goal **selection** model (the "last process" before action)
- ✗ Not a goal **memory** model (doesn't model storage or retrieval)
- ✗ Not a goal **retrieval** model (assumes intentions are already active)

**The missing piece:** How do goals move from LTM → WM? (Step 2)
- What triggers retrieval?
- What contexts activate which goals?
- How does retrieval compete with encoding new goals?

---

## Slide 6: Implications for Goal Representation

**What this framework reveals:**

**Current state of goal memory research:**
- We have good models of goal **selection** (like MIS)
- We lack models of goal **memory** (storage, retrieval, interference)

**What a true goal memory model would need:**
1. **Encoding:** How are goal-action bindings formed?
   - When I learn "in context X, do action Y to achieve goal Z"
   
2. **Storage:** How are they maintained?
   - Multiple goal structures in memory
   - Organized by task context, temporal structure, hierarchical relationships

3. **Retrieval:** How are they reactivated?
   - Context cues (task switch, environmental trigger)
   - Goal-based retrieval vs. stimulus-based retrieval

**MIS's strength:** Models competition after goals are active

**MIS's opportunity:** Extend backward to explain how goals become active through memory retrieval

---

## Slide 6: Retrieval Architecture Determines Memory Space

**Key insight:** The retrieval process defines what kind of space we're in

**How you retrieve determines what you can store:**

| Retrieval mechanism | Memory space | What it affords | What it costs |
|---------------------|--------------|-----------------|---------------|
| **Full product:** $\langle f_i, f_t \rangle \times \langle \psi_{\text{cue}}, \psi_t \rangle$ | Product space | Serial order, positional codes | Requires discrete context markers |
| **Temporal embedding:** $e^{-c|\log t - \log t_i|}$ | Embedded manifold | Scale invariance, distinctiveness | Can't represent dependencies |
| **Drifting context:** Project through $\sum f_t \otimes (\rho^k \psi_0 + \sum \eta f_j)$ | Joint space | Contiguity, forward asymmetry | Complex dynamics |
| **Direct activation:** $\sum B_k \times \text{match}(\text{component}_k)$ | Factorized/direct-sum | Parallel processing, component independence | No stored associations |

**For MIS:**
- Current retrieval = weighted sum of component matches
- No context reinstatement
- Suggests goals are not retrieved from memory but assembled/activated in working memory

---

## Slide 8: The 3-Component Structure: Context vs Content

**In MIS:** Intention $I = [S, R, G]$

**From a memory perspective:**

| Component | Function in MIS | Memory classification | Why? |
|-----------|-----------------|----------------------|------|
| **G (Goal)** | Task state, defines relevance | **Context** | - Frames what's relevant<br>- Not retrieved itself<br>- Gates other components |
| **S (Stimulus)** | Environmental input | **Content** | - The "what" that gets bound<br>- Retrieved/activated |
| **R (Response)** | Motor output | **Content** | - The action bound to stimulus<br>- Part of the retrieved association |

**This suggests:**
- Goal (G) = retrieval cue/context
- S-R pair = content being retrieved
- MIS models: "Given goal context G, which S-R pairs are active?"

**But without a storage operator:**
- How did the S-R-G bindings get there?
- What happens when goals change?
- How do we learn new goal structures?

---

## Slide 9: The Capacity Question

**MIS assumes limited capacity** (typically 3-5 intentions in WM)

**Current justification:**
- Working memory capacity limits (Cowan, 2001: ~4 chunks)
- Intentions compete for a limited resource
- Parallels with multi-tasking costs

**But from memory framework perspective:**

**Question 1:** Is the capacity limit in...
- **Storage:** How many goal structures exist in memory? (likely unlimited)
- **Activation:** How many can be active at once? (this is MIS's claim)
- **Retrieval:** How many can be accessed given a cue? (depends on cue specificity)

**Question 2:** What constrains activation capacity?
- If inputs can't arrive simultaneously → no need to discuss capacity?
- Or is there interference among active intentions independent of input timing?

**Comparison to memory models:**
| Model | Capacity assumption | Constraint source |
|-------|---------------------|------------------|
| TCM/OSCAR | Unlimited storage, limited by interference | Similarity and temporal degradation |
| Cowan (2001) | ~4 chunks in WM | Attention-based activation |
| MIS | Limited active intentions | ??? Needs stronger justification |

**Discussion point:** Is capacity limit about:
- Parallel processing bottleneck?
- Interference during retrieval?
- Maintenance cost?

---

## Slide 10: Serial vs Parallel, Familiarity vs Recall

**In memory models, these map to architecture:**

### **Serial vs Parallel:**
- **Serial models** (TCM, positional models): One-at-a-time retrieval, chaining
- **Parallel models** (SIMPLE, REM): All items evaluated simultaneously

**MIS appears parallel:**
- All intentions compete simultaneously
- Activation computed in parallel for each
- Stochastic selection based on relative strength

**But:** Is goal retrieval parallel or serial?
- Activating goals from memory might be serial
- Competition among active goals is parallel

### **Familiarity vs Recall:**
- **Familiarity:** Strength-based recognition (single process)
- **Recall:** Regenerate content from context (two-stage)

**MIS seems familiarity-based:**
- Intentions "feel" more or less active
- Selection based on activation strength
- No reconstruction process

**But:** What about goal recall?
- "What was I doing?" = goal retrieval/reconstruction
- Different from "which goal is most active now?"

---

## Slide 11: Connections to Decision Making

**Poisson race models in both domains:**

**In decision making (Merkle & Van Zandt, 2006):**
- Evidence accumulation as Poisson processes
- First to threshold wins
- Models confidence based on race dynamics

**In MIS:**
- Intention activation as racing processes
- Selection when one crosses threshold
- Parallels to sequential sampling models

**Opportunity:**
- Use Poisson race framework more explicitly
- Connect goal selection to evidence accumulation literature
- Model confidence/commitment to selected goals

**Key insight from Merkle & Van Zandt:**
- Post-decision confidence reflects race state
- Applies to: "How sure am I this is the right goal?"

---

## Slide 12: Collaboration Directions

### **1. Formalize goal memory using context × content framework**

**What this adds to MIS:**
- Explicit encoding mechanism (how S-R-G bindings form)
- Storage operator W_goal for long-term goal structures
- Retrieval process that precedes competition

**Questions to explore:**
- What is the context for goal memories? (task state, temporal, spatial?)
- How do goals get reinstated from memory?
- What causes goal interference at retrieval vs. competition?

---

### **2. Better justify capacity limits**

**Current gap:** Limited capacity seems assumed rather than derived

**What we need:**
- Distinguish storage capacity (unlimited?) from activation capacity (limited)
- Mechanistic account of what constrains active intention count
- Connection to working memory theories (Cowan, Oberauer, etc.)

**Possible approaches:**
- Resource competition model (shared activation pool)
- Interference-based limit (cross-talk among intentions)
- Retrieval constraint (only N goals can be cued simultaneously)

**Critical question:** If intentions arrive sequentially (not all at once), is the capacity limit about:
- Processing bandwidth?
- Maintenance cost?
- Something else?

This needs stronger theoretical grounding than "WM has limited capacity."

---

### **3. Extend to goal memory phenomena**

**Current MIS explains:**
- Goal shielding
- Task switching costs
- Intention competition

**Goal memory phenomena to add:**
- **Prospective memory:** Retrieving delayed intentions
- **Goal interference:** Similar goals in memory competing
- **Goal learning:** Acquiring new goal-action bindings
- **Hierarchical goals:** Parent goals as context for subgoals

**These require:**
- Explicit memory storage (not just active competition)
- Temporal/contextual encoding
- Retrieval cues beyond current stimulus

---

### **4. Bridge to Poisson race models**

**Opportunity:**
- Make Poisson dynamics more explicit in MIS
- Connect to sequential sampling framework
- Model confidence/commitment to selected goals

**Relevant work:**
- Merkle & Van Zandt (2006): Poisson races for confidence
- Ratcliff diffusion model: Could parallel race dynamics
- LCA (Usher & McClelland): Lateral inhibition in races

**Questions:**
- How do stopping rules differ for goal selection vs. perceptual decisions?
- What role does urgency play in intention selection?

---

## Slide 13: Summary & Next Steps

**What we've established:**
1. **Memory models** distinguish context × content with different binding architectures
2. **MIS classification:** Factorized embedding / direct-sum space
   - Models parallel competition, not memory storage/retrieval
3. **MIS as "last process":** Selection step (WM competition) before action
   - Explains why: capacity limited, competition-based, no storage operator
4. **Missing steps:** Encoding (how S-R-G bindings form) and retrieval (LTM → WM)

**Key insights:**
- MIS models what happens AFTER goals are retrieved into WM
- The framework reveals MIS is a selection model, not a memory model
- Capacity limits make sense for WM selection, but need better justification

**Discussion priorities:**
1. Does framing MIS as "the last process" (post-retrieval selection) fit your view?
2. What would goal retrieval (LTM → WM) look like?
3. How do goals get encoded? (instruction, planning, learning, inference)
4. Interest in formalizing the encoding → storage → retrieval steps using context × content operators?

**Next steps:**
- Model the full pipeline: $W_{\text{goal}}$ (LTM storage) → retrieval dynamics → MIS competition
- Distinguish capacity limits at different stages (storage unlimited, WM limited)
- Test predictions about goal encoding, interference, and prospective memory

---

Thank you! Let's discuss.
