[[Source Memory]]
# Differential Resolution in Content and Context:

# A Kernel Density Model of Item and Source Memory

## DRAFT — Core Idea and Background

---

## 1. Introduction

### 1.1 The Problem

Episodic memory is memory for personally experienced events, and every event has two aspects: _what happened_ (content) and _the circumstances under which it happened_ (context — where, when, how, from whom). A fundamental empirical fact about episodic memory is that these two aspects are not remembered equally well. People routinely remember encountering an item while failing to remember the source, context, or circumstances of that encounter. You remember the fact but not whether you read it in a newspaper or heard it from a friend. You recognize the face but cannot remember where you met the person. You know the word was on the list but not which list.

This asymmetry — reliable item memory paired with unreliable source memory — is one of the most robust phenomena in the episodic memory literature. It has been documented across dozens of paradigms and populations (Johnson, Hashtroudi, & Lindsay, 1993; Mitchell & Johnson, 2009). Yet existing theoretical accounts of this asymmetry fall into two camps that are each unsatisfying in different ways. Dual-process theories explain the asymmetry by positing two qualitatively different retrieval processes. Signal detection theories explain it by fitting different parameters to different conditions. Neither camp offers a _structural_ account — one that derives the asymmetry from the representational format of the memory trace itself.

This paper proposes such an account. The model is simple: memory traces are represented as kernel density contributions to a joint probability measure over content and context spaces, and the kernel bandwidth (resolution) differs between the two spaces. Content is stored at high resolution (narrow bandwidth); context is stored at low resolution (broad bandwidth). Different memory tasks — item recognition, source memory, and recall — correspond to different mathematical operations on this joint measure: marginalization, conditional discrimination, and conditional sampling, respectively. The item-source asymmetry is a necessary consequence of the differential bandwidth, not a free parameter adjusted to fit each task separately.

The model makes specific, falsifiable predictions — including one surprising crossover interaction — that distinguish it from both dual-process and equal-variance signal detection accounts.

### 1.2 What Is Source Memory?

Source memory refers to memory for the contextual attributes of an encoding episode, as distinct from memory for the item or event itself (Johnson et al., 1993). In a typical source memory experiment, participants study items from two (or more) sources — for example, words spoken by a male versus female voice (Glisky, Polster, & Routhieaux, 1995), words presented in red versus green font (Lindsay & Johnson, 2000), or words studied in one of two spatial locations (Murnane & Phelps, 1993). At test, participants first make an old/new recognition judgment (item memory) and then, for items judged "old," indicate the source (source memory).

The consistent finding is that item recognition accuracy is substantially higher than source memory accuracy. This dissociation holds across age groups (older adults show disproportionate source memory deficits; Glisky et al., 1995; Spencer & Raz, 1995), across clinical populations (frontal lobe patients show impaired source memory with relatively intact item recognition; Janowsky, Shimamura, & Squire, 1989), and across encoding manipulations (divided attention at encoding harms source memory more than item memory; Troyer & Craik, 2000).

Source memory is not a peripheral topic — it is at the heart of what makes episodic memory _episodic_. Tulving (1983, 2002) defined episodic memory precisely as memory for events bound to their spatiotemporal context. If you strip away the contextual binding — the "when and where" — what remains is semantic memory (knowing facts without knowing when or how you learned them). Source memory failure is therefore the boundary between episodic and semantic memory: it is the process by which episodic memories degrade into semantic ones.

### 1.3 Why Existing Theories Are Incomplete

The two dominant theoretical frameworks handle the item-source asymmetry in different ways, each with characteristic limitations.

---

## 2. Background: Theoretical Accounts of Item and Source Memory

### 2.1 The Dual-Process Framework

The most influential account of the item-source dissociation is the dual-process theory developed by Yonelinas and colleagues (Yonelinas, 1994, 1999, 2002; Yonelinas & Parks, 2007). The theory proposes that recognition memory is supported by two qualitatively distinct processes:

**Familiarity** is a fast, automatic signal that provides a sense of prior occurrence without contextual detail. It is modeled as a continuous, Gaussian signal-detection process. Familiarity supports item recognition: you know you have seen the word before, but you do not recover any details about the study episode.

**Recollection** is a slower, effortful process that recovers specific contextual details from the study episode — the source, the temporal position, associated thoughts. It is modeled as a threshold process: either you recollect (and recover source information) or you do not.

Under this framework, the item-source asymmetry has a straightforward explanation: item recognition can succeed on the basis of familiarity alone, whereas source memory requires recollection. Since recollection is a threshold process that sometimes fails entirely, source memory is naturally less reliable than item recognition.

The dual-process theory has been enormously productive. It explains asymmetric ROC curves in recognition (Yonelinas, 1994), the disproportionate effect of aging on source memory (Yonelinas, 2002), and dissociations between "remember" and "know" judgments (Tulving, 1985; Gardiner, 1988).

However, the theory has been challenged on several grounds:

First, the claim that recollection is a threshold process (all-or-none) has been contested. Mickes, Wais, and Wixted (2009) showed that source memory ROC curves are curved, not linear, suggesting that source memory is based on a continuous signal rather than a threshold. Wixted (2007) and Wixted and Mickes (2010) argued that both item and source memory reflect continuous signal-detection processes, differing only in signal strength. If this is correct, the qualitative distinction between familiarity and recollection dissolves, and the dual-process explanation of the item-source asymmetry loses its structural foundation.

Second, the theory does not specify _why_ recollection fails when it does. The threshold is a descriptive parameter, not a mechanistic explanation. What determines whether recollection succeeds or fails for a given item? The theory does not derive this from the structure of the memory representation — it simply posits that recollection is probabilistic.

Third, the theory has difficulty explaining continuous variation in source memory quality. Source memory is not all-or-none in practice: participants can sometimes partially recover source information, reporting confidence that varies continuously (Slotnick & Dodson, 2005). A threshold process predicts bimodal distributions of source accuracy; continuous distributions are more naturally accommodated by signal-detection models.

### 2.2 Signal Detection Approaches

The competing framework treats both item and source memory as continuous signal-detection processes (Wixted, 2007; Wixted & Mickes, 2010; DeCarlo, 2003; Banks, 2000).

Under this approach, item recognition and source memory both involve comparing a continuous evidence variable to a criterion. The key difference is that source memory has lower signal-to-noise ratio (lower d') than item recognition, because source-diagnostic information is weaker or noisier than item-diagnostic information.

This framework can accommodate curved ROC functions for both item and source memory (Mickes et al., 2009), and it does not require two qualitatively different processes. It is more parsimonious than the dual-process theory.

However, it has its own limitation: it does not explain _why_ source d' is lower than item d'. The claim that "source information is weaker" is a restatement of the empirical finding, not a derivation from representational principles. What about the structure of memory representations makes source information inherently weaker? The signal detection framework, as typically formulated, treats d' as a free parameter estimated separately for each condition. It describes the asymmetry but does not explain it.

### 2.3 Global Matching Models

A third tradition approaches recognition memory through global matching models: MINERVA 2 (Hintzman, 1984, 1988), SAM (Gillund & Shiffrin, 1984), TODAM (Murdock, 1982), and REM (Shiffrin & Steyvers, 1997).

In these models, each memory trace is a vector of features. At test, a probe is compared simultaneously to all stored traces, and the aggregate match signal (echo intensity, likelihood ratio, or summed similarity) drives the recognition decision.

Global matching models can address source memory by including context features in the trace vector. A source judgment then requires matching on context features specifically, while an item judgment matches on content features (or on the full vector). Clark (1992) and Riefer, Hu, and Batchelder (1994) explored such extensions.

However, standard global matching models treat all features symmetrically — there is no principled reason why context features should be stored less precisely than content features. If context features are simply given lower weights, this amounts to the same descriptive strategy as signal detection (fitting different parameters for different tasks). The architectural question remains: what about the structure of encoding makes context inherently lower-resolution?

### 2.4 Context Models: TCM and Successors

The Temporal Context Model (TCM; Howard & Kahana, 2002) and its variants (Howard, Fotedar, Datey, & Hasselmo, 2005; Polyn, Norman, & Kahana, 2009; Lohnas, Polyn, & Kahana, 2015) provide a specific mechanism for how context evolves during study. Context is a vector that drifts gradually as new items are encoded, with each new item partially updating the context representation.

TCM naturally produces the finding that nearby items in a list tend to be recalled together (the contiguity effect), because their context vectors overlap. It also provides a mechanism for source memory: source discrimination requires distinguishing between contexts that may have drifted only slightly from each other.

The insight from TCM that is most relevant to the present model is that context is inherently more confusable than content. Item vectors are drawn independently from a feature distribution and can be highly distinctive. Context vectors, by contrast, evolve through a slow drift process, meaning that temporally adjacent contexts are highly similar. This built-in similarity structure in context space creates an inherent resolution disadvantage for source-level discrimination.

However, TCM does not formalize this intuition as a bandwidth difference, and it does not derive the specific quantitative relationships between item and source memory that follow from a formal treatment of resolution.

### 2.5 The Dennis and Humphreys Context Noise Model

Dennis and Humphreys (2001) proposed a model in which recognition memory is limited by context noise rather than item noise. In their model, the primary source of interference in recognition is not similarity between the target and other items (item noise), but rather similarity between the current test context and the various contexts in which the target was previously encountered (context noise).

This model makes a strong prediction: list-length effects should be small or absent in item recognition, because adding more items to a list adds item noise but not context noise. This prediction has received some empirical support (Dennis & Humphreys, 2001; Dennis, Lee, & Kinnell, 2008), though the evidence is debated (Kinnell & Dennis, 2011; Malmberg & Murnane, 2002).

The context noise model is relevant to the present framework because it explicitly distinguishes the representational structure of content and context. However, it does not formalize the distinction as a bandwidth or resolution difference, and it does not address source memory specifically.

### 2.6 Summary: The Theoretical Gap

Across these traditions, a common pattern emerges: every account of the item-source asymmetry either (a) posits two qualitatively different processes (dual-process theory), (b) fits different parameters to different conditions without explaining why the parameters differ (signal detection), or (c) builds in context confusability informally without deriving its consequences quantitatively (TCM, context noise models).

What is missing is a model that:

1. Uses a single retrieval mechanism (not two processes)
    
2. Derives the item-source asymmetry from the representational structure of the memory trace
    
3. Specifies the quantitative relationship between item and source memory as a function of a structural parameter
    
4. Generates novel, testable predictions that distinguish it from existing accounts
    

The present model aims to fill this gap.

---

## 3. The Model

### 3.1 Core Representational Assumption

Each studied event contributes a kernel density to a joint probability measure over content space F and context space Ψ:

$$\mu_{study}(f, \psi) = \sum_{t=1}^{N} \gamma_t \cdot K_{\sigma_f}(f, f_t) \cdot K_{\sigma_\psi}(\psi, \psi_t)$$

where:

- $f_t \in \mathcal{F}$ is the content representation of item $t$
    
- $\psi_t \in \Psi$ is the context representation at encoding time $t$
    
- $K_{\sigma}(x, y)$ is a kernel function (e.g., Gaussian) with bandwidth $\sigma$: $$K_{\sigma}(x, y) = \frac{1}{(2\pi\sigma^2)^{d/2}} \exp\left(-\frac{|x - y|^2}{2\sigma^2}\right)$$
    
- $\gamma_t$ is the encoding strength at time $t$
    
- $\sigma_f$ is the bandwidth (resolution) in content space
    
- $\sigma_\psi$ is the bandwidth (resolution) in context space
    

**The single structural assumption:**

$$\sigma_f < \sigma_\psi$$

Content is stored at higher resolution (narrower bandwidth) than context.

### 3.2 Why σ_f < σ_ψ: Justification

This assumption is not arbitrary. It reflects a structural asymmetry between content and context that multiple lines of evidence support:

**From TCM:** Context vectors are generated by a slow drift process ($\psi_{t+1} = \rho \psi_t + \eta f_{t+1}$). Because $\rho$ is close to 1, successive context vectors are highly correlated. Item vectors, by contrast, are drawn relatively independently. High inter-item correlation in context space is mathematically equivalent to broad bandwidth: the "effective kernel" that context occupies in representational space is wide because adjacent contexts overlap substantially.

**From the neuroscience of context:** Hippocampal time cells and place cells provide the neural substrate for context representation. These cells have broad tuning curves — each cell fires over an extended temporal window or spatial region (MacDonald, Lepage, Eden, & Bhatt, 2011; Eichenbaum, 2014). Broad tuning is, in the kernel density framework, a wide bandwidth.

**From everyday phenomenology:** The subjective experience of "remembering the item but not the source" is so common as to be unremarkable. The reverse — remembering the source but not the item — is rare and striking. This asymmetry is consistent with content being represented at higher resolution than context.

**From encoding specificity research:** Encoding specificity effects (Tulving & Thomson, 1973) demonstrate that memory is sensitive to context, but the sensitivity is partial and graded — performance degrades smoothly as context changes, rather than collapsing entirely. Smooth degradation is the signature of a broad kernel: a narrow kernel would produce sharp, all-or-none context dependence.

### 3.3 Retrieval Operations

Different memory tasks correspond to different mathematical operations on the joint measure $\mu_{study}$.

#### 3.3.1 Item Recognition: Marginalization Over Context

Item recognition asks: "Was this item studied, regardless of source?" The relevant computation marginalizes over all contexts:

$$a_{item}(probe) = \int_{\Psi} \mu_{study}(probe, \psi) \, d\psi = \sum_{t=1}^{N} \gamma_t \cdot K_{\sigma_f}(probe, f_t) \cdot \underbrace{\int_{\Psi} K_{\sigma_\psi}(\psi, \psi_t) \, d\psi}_{= 1}$$

The context kernel integrates to 1 (it is a probability density). Therefore:

$$a_{item}(probe) = \sum_{t=1}^{N} \gamma_t \cdot K_{\sigma_f}(probe, f_t)$$

Item recognition depends only on the content kernel and is independent of $\sigma_\psi$. This is the standard global matching computation.

#### 3.3.2 Source Memory: Conditional Discrimination in Context

Source memory asks: "Given that this item was studied, which source did it come from?" This requires discriminating between contexts conditional on content.

Suppose there are two sources (contexts $\psi_A$ and $\psi_B$). The source judgment compares:

$$a_{source}(A \mid probe) = \frac{\sum_{t \in A} \gamma_t \cdot K_{\sigma_f}(probe, f_t) \cdot K_{\sigma_\psi}(\psi_{test}, \psi_t)}{\sum_{t=1}^{N} \gamma_t \cdot K_{\sigma_f}(probe, f_t) \cdot K_{\sigma_\psi}(\psi_{test}, \psi_t)}$$

Here, the context kernel does NOT integrate out. Source discrimination depends on the ability of $K_{\sigma_\psi}$ to distinguish $\psi_A$ from $\psi_B$. Because $\sigma_\psi$ is large, the kernels centered at $\psi_A$ and $\psi_B$ overlap substantially, and discrimination is poor.

**The item-source asymmetry follows directly:** item recognition depends only on $\sigma_f$ (high resolution, good performance), while source memory depends on $\sigma_\psi$ (low resolution, poor performance). The asymmetry is a structural consequence of the bandwidth difference, not a separate process or a fitted parameter.

#### 3.3.3 Cued Recall: Conditional Sampling from Context

Cued recall asks: "Given this context, what items were studied here?" This conditions on context and samples from content:

$$P(f_i \mid \psi_{cue}) \propto \gamma_i \cdot K_{\sigma_f}(f_i, f_i) \cdot K_{\sigma_\psi}(\psi_{cue}, \psi_i)$$

Recall accuracy depends on BOTH bandwidths: $\sigma_\psi$ determines how selectively the context cue activates the target trace (versus competing traces from other contexts), and $\sigma_f$ determines how discriminable the target is from other items activated by the same context.

#### 3.3.4 Free Recall: Sequential Sampling

Free recall can be modeled as sequential sampling from the context-conditional measure, with each recall updating the context (as in TCM):

$$P(f_i \mid \psi_{current}) \propto K_{\sigma_\psi}(\psi_{current}, \psi_i)$$

After recalling item $i$, context updates: $\psi_{current} \leftarrow \rho \psi_{current} + \eta f_i$. The contiguity effect emerges because items encoded in similar contexts have overlapping $K_{\sigma_\psi}$ kernels.

### 3.4 Discriminability Derivations

For each task, we can derive the discriminability (d') as a function of the two bandwidth parameters.

**Item recognition d':**

For a target item $f_{target}$ versus a lure $f_{lure}$:

$$d'_{item} \propto \frac{K_{\sigma_f}(f_{target}, f_{target}) - \mathbb{E}[K_{\sigma_f}(f_{lure}, f_t)]}{\text{SD of lure distribution}}$$

This depends on $\sigma_f$ and the inter-item distance structure in content space, but NOT on $\sigma_\psi$.

**Source memory d':**

For discriminating source A from source B:

$$d'_{source} \propto \frac{K_{\sigma_\psi}(\psi_A, \psi_A) - K_{\sigma_\psi}(\psi_A, \psi_B)}{\text{SD of source evidence distribution}}$$

For Gaussian kernels:

$$K_{\sigma_\psi}(\psi_A, \psi_A) - K_{\sigma_\psi}(\psi_A, \psi_B) = \frac{1}{(2\pi\sigma_\psi^2)^{d/2}} \left(1 - \exp\left(-\frac{|\psi_A - \psi_B|^2}{2\sigma_\psi^2}\right)\right)$$

When $\sigma_\psi$ is large relative to $|\psi_A - \psi_B|$, the exponential term is close to 1, and the difference is small — source memory is poor.

**The ratio:**

$$\frac{d'_{source}}{d'_{item}} \approx g\left(\frac{|\psi_A - \psi_B|}{\sigma_\psi}\right)$$

where $g$ is an increasing function. Source memory improves relative to item memory when (a) contexts are more distinctive ($|\psi_A - \psi_B|$ increases) or (b) context resolution increases ($\sigma_\psi$ decreases).

### 3.5 The Model in Relation to Existing Frameworks

The model relates to existing theories as follows:

**Versus dual-process theory:** The model uses a single retrieval mechanism (kernel density matching) applied to a single representational structure (the joint measure). There is no qualitative distinction between familiarity and recollection. The item-source asymmetry arises from the geometry of the representation, not from the retrieval process. The model predicts continuously curved ROC functions for both item and source memory (consistent with Mickes et al., 2009), but derives the d' difference from the bandwidth ratio rather than fitting it as a free parameter.

**Versus signal detection theory:** The model IS a signal detection model, but one in which the signal distributions for item and source memory are derived from the same joint kernel density rather than specified independently. The d' values for item and source are yoked — they are both determined by $\sigma_f$ and $\sigma_\psi$, and changing one bandwidth affects both tasks in predictable ways.

**Versus global matching models:** The model IS a global matching model — item recognition is computed as the sum of kernel similarities, exactly as in MINERVA 2 or REM. The extension is the explicit treatment of the content-context joint density and the bandwidth asymmetry.

**Versus TCM:** The model is compatible with TCM's context drift mechanism. TCM provides a generative process for the context vectors $\psi_t$; the present model characterizes the resolution at which these contexts are stored and used for retrieval. The two frameworks are complementary, not competing.

---

## 4. Predictions

The model generates four specific predictions that differentiate it from existing theories.

### 4.1 Prediction 1: List-Length Effect Is Larger for Source Than Item Memory

Adding items to the study list increases the density of traces in the joint measure. Because $\sigma_\psi > \sigma_f$, traces overlap more in context space than in content space. Item recognition, which marginalizes over context, is affected only by overlap in content space — which grows slowly because $\sigma_f$ is small. Source memory, which must discriminate within context space, is affected by overlap in context space — which grows rapidly because $\sigma_\psi$ is large.

**Quantitative prediction:** The list-length effect on source d' should be approximately $(\sigma_\psi / \sigma_f)^{d}$ times the list-length effect on item d', where $d$ is the dimensionality of the representational space.

**Testable against:** Existing list-length data that includes both item and source judgments (e.g., Malmberg & Murnane, 2002, on environmental context; Gruppuso, Lindsay, & Masson, 2007, on source memory). If no existing dataset separates list-length effects for item versus source, this is a straightforward experiment to run.

### 4.2 Prediction 2: Encoding Strength Has a Specific Functional Form

Increasing encoding strength (e.g., through repetition, deeper processing, or longer study time) increases $\gamma_t$ and may also sharpen both bandwidths. If we model encoding strength as uniformly scaling both bandwidths:

$$\sigma_f(strength) = \sigma_{f,0} / h(strength), \quad \sigma_\psi(strength) = \sigma_{\psi,0} / h(strength)$$

then the proportional improvement in d' is greater for source memory (because it starts from a worse baseline at high $\sigma_\psi$) but the absolute level remains lower (because the bandwidth ratio is preserved).

**Prediction:** Plotting d' vs. encoding strength, the source memory curve should be steeper than the item memory curve but should asymptotically approach rather than cross the item memory curve.

**Testable against:** Levels-of-processing data that measures both item and source memory (e.g., Marsh & Hicks, 1998; Troyer & Craik, 2000).

### 4.3 Prediction 3: Context Distinctiveness Helps Source But Hurts Item Recognition

This is the novel, surprising prediction.

Suppose contexts are made more distinctive — for example, studying List A in a red room and List B in a blue room, rather than studying both in the same room. This increases $|\psi_A - \psi_B|$, the inter-context distance.

**Effect on source memory:** Increasing $|\psi_A - \psi_B|$ decreases the overlap between $K_{\sigma_\psi}(\cdot, \psi_A)$ and $K_{\sigma_\psi}(\cdot, \psi_B)$. Source discrimination improves.

**Effect on item recognition:** Item recognition marginalizes over context:

$$a_{item}(probe) = \sum_t \gamma_t \cdot K_{\sigma_f}(probe, f_t) \cdot \int K_{\sigma_\psi}(\psi_{test}, \psi_t) \, d\psi_t$$

Wait — this integration depends on the test context $\psi_{test}$. If the test context matches only one source context (e.g., testing in the red room), then only traces from that source contribute fully to the recognition signal. Traces from the other source (blue room) have reduced context match. The effective number of traces contributing to the recognition signal is reduced.

Under standard global matching, reducing the number of contributing traces has two effects: it reduces the signal (fewer target-trace matches) and it reduces the noise (fewer lure-trace matches). The net effect on d' depends on the signal-to-noise ratio. However, if the test context is neutral (neither red nor blue room), then traces from BOTH sources contribute, but each with reduced context match — the total signal decreases without a corresponding decrease in noise (because lures match neither context).

**The critical case:** When context is distinctive AND the test context is reinstated (matching one source), item recognition for items from the matching source should IMPROVE (better context match, less interference from other-source items). But item recognition for items from the non-matching source should substantially DECREASE.

When context is distinctive AND the test context is neutral (not matching either source), item recognition should DECREASE overall, because each trace's context kernel contributes less (the test context is far from both source contexts in the distinctive condition, whereas it would be close to both in the non-distinctive condition).

**Summary of Prediction 3:**

|Condition|Item d'|Source d'|
|---|---|---|
|Non-distinctive contexts, neutral test|Baseline|Low|
|Distinctive contexts, reinstated test|Improved for matching source|Improved|
|Distinctive contexts, neutral test|**Decreased**|Improved|

The crossover is in the third row: distinctive contexts improve source memory but decrease item recognition when test context is neutral. This is because item recognition benefits from having many traces contribute to the match signal (broad context overlap helps), while source memory benefits from having few traces contribute (narrow context overlap helps).

**Comparison with other theories:**

- **Dual-process theory** predicts that context distinctiveness should improve recollection (helping source memory) and either help or have no effect on familiarity (no mechanism for hurting item recognition). It does not predict the decrease in item d'.
    
- **Standard signal detection** does not make a directional prediction without fitting parameters post hoc.
    
- **The present model** derives the crossover as a necessary consequence of the bandwidth structure.
    

**Testable against:** Murnane and Phelps (1993, 1994, 1995) ran experiments systematically varying environmental context between study and test, measuring both item recognition and context-dependent effects. Their data can be reanalyzed for the crossover pattern. If no existing dataset tests this specific combination (distinctive contexts × neutral test context × both item and source measured), the experiment is straightforward to design.

### 4.4 Prediction 4: Source Memory Forgetting Rate Exceeds Item Memory Forgetting Rate by a Specific Ratio

If forgetting involves diffusion of the kernel (increasing $\sigma$ over time):

$$\sigma_f(t) = \sigma_{f,0} \cdot h(t), \quad \sigma_\psi(t) = \sigma_{\psi,0} \cdot h(t)$$

where $h(t)$ is an increasing function (e.g., $h(t) = \sqrt{1 + \beta t}$), then source memory degrades faster than item memory because it starts from a broader bandwidth. The rate of d' decline is:

$$\frac{d}{dt} d'_{source} \approx \frac{\sigma_\psi}{\sigma_f} \cdot \frac{d}{dt} d'_{item}$$

The ratio of forgetting rates should equal the bandwidth ratio. This is a specific quantitative prediction.

**Testable against:** Forgetting curve data that measures both item and source memory at multiple retention intervals (e.g., Bornstein & LeCompte, 1995; Gruppuso et al., 2007). If the ratio of forgetting rates is constant across retention intervals, this supports the bandwidth model; if the ratio changes, the model would need modification (e.g., differential diffusion rates for content and context).

---

## 5. Relation to the Broader Measure-Theoretic Program

The model presented above can be stated entirely in the language of kernel density estimation, which is familiar to psychologists from nonparametric statistics. No measure theory is required to understand or implement it.

However, the model has a natural interpretation in measure-theoretic terms that opens connections to a broader research program:

The joint kernel density $\mu_{study}(f, \psi)$ IS a probability measure on the product space $\mathcal{F} \times \Psi$. Item recognition IS marginalization of this measure over $\Psi$. Source memory IS conditional discrimination within $\Psi$. Recall IS conditional sampling from $\mathcal{F}$ given $\Psi$. Forgetting IS diffusion (broadening) of the measure.

These are not metaphors; they are the precise mathematical operations that the model performs. The kernel density formulation and the measure-theoretic formulation are notational variants of the same model.

The measure-theoretic perspective becomes useful (rather than merely equivalent) when one asks about the _optimal_ resolution structure. Given the statistical structure of the environment (how items and contexts are distributed), what bandwidth ratio $\sigma_\psi / \sigma_f$ should an ideal memory system use? This question can be formalized as: what measure on the joint space maximizes discriminability under resource constraints? The answer connects to rate-distortion theory (Shannon, 1959) and the information geometry of exponential families (Amari, 1985), and may provide a rational-analysis account (Anderson, 1990; Shiffrin & Steyvers, 1997) of why the human memory system stores context at lower resolution than content.

This extension is left to future work.

---

## 6. Discussion

### 6.1 Summary

The model proposes that the pervasive asymmetry between item and source memory is a structural consequence of differential bandwidth in content and context representations. Content is stored at high resolution (narrow kernel bandwidth), context at low resolution (broad kernel bandwidth). Different memory tasks — recognition, source discrimination, recall — are different mathematical operations on the same joint kernel density. The item-source asymmetry is not a reflection of two different retrieval processes, nor a post-hoc fitting of different parameters. It is a geometric necessity given the bandwidth structure.

### 6.2 Scope and Limitations

The model as presented treats content and context as separable dimensions with independent Gaussian kernels. This is a simplification. In reality, content and context may interact during encoding (e.g., context may affect how content features are weighted, as in the encoding specificity principle). The model can be extended to non-separable kernels, but the separable case is the natural starting point because it generates the clearest predictions.

The model does not specify the dimensionality of the content and context spaces, nor the specific form of the kernel (Gaussian is assumed for tractability). These are parameters that would need to be constrained by data fitting.

The model does not address response time. Extending the model to generate RT predictions would require combining it with an evidence accumulation framework (e.g., a diffusion decision model; Ratcliff, 1978), treating the kernel-derived evidence signal as the drift rate.

### 6.3 What the Model Is and Is Not

The model IS:

- A signal detection model (decisions are based on continuous evidence relative to criteria)
    
- A global matching model (evidence is computed by comparing the probe to all stored traces)
    
- A kernel density model (each trace contributes a kernel to a joint density)
    

The model IS NOT:

- A dual-process model (there is one retrieval mechanism, not two)
    
- A new architecture (the computation is standard global matching with an explicit joint density)
    
- A measure theory tutorial (the measure-theoretic interpretation is available but not required)
    

The contribution is the structural assumption ($\sigma_f < \sigma_\psi$), the derivation of the item-source asymmetry from this assumption, and the specific predictions (especially the crossover in Prediction 3) that follow from the model and distinguish it from existing accounts.

---

## References

[To be completed — key citations listed in text above]

Anderson, J. R. (1990). The adaptive character of thought. Erlbaum. Banks, W. P. (2000). Recognition and source memory as multivariate decision processes. Psychological Science, 11, 267–273. Clark, S. E. (1992). Word frequency effects in associative and item recognition. Memory & Cognition, 20, 231–243. Clark, S. E., & Gronlund, S. D. (1996). Global matching models of recognition memory. Psychonomic Bulletin & Review, 3, 37–60. DeCarlo, L. T. (2003). An application of signal detection theory with finite mixture distributions to source discrimination. Journal of Experimental Psychology: Learning, Memory, and Cognition, 29, 767–778. Dennis, S., & Humphreys, M. S. (2001). A context noise model of episodic word recognition. Psychological Review, 108, 452–478. Eichenbaum, H. (2014). Time cells in the hippocampus. Neuron, 81, 28–32. Gardiner, J. M. (1988). Functional aspects of recollective experience. Memory & Cognition, 16, 309–313. Gillund, G., & Shiffrin, R. M. (1984). A retrieval model for both recognition and recall. Psychological Review, 91, 1–67. Glanzer, M., & Adams, J. K. (1985). The mirror effect in recognition memory. Memory & Cognition, 13, 8–20. Glisky, E. L., Polster, M. R., & Routhieaux, B. C. (1995). Double dissociation between item and source memory. Neuropsychology, 9, 229–235. Gruppuso, V., Lindsay, D. S., & Masson, M. E. J. (2007). I'd know that face anywhere! Psychonomic Bulletin & Review, 14, 1085–1089. Hintzman, D. L. (1984). MINERVA 2: A simulation model of human memory. Behavior Research Methods, Instruments, & Computers, 16, 96–101. Hintzman, D. L. (1988). Judgments of frequency and recognition memory in a multiple-trace memory model. Psychological Review, 95, 528–551. Howard, M. W., & Kahana, M. J. (2002). A distributed representation of temporal context. Journal of Mathematical Psychology, 46, 269–299. Janowsky, J. S., Shimamura, A. P., & Squire, L. R. (1989). Source memory impairment in patients with frontal lobe lesions. Neuropsychologia, 27, 1043–1056. Johnson, M. K., Hashtroudi, S., & Lindsay, D. S. (1993). Source monitoring. Psychological Bulletin, 114, 3–28. Lohnas, L. J., Polyn, S. M., & Kahana, M. J. (2015). Expanding the scope of memory search: Modeling intralist and interlist effects in free recall. Psychological Review, 122, 337–363. Malmberg, K. J., & Murnane, K. (2002). List composition and the word-frequency effect for recognition memory. Journal of Experimental Psychology: Learning, Memory, and Cognition, 28, 616–630. Marsh, R. L., & Hicks, J. L. (1998). Test formats change source-monitoring decision processes. Journal of Experimental Psychology: Learning, Memory, and Cognition, 24, 1137–1151. Mickes, L., Wais, P. E., & Wixted, J. T. (2009). Recollection is a continuous process: Implications for dual-process theories of recognition memory. Psychological Science, 20, 509–515. Mitchell, K. J., & Johnson, M. K. (2009). Source monitoring 15 years later: What have we learned from fMRI about the neural mechanisms of source memory? Psychological Bulletin, 135, 638–677. Murdock, B. B. (1982). A theory for the storage and retrieval of item and associative information. Psychological Review, 89, 609–626. Murnane, K., & Phelps, M. P. (1993). A global activation approach to the effect of changes in environmental context on recognition. Journal of Experimental Psychology: Learning, Memory, and Cognition, 19, 882–894. Murnane, K., & Phelps, M. P. (1994). When does a different environmental context make a difference in recognition? A global activation model. Memory & Cognition, 22, 584–590. Murnane, K., & Phelps, M. P. (1995). Effects of changes in relative cue strength on context-dependent recognition. Journal of Experimental Psychology: Learning, Memory, and Cognition, 21, 158–172. Polyn, S. M., Norman, K. A., & Kahana, M. J. (2009). A context maintenance and retrieval model of organizational processes in free recall. Psychological Review, 116, 129–156. Ratcliff, R. (1978). A theory of memory retrieval. Psychological Review, 85, 59–108. Shiffrin, R. M., & Steyvers, M. (1997). A model for recognition memory: REM—retrieving effectively from memory. Psychonomic Bulletin & Review, 4, 145–166. Slotnick, S. D., & Dodson, C. S. (2005). Support for a continuous (single-process) model of recognition memory and source memory. Memory & Cognition, 33, 151–170. Spencer, W. D., & Raz, N. (1995). Differential effects of aging on memory for content and context. Psychology and Aging, 10, 527–539. Troyer, A. K., & Craik, F. I. M. (2000). The effect of divided attention on memory for items and their context. Canadian Journal of Experimental Psychology, 54, 161–171. Tulving, E. (1983). Elements of episodic memory. Oxford University Press. Tulving, E. (1985). Memory and consciousness. Canadian Psychology, 26, 1–12. Tulving, E. (2002). Episodic memory: From mind to brain. Annual Review of Psychology, 53, 1–25. Tulving, E., & Thomson, D. M. (1973). Encoding specificity and retrieval processes in episodic memory. Psychological Review, 80, 352–373. Wixted, J. T. (2007). Dual-process theory and signal-detection theory of recognition memory. Psychological Review, 114, 152–176. Wixted, J. T., & Mickes, L. (2010). A continuous dual-process model of remember/know judgments. Psychological Review, 117, 1025–1054. Yonelinas, A. P. (1994). Receiver-operating characteristics in recognition memory: Evidence for a dual-process model. Journal of Experimental Psychology: Learning, Memory, and Cognition, 20, 1341–1354. Yonelinas, A. P. (1999). The contribution of recollection and familiarity to recognition and source-memory judgments: A formal dual-process model and an analysis of receiver operating characteristics. Journal of Experimental Psychology: Learning, Memory, and Cognition, 25, 1415–1434. Yonelinas, A. P. (2002). The nature of recollection and familiarity: A review of 30 years of research. Journal of Memory and Language, 46, 441–517. Yonelinas, A. P., & Parks, C. M. (2007). Receiver operating characteristics (ROCs) in recognition memory: A review. Psychological Bulletin, 133, 800–832.