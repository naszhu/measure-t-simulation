\subsection{From Familiarity Distributions to Measure Transformations}

In SDT, recognition memory is modeled by comparing two probability distributions on a one-dimensional familiarity space. The decision to respond ``old'' or ``new'' depends on whether the observed familiarity value is more likely under the old-item distribution or the new-item distribution. This is, at its core, a comparison of two probability measures.

We can extend this structure in several natural ways. First, we can move from one-dimensional familiarity to a richer joint space that includes both content (items, features) and context (temporal positions, contextual states). Second, we can allow measures to evolve over time, rather than remaining static. Third, we can introduce different types of transformations: deterministic shifts (push-forward mappings), stochastic sampling (kernel transformations), or selective reweighting (density changes).

When we do this, we find that memory models fall naturally into a unified framework. The study-phase measure $\studymeasure$ encodes what was learned, and retrieval involves transforming this measure in various ways. For example, we might construct a discrete measure on the product space $\contentspace \times \contextspace$: {\jy for fixed sequences $\{f_t\}_{t \in \mathbb{N}} \subset \mathcal F$ and $\{\psi_t\}_{t \in \mathbb{N}} \subset \mathcal C$, let us define $\mu_\text{study}$ via}
\begin{equation}
\studymeasure(A \times B) = \sum_{t=1}^{T} \gamma_t \mathbb{1}_A(f_t) \mathbb{1}_B(\psi_t)
\end{equation}
{\jy for any measurable sets $A \subset F$ and $B \subset C$, }where $\{f_t\}$ are item vectors, $\{\psi_t\}$ are context vectors, $\gamma_t \in \R$ are encoding strengths, and $\mathbb{1}_A$ is the indicator function. {\jy In other words, $\mu$ is a sum of Dirac $\delta$ functions on the product space weighted by $\gamma_i$'s, i.e. for any continuous function on $\mathcal F \times \mathcal C$, 
\begin{align*}
    \int_{\mathcal F \times \mathcal C} G(f,\psi) \mathrm d \mu(f,\psi) &:= \int_{\mathcal F \times \mathcal C} G(f,\psi) \pr{\sum_{t = 1}^T \gamma_t\delta_{f_t}(\mathrm df) \delta_{\psi_t}(\mathrm d\psi)}\\
    &=\sum_{t = 1}^T \gamma_t G(f_t, \psi_t).
\end{align*}

}

{\jy If furthermore the spaces $\mathcal F$ and $\mathcal C$ are equipped with inner product structures, i.e. Hilbert spaces, $\langle\cdot,\cdot\rangle$'s, we may define for each $i = 1,\dots, T$ and $\psi(\text{cue}) \in \mathcal C$ the function $A_{i,\psi(\text{cue})}:\mathcal F \times \mathcal C \mapsto \R$ via 
\begin{align*}
    A_{i,\psi(\text{cue})}(f,\psi):= \langle f_i,f\rangle\cdot \langle\psi(\text{cue}), \psi\rangle.
\end{align*}
}
{\jy Then, the r}etrieval then becomes an integral over this transformed measure:
\begin{equation}
a(i|\text{cue}) 
=\int_{\contentspace \times \contextspace} \langle f_i, f \rangle \langle \psi(\text{cue}), \psi \rangle \, d\studymeasure(f, \psi)
\end{equation}
{\jy The retrieval function can be constructed via the following simple method
\begin{align*}
     a(i|\text{cue}) &:=  \int_{\mathcal F \times \mathcal C} A_{i,\psi(\text{cue})}(f,\psi) \mathrm d\mu(f,\psi)\\
     &=\int_{\mathcal F\times \mathcal C} \langle f_i,f\rangle\cdot \langle\psi(\text{cue}), \psi\rangle. \mathrm{d}\mu(f,\psi). 
\end{align*}

}

This measure-theoretic view naturally extends to continuous models, probabilistic frameworks, and neural network representations, providing a common foundation for understanding memory across different levels of analysis.

\section{Mathematical Foundations}

\subsection{Measurable Spaces and Joint Measures}

\begin{definition}[Memory Space Structure]
Let $(\contentspace, \mathcal{B}_{\mathcal{F}})$ and $(\contextspace, \mathcal{B}_{\mathcal{C}})$ be measurable spaces representing:
\begin{itemize}
    \item \textbf{Content space} $\contentspace$: The space of item/feature representations
    \item \textbf{Context space} $\contextspace$: The space of contextual/temporal states
\end{itemize}

The \textbf{joint memory space} is $(\contentspace \times \contextspace, \mathcal{B}_{\mathcal{F}} \otimes \mathcal{B}_{\mathcal{C}})$, where $\otimes$ denotes the product $\sigma$-algebra.
\end{definition}

\begin{definition}[Study-Phase Measure]
During study, a sequence of items $\{x_t\}_{t=1}^{T}$ is encoded, producing item vectors $\{f_t\}$ and context vectors $\{\psi_t\}$. The \textbf{study-phase measure} $\studymeasure$ is defined on $\contentspace \times \contextspace$ as:
\begin{equation}
\studymeasure(A \times B) = \sum_{t=1}^{T} \gamma_t \mathbb{1}_A(f_t) \mathbb{1}_B(\psi_t)
\end{equation}
where $\gamma_t$ is the encoding strength at time $t$.
{\jy In other words, 
\begin{align*}
    \mathrm d\mu_\text{study}(f,\psi):= \sum_{t = 1}^T \gamma_t \delta_{f_t}(\mathrm df) \otimes \delta_{\psi_t}(\mathrm d\psi).
\end{align*}

}
For continuous models, $\studymeasure$ may have a density $d\studymeasure(f, \psi) = w(f, \psi) \, d(f, \psi)$ with respect to a base measure (e.g., Lebesgue or counting measure).

{\jy For example, suppose $\mathcal F = \mathcal C = [0,1]$, which are continuums, and let $\mathrm{d}x$ be the Lebesgue's measure on $[0,1]$. For any non-negative measurable function $S$ on $ [0,1]^2$, we may define 
\begin{align*}
    \mathrm d\mu_S(f,\psi):= S(f,\psi) \mathrm df \mathrm d\psi.
\end{align*}

}
\end{definition}

\subsection{The Three Fundamental Measure Transformations}

All memory processes can be expressed through three types of measure transformations:

\subsubsection{Kernel Transformation (Stochastic Transition)}

{\jy 
\begin{definition}
    Let $\pr{\mathbb X,\mathcal X}$ be a measurable space, a integral kernel $K$ on $\mathbb{X}$ is a map on $\mathbb{ X}\times \mathcal X$ so that 
    \begin{itemize}
        \item for each $x \in \mathbb{X}$, $K(x,\cdot)$ is a probability measure on $\X$.
        \item For each measurable set $A \in \mathcal X$, the function $x \mapsto K(x, A)$ is a measurable function. 
    \end{itemize}
\end{definition}

}

\begin{definition}[Kernel Transformation]
{\jy Let $K$ be a  probability integral kernel on $(\Omega, \mathcal B_\Omega)$, that is a measurable space, the $K$-}\textbf{kernel transformation} of $\mu$ {\jy denoted by $K\mu$ is a measure on $(\Omega, \mathcal B_\Omega)$, so that for each $A \in \mathcal B_\Omega$,}
\begin{equation}
K\mu(A):=\nu(A) = \int_{\Omega} K(x, A) \, d\mu(x).
\end{equation}
\end{definition}

\textbf{Psychological Interpretation:} Kernel transformations represent \textbf{stochastic retrieval processes}---probabilistic sampling from similarity distributions, retrieval noise, or context-dependent activation.

\textbf{Memory Applications:}
\begin{itemize}
    \item \textbf{REM (Retrieving Effectively from Memory):} Retrieval via similarity-based sampling
    \item \textbf{EBRW (Exemplar-Based Random Walk):} Stochastic accumulation of evidence
    \item \textbf{Monte Carlo STM:} Probabilistic retrieval with uncertainty
\end{itemize}

\textbf{Mathematical Representation:}

For retrieval under cue $\psi(\text{cue})$, the kernel $K_\sigma(\psi(\text{cue}), \cdot)$ defines a probability distribution over context space with bandwidth $\sigma^2$:
\begin{equation}
K_\sigma(\psi(\text{cue}), d\psi') = \frac{1}{Z} \exp\left(-\frac{\|\psi(\text{cue}) - \psi'\|^2}{2\sigma^2}\right) \, d\psi',
\end{equation}
{\jy where $Z$ is a normalization constant so that 
\begin{align*}
    \int_{\mathcal C} K_\sigma(\psi(\text{cue}), d\psi') \mathrm d \psi' = 1.
\end{align*}
Observe that, if $\mathcal F$ comes with a inner product structure, and $\mathcal K_{\sigma}((f,\psi), \cdot)$ defined via  $\delta_f(\mathrm df')\otimes  K_\sigma(\psi, \psi') \mathrm d\psi$ is an probability integral kernel on $\mathcal F \times \mathcal C$. In addition, 
\begin{align*}
   \int_{\mathcal F\times \mathcal C} G(f,\psi) \mathrm d \mathcal K_\sigma \mu_\text{study}(f,\psi)&= \int_{\mathcal F\times \mathcal C}G(f,\psi)  \int_{\mathcal F\times \mathcal C}\delta_f(\mathrm df')\otimes  K_\sigma(\psi, \mathrm d\psi') \mathrm d\psi \mathrm{d}\mu(f',\psi')\\
    &=\int_{\mathcal F\times \mathcal C} \int_{\mathcal F\times \mathcal C}G(f,\psi) \delta_f(\mathrm df')\otimes  K_\sigma(\psi, \mathrm d\psi') \mathrm d\psi \mathrm{d}\mu(f',\psi')\\
    &=\int_{\mathcal F\times \mathcal C} G(f', \psi) K_\sigma(\psi, \psi') \mathrm d\psi \mathrm d \mu(f',\psi').
\end{align*}
Then, for retrieval $a(i,\text{cue})$, we may define $G_{i,cue}(f,\psi):= \langle f_i,f\rangle$, then 
}
Retrieval activation becomes:
\begin{equation}
a(i|\text{cue}){\jy : = \int_{\mathcal F \times \mathcal C} G_a(f,\psi)\mathrm d \mathcal K_{\sigma}\mu_{study}(f,\psi)}= \int_{\contentspace \times \contextspace} \langle f_i, f \rangle K_\sigma(\psi(\text{cue}), d\psi) \, d\studymeasure(f, \psi)
\end{equation}

As $\sigma^2 \to 0$, the kernel approaches a Dirac delta, yielding deterministic context matching.

\textbf{Simulation Demonstration:}

To illustrate kernel transformation concretely, we implemented a computational simulation\footnote{Code and visualizations available at \url{https://github.com/naszhu/measure-t-simulation}} that demonstrates how kernel bandwidth controls retrieval precision. The simulation creates a discrete study-phase measure $\studymeasure$ on a 2D context space by storing 8 items, each with an associated context vector. During retrieval, a cue $\psi(\text{cue})$ activates stored memories according to the Gaussian kernel $K_\sigma(\psi(\text{cue}), \cdot)$.

Figure~\ref{fig:kernel-visualization} shows how different bandwidth values $\sigma^2 \in \{0.1, 0.5, 2.0, 5.0\}$ affect the activation pattern. The contour heatmap visualizes the kernel activation field $K_\sigma(\psi(\text{cue}), \cdot)$ across context space, while the colored circles show the activation strength for each stored item (size proportional to activation). With small bandwidth ($\sigma^2 = 0.1$), activation is highly focused around the cue, demonstrating recall-like precision. As bandwidth increases, activation spreads more broadly, capturing recognition-like behavior where many items contribute to familiarity.

Figure~\ref{fig:bandwidth-comparison} compares activation patterns across bandwidths, showing how the distribution of activation across items changes systematically. Small bandwidths produce sparse, focused activation (high precision), while large bandwidths produce diffuse activation across many items (high recall). This visualization demonstrates the recognition--recall equivalence principle: both processes use the same kernel transformation, differing only in bandwidth precision.

\begin{figure}[h]
\centering
\includegraphics[width=0.95\textwidth]{images/kernel_transformation_visualization.png}
\caption{Kernel transformation visualization showing how bandwidth $\sigma^2$ controls retrieval precision. Each panel shows the kernel activation field (contour heatmap), stored contexts (black dots), retrieval cue (red star), and item activations (colored circles, size proportional to activation). Small bandwidth ($\sigma^2 = 0.1$) produces focused, recall-like activation; large bandwidth ($\sigma^2 = 5.0$) produces diffuse, recognition-like activation.}
\label{fig:kernel-visualization}
\end{figure}

\begin{figure}[h]
\centering
\includegraphics[width=0.95\textwidth]{images/bandwidth_comparison.png}
\caption{Comparison of activation patterns across bandwidths. Left panel: Heatmap showing activation strength across items (columns) and bandwidths (rows). Right panel: Activation profiles for each bandwidth, demonstrating how bandwidth controls the precision--recall trade-off.}
\label{fig:bandwidth-comparison}
\end{figure}

\begin{definition}[Push-Forward Measure]
Given a measurable map $T: \Omega \to \Omega'$ and a measure $\mu$ on $\Omega$, the \textbf{push-forward measure} {\jy of $\mu$ under the map $T$, for which we call} $\pushforward{T}{\mu}$, on $\Omega'$ is defined as:
\begin{equation}
(\pushforward{T}{\mu})(B) = \mu(T^{-1}(B))
\end{equation}
for all measurable sets $B \subseteq \Omega'$.
\end{definition}

\textbf{Psychological Interpretation:} Push-forward transformations represent \textbf{deterministic context evolution}---context drift, encoding mappings, or spatial transformations of representations.

\textbf{Memory Applications:}
\begin{itemize}
    \item \textbf{TCM (Temporal Context Model):} Context drift $\psi_{t+1} = \rho\psi_t + \eta f_t$ defines a push-forward
    \item \textbf{CRU (Context Retrieval and Updating):} Context as mixture of previous items via linear transformation
    \item \textbf{SIMPLE:} Temporal compression via log-transform mapping
\end{itemize}

\textbf{Mathematical Representation:}

In TCM, the context evolution  $T_t(\psi_t)=\rho\psi_{\jy t} + \eta f_t$ defines a family of push-forward maps {\issue I think meant $T_t(f,\psi) =  f_t\otimes \pr{\rho\psi_t+\eta f_t}$?}. The study-phase measure evolves as:
\begin{equation}
\mu_{t+1} = \pushforward{T_t}{\mu_t} + \delta_{(f_{t+1}, \psi_{t+1})}
\end{equation}
where $\delta_{(f, \psi)}$ is a point mass at $(f, \psi)$. {\issue what's $\mu_t$ here?}

{\jy
\begin{align*}
    \int G(f,\psi) \mathrm d\mu_{t+1} = \int G\circ T_{t}\pr{f,\psi} \mathrm d\mu_t + G(f_{t+1}, \psi_{t+1}).
\end{align*}
}
{\issue I can't make sense of this one.}

\subsubsection{Density Change (Reweighting)}

\begin{definition}[Radon--Nikodym Derivative / Density Change]
Given two measures $\mu$ and $\nu$ on $(\Omega, \mathcal{B})$ where $\nu \ll \mu$ (absolute continuity), the \textbf{Radon--Nikodym derivative} $w = \radonnikodym$ satisfies:
\begin{equation}
\nu(A) = \int_A w(x) \, d\mu(x)
\end{equation}
\end{definition}

\textbf{Psychological Interpretation:} Density changes represent \textbf{attentional weighting}, \textbf{rehearsal effects}, or \textbf{selective emphasis}---reweighting the importance of different parts of the measure.

\textbf{Memory Applications:}
\begin{itemize}
    \item \textbf{SOB (Serial Order in a Box):} Novelty-weighted encoding via $\gamma_t = n_t$
    \item \textbf{Page \& Norris Primacy Model:} Primacy gradient $\gamma_t = e^{-\lambda t}$
    \item \textbf{EBRW:} Attention-driven weighting during recognition
\end{itemize}

\textbf{Mathematical Representation:}

Encoding strength variations correspond to density changes:
\begin{equation}
d\mu_{\text{weighted}}(f, \psi) = w(f, \psi) \, d\studymeasure(f, \psi)
\end{equation}
where $w(f, \psi)$ is the Radon--Nikodym derivative. For discrete measures:
\begin{equation}
\mu_{\text{weighted}}(A \times B) = \sum_{t=1}^{T} w(f_t, \psi_t) \gamma_t \mathbb{1}_A(f_t) \mathbb{1}_B(\psi_t)
\end{equation}

\subsection{Composition of Transformations}

Memory processes often involve \textbf{compositions} of the three transformation types:

\begin{example}[TCM with Retrieval Noise]
Context drift (push-forward) followed by stochastic retrieval (kernel):
\begin{equation}
\mu_{\text{retrieval}} = K_\sigma(\psi(\text{cue}), \cdot) \circ \pushforward{T_T \circ \cdots \circ T_1}{\mu_0}
\end{equation}
{\issue I don't understand the meaning of this, how do you compose $K$ with other functions? Do you mean 

\begin{align*}
    \mu_{\text{retrieval}} = K_\sigma(\psi(cue),\cdot) \ast \pr{\pr{T_T \circ \cdots \circ T_1_\#} \mu}?
\end{align*}
}
\end{example}

\begin{example}[Weighted Sampling]
Density change (novelty weighting) followed by kernel transformation (sampling):
\begin{equation}
d\mu_{\text{sampled}}(f, \psi) = K(\psi(\text{cue}), d\psi) \cdot w(f, \psi) \, d\studymeasure(f, \psi)
\end{equation}
\end{example}
{\issue $K$ is a measure in one argument, so here one has measure times measure, this does not make sense. Do you mean $K$ convolution another meausre like 
\begin{align*}
    d\mu_{\text{sampled}}(f, \psi) = K(\psi(\text{cue}), d\psi)\ast  w(f, \psi) \, d\studymeasure(f, \psi)?
\end{align*}
}

