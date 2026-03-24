I really appreciate the feedback you sent; it mattered a lot to me. After some more thinking and a discussion with my measure-theory colleague throughout last week, I started to formalize the ideas more concretely in mathematical language, and I found that some of this thinking actually aligns very closely with the Criss and Malmberg result you just shared—that the “content” dimension must be formally decomposed into multiple subspaces (physical vs. semantic) because recognition is sensitive to one and recall to the other. This fits very naturally with the orthogonal distance-decomposition framework that I reached this week (content, context, time), and your note helped clarify parts of the structure in a way I hadn’t explicitly articulated before.

To make the setup precise, I am currently assuming a metric-space formulation. The world still begins with a sample space (Ω, 𝔽). Here is the structure as I’m defining it:

• **Content (items)**: samples in Ω. These samples can be expanded into a topological vector space (any general form of vector space) so that similarity or discriminability in content can be computed. REM is an example of important use of such an expansion, because it explicitly constructs a high-dimensional feature representation that allows differentiation (I have some thoughts about this at the end of the email).

• **Context**: the measure μ on Ω. Context lives in the space of measures (the collection of all measures).

• **Time**: a separate axis T. Time remains separate right now merely because mathematically it is usually treated as the index set of a stochastic process rather than part of the state space. It behaves like an orthogonal dimension with its own special structure.

Under this setup, we obtain three orthogonal (or partially orthogonal) sources of discriminability:

- distance in content (from the expanded vector space)
    
- distance in context (from differences between measures μ)
    
- distance in time (from separation along T)
    

Time should be orthogonal to both content and context; content and context may be partially orthogonal, and this needs more discussion, but your physical-feature manipulation in the WFE results strongly suggests possibility of near-orthogonality.

This makes it natural to define total discriminability as the orthogonal sum of squares of the distance components:

d_total² = d_content² + d_context² + dassuming a metric-space formulation. The world still begins with a sample space (Ω, 𝔽). Here is the structure as I’m defining it:

• ￼￼Content (items)￼￼: samples in Ω. These samples can be expanded into a topological vector space (any general form of vector space) so that similarity or discriminability in content can be computed. REM is an example of important use of such an expansion, because it explicitly constructs a high-dimensional feature representation that allows differentiation (I have some thoughts about this at the end of the email).

• ￼￼Context￼￼: the measure μ on Ω. Context lives in the space of measures (the collection of all measures).

• ￼￼Time￼￼: a separate axis T. Time remains separate right now merely because mathematically it is usually treated as the index set of a stochastic process rather than part of the state space. It behaves like an orthogonal dimension with its own special structure.

Under this setup, we obtain three orthogonal (or partially orthogonal) sources of discriminability:

- distance in content (from the expanded vector space)
    
- distance in context (from differences between measures μ)
    
- distance in time (from separation along T)
    _time²

This is the ordinary decomposition of a distance in a product space into squared components along each axis, and it matches the intuition that each dimension contributes independently to discriminability.

There is also a structural relationship between content and context/time. Let us define the events as a sequence indexed by context/time i ∈ T. Thus, for each moment i, we have a state (Xᵢ, i) where Xᵢ ∈ Ω.

1. **Global matching:**  
    Under global matching, the pairs (X₁, 1) and (X₂, 2) could be collapsed to X₁ and X₂.  
    The context/time index is discarded, and X₁ must be different from X₂ for the system to distinguish them.
    
2. **Recollection:  
    **Under recollection, the full pair (Xᵢ, i) must be preserved.  
    Thus (X₁, 1) ≠ (X₂, 2), and X₁ may be equal to or different from X₂ as elements of Ω.  
    The distinction comes from the time/context index, which remains part of the representation.
    

This gives a clearer mathematical representation of the Criss–Malmberg pattern:

1. **For Recognition (Probe-Dependent)**, we can resolve the paradox by decomposing the content distance into orthogonal subspaces, where d_content² = d_physical² + d_semantic². If we assume the WFE relies on density structure within the physical subspace, the disappearance of the effect in your mismatched condition becomes a geometric necessity. Because the probe does not match the trace's form, d_physical is maximized, creating a massive distance that swamps the subtle physical distinctiveness signals that normally drive the WFE. This forces the system to rely entirely on d_semantic to make the recognition decision, and since the semantic dimension is frequency-neutral, the WFE vanishes even though accurate recognition is still possible
    
2. **Recall (Context-Dependent):** Recall, however, avoids this collapse because it operates via the orthogonal d_context dimension (Time/Measure) rather than relying on a physical probe. The retrieval operator searches the measure space for a temporal coordinate, bypassing the format mismatch entirely. Consequently, once the trace is located via context, its intrinsic physical distinctiveness is preserved, explaining why the WFE re-emerges in free recall even when it vanishes in mismatched recognition.
    

I’m still progressing on thinking through the details and how to incorporate other processes, but I think this could be a reasonable starting structure. The distinction between collapsing the measure (global matching) versus preserving the full product space (recollection/positional coding) seems to offer exactly the kind of structural explanation your results point toward. I would love to know whether this decomposition matches how you think about the structural differences in the general theory.

  

---

As a separate side note (and this connects to your wave analogy as well), I feel these differences integrate naturally into the same framework if we view them geometrically in understanding REM. Here are how I think REM differs from the more traditional global-matching models:

• **First**, REM uses a geometric distribution instead of a Gaussian — relying on the 'fat tail' of geometric distribution. The geometric has a heavy tail; the Gaussian does not. This heavy tail produces stronger differentiation because rare, high-match features contribute disproportionately. A Gaussian-like code would compress such differences, but the geometric distribution magnifies them. The "fat tail" creates a non uniform metric. It allows the model to ignore noise and lock onto specific "diagnostic" features.

• **Second**, REM introduces differentiation by replacing the simple dot product with a **weighted dot product**. I learned that this is mathematically a c**hange of metric** or **anisotropic scaling** (stretching different axes by different amounts). A simple dot product (old models) only scales the magnitude of the vector. A weighted dot product effectively rotates the vector inside the content subspace because different feature dimensions receive different weights. This rotation changes the direction of the content vector, not just its length, and that directional change is exactly what creates differentiation in REM. Traditional global matching cannot do this because the similarity operator only stretches the vector without altering its orientation.

In my mind, all of this relates to how the content space itself is structured—whether we treat it as a high-dimensional vector space or more abstractly as a metric space—and how weighted dot-product operations should be expressed in the distance-decomposition framework above. REM uses a high-dimensional feature representation to achieve the differentiation it needs, which is the innovation addup on the tradiational global matching models. 

The “weighted product” in REM is effectively defining a weighted distance metric on the expanded **content** space d_REM²(P, T) = Σᵢ αᵢ (pᵢ − tᵢ)². And the point here is that REM still bases its computations almost entirely on content-distance, even though the weighting introduces differentiation that simple global-matching models cannot produce. 

Best,  
Lea