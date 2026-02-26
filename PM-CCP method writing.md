# Method

## Theoretical Framework

This study investigates how value-based intention selection mechanisms interact with prospective memory demands by combining a multiple cue paradigm (MCP) with embedded prospective memory (PM) tasks. We draw on the Prospective Memory Decision Control (PMDC) framework developed by Strickland et al. (2018), which characterizes PM retrieval as an evidence accumulation process that can be modeled using the Linear Ballistic Accumulator (LBA). The PMDC framework distinguishes between two key mechanisms: proactive control, which operates through strategic adjustment of decision thresholds, and reactive control, which involves capacity-limited changes in information processing rates.

The critical theoretical question is whether value-based intention selection operates through threshold control (strategic caution adjustments), through capacity sharing (competition for limited processing resources), or through a combination of both mechanisms. To test these alternatives, we manipulate PM cue focality—a well-established distinction in the PM literature that separates cues requiring minimal attentional monitoring (focal cues) from those requiring sustained vigilance (nonfocal cues). According to multiprocess theory (Einstein & McDaniel, 2005), focal cues can trigger retrieval relatively automatically, while nonfocal cues demand active monitoring that should tax limited cognitive capacity.

We consider three competing theoretical accounts. The strategic threshold control account predicts that both PM demands and MCP reward values modulate decision boundaries, with higher-priority intentions receiving lower thresholds regardless of whether this priority comes from PM importance or MCP reward magnitude. The shared capacity account predicts that nonfocal PM monitoring depletes the same attentional resources needed for processing MCP cues, reducing evidence accumulation rates (drift rates) particularly for high-value intentions that had allocated substantial resources. The dual-mechanism account predicts both effects operate in parallel: PM demands increase thresholds globally (proactive control), while nonfocal monitoring specifically reduces drift rates (reactive capacity limitation).

## Participants

We will recruit 30 (?) adults aged 18-35 from the University of Copenhagen participant pool. All participants will provide informed consent and receive course credit plus performance-based monetary compensation (€0.01 per point earned in the task). Participants will be screened for normal color vision using Ishihara plates and normal or corrected-to-normal visual acuity. We will exclude participants who show PM hit rates below 20% (indicating failure to engage with the PM task), MCP accuracy below 60% (indicating task misunderstanding), or more than 15% anticipatory responses (RT < 200ms).

## Apparatus and Stimuli

The experiment will be programmed in PsychoPy and presented on a 24-inch LCD monitor at 60 Hz refresh rate. Participants will sit approximately 60 cm from the screen and respond using a standard keyboard.

On each trial, four colored circles (150px diameter) appeared in a roughly square formation centered on screen. Each circle contained a black number (0-4) indicating the reward value for responding to that color. We used a colorblind-safe palette: red, blue, green, and yellow, with each color mapped to a corresponding key (d, c, k, m). The key mapping is chosen such way basing on the natural resting position of index and middle figures of both left and right hands. The left hand index finger is instructed to place on 'c' and middle finger on 'd', and the right hand index finger is instructed to place on 'm' and middle finger 'k'. 

The experiment included two types of MCP trials. **Single-cue trials** presented one circle with a reward value (1, 2, 3, or 4) while the others showed "0". **Dual-cue trials** presented two circles with different reward values (2 vs 1, 3 vs 1, 4 vs 1, 3 vs 2, 4 vs 2, or 4 vs 3) while the others showed "0". Color assignments and spatial positions were fully counterbalanced across trials.

For the PM manipulation, we used two types of cues. **Focal PM cues** consisted of an orange border (8px thick) surrounding one circle. Because participants were already processing color information for the MCP task, the orange border falls on the same visual dimension as the task-relevant features, meeting the definition of a focal cue. **Nonfocal PM cues** consisted of a small white star symbol (★) appearing inside one circle. The star requires monitoring a separate feature dimension (shape/symbol) not otherwise processed for the MCP task, making it nonfocal. Critically, PM cues always appeared on circles displaying "0" so they never provided useful information for the MCP task.

## Procedure

Participants completed thirteen experimental sessions over 3-4 weeks, with each session lasting 30-60 minutes depending on the phase. The first five sessions focused on gradual training to ensure thorough learning of the color-key mappings and task structure. Sessions 6-7 established baseline MCP performance without PM demands, while sessions 8-13 introduced the PM manipulations. Half the participants encountered focal PM cues first (sessions 8-10) and nonfocal cues second (sessions 11-13), with order reversed for the remaining participants.

### Sessions 1-5: Training Phase

The training protocol followed a careful progression to ensure participants fully automatized the color-key mappings before introducing task complexity. Session 1 (100 trials, five 20-trial blocks) presented colored circles only at the center of the screen, with a single cue per trial showing reward values 1-4. The color-key mapping chart remained visible at the bottom of the screen throughout this session to support initial learning.

Session 2 (100 trials, five 20-trial blocks) moved the colored circles to peripheral locations matching the experimental display, but maintained the single-cue structure with only one circle showing a reward value per trial. The mapping chart remained visible to support the transition from central to peripheral presentation.

Session 3 (60 trials, two 30-trial blocks) introduced dual-cue trials for the first time, with all ten experimental trial types (four single-cue and six dual-cue configurations) appearing. The mapping chart remained visible as participants learned to handle competition between multiple rewarded options.

Session 4 (60 trials, two 30-trial blocks) continued with the full dual-cue protocol but removed the on-screen mapping chart, requiring participants to rely on memory for the color-key associations. This session ensured participants had internalized the mappings before data collection began.

Session 5 (100 trials, two 50-trial blocks) provided additional practice with the full experimental protocol without visual scaffolding, establishing stable performance and confidence with the complete task structure.

### Sessions 6-7: Control Baseline

These sessions established baseline MCP performance without any PM demands. Each session included 200 trials (four 50-trial blocks) with the standard distribution of ten trial types. Performance feedback remained identical to training: correct MCP responses showed "+[X] points!" in green, incorrect responses showed "Wrong color -2 points" in red, and responses exceeding 3000ms showed "TOO SLOW" in red. These 400 baseline trials were essential for establishing individual differences in MCP performance and providing a clean comparison point for measuring PM costs.

### Sessions 8-10: First PM Condition

These sessions introduced the first PM manipulation (either focal or nonfocal depending on counterbalancing). At the start of session 8, participants received detailed instructions about the PM task, emphasizing that catching PM cues was a priority. For focal PM, they were told to press the spacebar whenever they saw a circle with an orange border. For nonfocal PM, they were told to press the spacebar whenever they saw a star symbol inside a circle.

After instructions, participants completed a brief practice block (30 trials with 30% PM frequency) to familiarize themselves with the dual-task demands. Each of the three PM sessions then included 200 trials (four 50-trial blocks) with PM cues appearing on 15% of trials (30 PM trials per session). This yielded 90 PM trials across the three sessions. Correct PM responses displayed "PM CUE CAUGHT! +10 points" in blue, while missed PM cues displayed "MISSED PM CUE -10 points" in red at the end of the trial.

### Sessions 11-13: Second PM Condition

These sessions followed the same structure as sessions 8-10 but introduced the alternate PM cue type. Participants who had completed focal PM in sessions 8-10 now encountered nonfocal PM, and vice versa. Again, each session included 200 trials with 15% PM frequency, yielding 90 PM trials total for the second condition.

### Trial Timing

Each trial began with a 500ms fixation cross, followed by the cue display which remained on screen until response (maximum 3000ms). Feedback appeared for 800ms, followed by a 500ms inter-trial interval (jittered ±100ms). Total trial duration was approximately 2.3-2.8 seconds, making each block manageable in terms of participant fatigue.

### Trial Distribution

The trial distribution varied across training and experimental phases. During training sessions 1-2, each 20-trial block presented the four single-cue types (reward values 1, 2, 3, 4) with 5 repetitions each. Sessions 3-5 introduced the full distribution of ten trial types: four single-cue conditions and six dual-cue conditions (2v1, 3v1, 4v1, 3v2, 4v2, 4v3).

For the control baseline and PM sessions, each 50-trial block maintained this full distribution with approximately: 20 single-cue trials (5 per type) and 30 dual-cue trials (5 per type). Across a full 200-trial session, this yielded roughly 80 single-cue trials and 120 dual-cue trials, ensuring adequate sampling of all trial types while maintaining naturalistic task difficulty.

In PM sessions, the 30 PM cues (15% of 200 trials) were distributed across blocks to maintain consistent PM frequency throughout each session. PM cues always appeared on circles displaying "0" and were evenly distributed across the four circle positions to prevent spatial learning.

Across the entire experiment, participants completed approximately 2,020 total trials: 420 training trials, 400 control baseline trials, 600 focal PM trials (including 90 PM cue trials), and 600 nonfocal PM trials (including 90 PM cue trials).
## Data Analysis

### Behavioral Analyses

We analyzed MCP performance focusing on accuracy (percentage of correct color selections), response time for correct trials, and optimal selection rate (percentage of trials where participants chose the highest-reward color). We used 2 (Focality: Focal vs Nonfocal) × 2 (Cue Type: Single vs Dual) repeated-measures ANOVAs to test for main effects and interactions. A key dependent measure was the dual-cue competition cost, calculated as the RT difference between dual-cue and single-cue trials, which indexes the difficulty of selecting among competing intentions.

PM performance was assessed through hit rate (percentage of PM cues correctly detected) and false alarm rate (spacebar presses on non-PM trials). We also calculated the PM cost on MCP performance by comparing RTs on no-PM-cue trials in PM blocks to RTs in the control baseline sessions. This cost measure is critical because it reflects the monitoring demands imposed by the PM task even on trials where no PM cue appears.

### Linear Ballistic Accumulator Modeling

The core theoretical tests relied on fitting LBA models to the choice and RT data. The LBA assumes independent evidence accumulators for each response option race toward a decision threshold, with the first to reach threshold determining the response. For this study, we implemented five accumulators (Red, Blue, Green, Yellow, and PM) that raced on each trial. In control blocks, only the four color accumulators were active, while in PM blocks all five could compete.

The model has several key parameters. The threshold parameter (b) controls decision caution—higher thresholds require more evidence before committing to a response. The drift rate parameter (v) governs how quickly evidence accumulates, with higher values producing faster and more accurate responses. Additional parameters include start-point variability (A), drift rate variability (sv), and non-decision time (t0) which captures perceptual encoding and motor execution processes.

We used hierarchical Bayesian estimation implemented in Stan, which allows individual-level parameters to be informed by population-level distributions while still capturing individual differences. Models were fit separately for each condition (Control, Focal PM, Nonfocal PM) using 4 chains with 2000 iterations each (1000 warm-up). We assessed convergence using the R-hat statistic and required all parameters to have R-hat < 1.01.

To adjudicate among the three theoretical accounts, we compared three model variants. The threshold-only model implements both reward and PM effects through threshold differences while holding drift rates constant across conditions. The drift-only model implements effects through drift rate changes while holding thresholds constant. The dual-mechanism model allows both thresholds and drift rates to vary with task demands. We will compare these models using WAIC and LOO-CV, which balance model fit against complexity.

### Individual Differences

In an optional seventh session, we will collect individual differences measures to test predictions about the cognitive resources underlying different control mechanisms. The Operation Span task measures working memory capacity, the Pattern Comparison task measures processing speed, and a Stop-Signal task measures inhibitory control. The dual-mechanism account predicts that WM capacity should correlate with threshold modulation (reflecting proactive control ability), while processing speed should correlate with drift rate modulation (reflecting reactive capacity). These correlations should be independent if the mechanisms are truly dissociable.

## Predictions

### Behavioral Predictions

The three theoretical accounts make distinct behavioral predictions. If intention selection operates purely through strategic threshold control, we should see RT slowing in PM blocks relative to control, but this slowing should be similar for focal and nonfocal conditions since both require threshold adjustment. Accuracy should remain stable because increased caution compensates for any added difficulty. Importantly, there should be minimal interaction between PM condition and dual-cue trial type because threshold control doesn't involve capacity limitations.

The shared capacity account predicts a different pattern. Nonfocal PM should produce accuracy decrements, particularly on dual-cue trials where capacity demands are highest. Focal PM should produce minimal cost because focal cues don't require sustained monitoring. The RT increases under nonfocal PM should reflect genuinely slowed processing rather than strategic caution. Dual-cue trials should show disproportionately large costs under nonfocal PM because the capacity demands of monitoring and multi-cue processing compound.

The dual-mechanism account predicts dissociable effects. PM presence should increase RT globally through proactive threshold adjustment, but nonfocal PM should additionally reduce accuracy on complex trials through reactive capacity limitation. We should see pure RT slowing for focal PM but both slowing and accuracy loss for nonfocal PM, with the pattern depending on trial complexity.

### LBA Parameter Predictions

The most definitive tests come from the LBA parameter estimates. The threshold-only account predicts that PM blocks show increased thresholds relative to control (b_PM > b_Control), with similar increases for focal and nonfocal conditions. Critically, the relative threshold differences among MCP responses based on reward value should be preserved across conditions—if high-reward colors have lower thresholds than low-reward colors in the control condition, this pattern should persist in PM blocks. Drift rates should show no systematic changes across conditions.

The capacity account predicts the opposite pattern. Thresholds should remain stable across conditions, while drift rates should decrease specifically in the nonfocal PM condition (v_Nonfocal < v_Control ≈ v_Focal). Moreover, the drift rate reduction should be larger for high-reward colors that had allocated more attentional resources in the baseline condition. This predicts an interaction between reward level and nonfocal monitoring demands in the drift rate estimates.

The dual-mechanism account predicts both patterns simultaneously. PM should increase thresholds (Control < Focal < Nonfocal), with nonfocal showing larger increases due to task difficulty. Reward-based threshold differences should be preserved additively across PM conditions. Additionally, nonfocal PM should selectively reduce drift rates while focal PM leaves drift rates largely unchanged. The threshold effects should be constant across trial types (reflecting sustained proactive control), while the drift effects should vary by trial type (reflecting trial-specific reactive processing demands).

### Critical Distinguishing Tests

Three specific comparisons will distinguish the accounts. First, we can examine the focal versus nonfocal dissociation: does nonfocal PM affect parameters differently than focal PM? The threshold-only model predicts both increase thresholds similarly without affecting drift. The capacity model predicts only nonfocal reduces drift without threshold changes. The dual-mechanism model predicts both increase thresholds (nonfocal more so) and only nonfocal reduces drift.

Second, we can examine how PM effects interact with MCP reward structure. The threshold model predicts additive effects on thresholds with no drift changes. The capacity model predicts interactive effects on drift rates. The dual-mechanism model predicts both additive threshold effects and interactive drift effects.

Third, the individual differences structure provides a strong test. If a single factor (strategic control or capacity) drives all PM-MCP interactions, we should see a single latent variable predicting both behavioral costs and parameter changes. If the mechanisms are truly dissociable, we should find two uncorrelated factors: working memory capacity predicting threshold modulation and processing speed predicting drift rate preservation. This would strongly support the dual-mechanism account while ruling out the single-mechanism alternatives.