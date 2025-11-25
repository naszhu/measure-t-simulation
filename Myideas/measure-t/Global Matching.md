

Let $(X,\mathcal X)$ be a measurable space. If $\mu$ is a Radon measure on $(X,\mathcal X)$ 
$$
\mu,\, \nu  \text{ measures on }  \mathcal X
$$

$$
\mu <<\nu \leftrightarrow \forall A \subset \mathcal X, \nu(A) = 0 \Rightarrow \mu(A) = 0.
$$

$$
\frac{\mathrm d\mu}{\mathrm d\nu} \text{ exists .}
$$

$$
X = \R,\, \Lambda\text{ is Leb-measure.}
$$

Let $\delta_0$ is Dirac delta mass at zero. 

$\Lambda \text{ is not absolutely continuous with respect to } \delta_0$, i.e. $\delta_0(A) =0$ does not imply $\Lambda(A)=0$. $\Lambda$ not $<<$ $\delta_0$.

e.g. $A = [1,2]$, then $\delta_0(A) = 0$, but $\Lambda([1,2]) = 1$.

$\delta_0$ is not absoltuely continuous with respect to $\Lambda$. 

e.g. $\Lambda(\{0\}) = 0$ but $\delta_0(\{0\}) =1$.



$$\delta_0(\{0\}) =1$$ and $\delta_0(\{0\}^c) = 0$.  $\Lambda(\{0\}^c)$ full measure.



$\{1,2,3.\dots, n\}$



**Definition of a kernel**

$K(x,dy)$ is an kernel from measurable space $(Y, \mathcal Y)$ to $(X,\mathcal X)$

1) For each $x \in X$, $K(x,\mathrm dy)$ is a measure on $(Y,\mathcal Y)$.
2) For any set $A \subset Y$, $K(x,A)$ is a measurable function in on the space $X$.

**Kernel apply to a measure**

If $\mu$ is a measure. $K\ast \mu$ is a meaure defined via 
$$
K\ast \mu(A) = \int \int_A K(x,\mathrm dy) \mu(dx)
$$







$$
K_t(x,\mathrm dy) = p_t(x,y) \mathrm dy
$$

$$
p_t(x,y) = (2\pi t)^{\frac{1}{2}} \exp \left(- \frac{(x-y)^2}{2t} \right)
$$

$$
K_t\ast\delta_0 (\mathrm dx)= \left(\int_\R p_t(x,y) \delta_0(\mathrm dy)\right) \mathrm dx = p_t(x,0) \mathrm dx
$$



$$\delta_0 \perp \Lambda$$ but $K\ast \delta_0 << \Lambda$











$x = \text{💡}$

Case 1: x is an item.

Case 2: 💡 和 Lea together is an item.

Pick $r \ge 0$, the define the actual item related to 💡 as $B_r(x)$. 

When $r= 0$, then $B_0(x) = \{x\}$, corresponds to case 1. 

When $r>0$, then $B_r(x) = \{💡, Lea\}$

y = 窗帘

Item y:= $B_r(y)$ for appropriate $r\ge0$, so that $x \in B_r(y)$

Item Lea:= $B_{r'}(Lea) = \{Lea,💡\}$.

similarity of Item y and Item Lea = $B_r(y) \cap B_{r'}(Lea) = \{💡\}$.

An item is a set, that is a ball centered at some location x, with radius r. 

When we say item $(x,r)$, we mean $B_r(x)$.




$$
\R^3
$$


item x: $p_\varepsilon(x,y)\mathrm dy$ where $\varepsilon$ is small

Almost forgot what x is, $p_{T}(x,y) \mathrm dy$ where $T$ is big. 



































All models in math is of the form
$$
u = F(u). 
$$


All mechanism is of the form for some function $G: X \to Y$,
$$
G(x) 
$$


All things you can you measure in experimental science is in some Space $\mathcal H$.

familarity: sclar intensity, represent the likelyhood (probability) that $q \in M$.

Recollection: is discrete change, diagnostic validity, conditional probability of retreiving qualitative details (item), i.e. probability of getting a specific element $q$. 

**Global Matching models**

End Goal: predict actions/choices

Measure familiarity, then predict probability of choice.

**Recollection**

Measure conditional probability of retreiving qualitative details. 

## Global Matching

$E$ is some set represents the physical space, maybe with structures. 

$M$, the **Memory space**, a space with some structures. 

$F$, is the encoding functions from $E$ to $M$.

*Idea: Let $\mathcal M(E)$ be the space of measures on $E$. Then define $M=\mathcal M(E)\otimes  E$*.

If $x \in E$, then $F(x) =\mu_x\otimes  x$, where $\mu_x \in \mathcal M(E)$ for each $x \in E$. 

If i am talking about $m \in M$, then $m$ must be of the form $\mu\otimes x$ for some measure $\mu$ on $E$ and $x \in E$.

Example of measures:

1. $\delta$-measure. 
2. If $E$ comes with a reference measure $\mu$. $f(x) \mu(dx)$ is a measure that is absoltuely continuous with respect to $\mu$. 

Measure the probability of $F(\text{cue})\in M$ for some transformation $F: E \mapsto M$. 

1) What is $\text{cue}$:  $\text{cue}$ is a cue.
2) What is $M$: $M$ is memory, memory is a collection of trace, after mapping. Memory is in brain. $M$ must be a set, maybe with some structures. In theory, it must have structures. 
   1) e.g. $M$ is a Hilbert space. 
   2) e.g. The space of measures. 

3. What is $F$: map from physical space to memory space. 

















$X$: collection for humans

$Y$: collection of fruits.

$M_{\text{all human}}:=X\otimes Y = \{(human, fruit)\}$



$M_\text{Johnny} = \{(johnny, banana)\}$





