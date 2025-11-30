

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

Almost forgot what x is, $p_{T}(x,y) \mathrm dy$ where $T $ is big. 



































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

$E$ is some set represents the **physical space**, maybe with structures. 

$M$, the **Memory space**, a space with some structures. 

$F$, is the **encoding functions** from $E$ to $M$.

*Idea: Let $\mathcal M(E)$ be the space of measures on $E$. Then define $M=\mathcal M(E)\otimes  E$*.

If $x \in E$, then $F(x) =\mu_x\otimes  x$, where $\mu_x \in \mathcal M(E)$ for each $x \in E$. 

If i am talking about $m \in M$, then $m$ must be of the form $\mu\otimes x$ for some measure $\mu$ on $E$ and $x \in E$.



$I_1 = \text{Apple 1}$, $I_2 = \text{ Apple 2}$, $E=\{I_1, I_2\}$

$F(I_1) = \mu_1 \otimes I_1$, $F(I_2) = \mu_2\otimes I_2$.

$M = \mathcal M(E)\otimes E$.

$F_\text{johnny}(I_1) = \delta_{I_1}\otimes I_1$, $F_\text{johnny}(I_2)= \delta_{I_2}\otimes I_2$.

$F_{\text{Lea}}(I_1) = \left(\frac{1}{2}\delta_{I_1} + \frac{1}{2}\delta_{I_2}\right) \otimes I_1$







# Content and Context making sense

1) You are given a sample space $(\Omega,\mathcal F)$. 
   1)  You want to make it a topological vector space (the most general concept of vector space). 

Let $T$ be a topological vector space, and let $F_{\Omega \to T}$ be your favorate measurable map from $\Omega$ to $T$. Then Content space is $T(\Omega)$. 

Definition: $d$ is a metric on $T$ (a.k.a distance on $T$), if $d$ satisfies the following conditions:

1. $d(x,y) = 0$ if and only if $x = y$. 
2. $d(x,y) = d(y,x)$. 
3. $d(x,z)\le d(x,y)+d(z,y)$. 

## How content changes with time

Let $\{X_i\}_{i = 1}^\infty $ be a sequence of elements in $T$, i.e. $\{X_i\}_{i = 1}^\infty \subset T$ .

1. $X_1 $ can equal to $ X_2$ as element in $T$, but does not have to. 
2. $(X_1,1 ) \neq (X_2,2)$ but $X_1$ can equal to $X_2$ as elements in $T.$



## How we differentiate items

Let $T$ be content space, let $X$ be context space. The memory space $\mathcal M=T \otimes X$. Let $\{m_i\}_{i = 1}^\infty\subset \mathcal M$, where $m_i = t_i\otimes x_i$. Assume the followings:

There is a notion of "distance" in $T$ and $X$, call them $d_T$ and $d_X$. 

Then depending on the specific model, the "overall distance" must be of the form
$$
d_\text{over all}(m_i,m_j) = a_1d_T(t_i,t_j)+a_2d_X(x_i,x_j) + a_3d_{\text{time }}(i,j)
$$
for some $a_1,a_2,a_3 \ge 0$.

Theorem: There exists $c_1, c_2 > 0$  so that for all $x,y \in \R$, 
$$
c_2(|x|+|y|) \le \sqrt{x^2+y^2} \le c_1(|x|+|y|)
$$
**Case# 2**: $T$ and $X$ not "orthogonal". Then $\mathcal M = T\otimes X$, there is a distance on $\mathcal M$ itself, call it $d_\mathcal M$. Then overall distance of $m_i,m_j$ defined to be 
$$
d_{\text{overall}}(m_i,m_j) =a_1d_{\mathcal M}(m_i,m_j) +a_2 d_{time}(i,j)
$$


Let $B_t$ be $n$ dimensional brownian motion, 对于任意时间 $ t \ge 0$, $B_t \in \R^n$. 

$\R^2$ the $x$-axis is time, Q: what's negative time. 



### Concerns

1. Becasue they are metric space, is it true we require $d_T$ is indepenet of $d_X$?

2. If context space is the "space of measures", then how to understand "distance between measures"?



Answers: Yes, there are many metrics on the "space of measures on a set". 

e.g.

1. $d_{TV}(\mu, \nu) = \sup_{f \in \mathcal C, \|f\|_{\infty \le 1}} \left|\int f d\mu - \int fd\nu\right|$.

2. Weissenstrass distance 

**Simple case of $\delta$ measures**: $d_T(\delta_x,\delta_y) = |x-y|$. 

e.g. the total variation distance between $\delta_0$ and $\delta_{100}$, we look at the following expression for continuous functions $f$ with maximum of $f$ being 1. 
$$
\left|\int f(x) d\delta_0(x) - \int f(x) d\delta_{100}(x)\right|
$$

### Measurable space, measures and integral

Measurable space: $(\Omega, \mathcal F)$. 

Measure: on $(\Omega, \mathcal F)$, $\mu$. If a set $A \subset \Omega$ is measurable, then you can measure the "size" of $A$ under your "ruler" $\mu$. 

Integration of a measurable function $f$ against a measure $\mu$: $\int_\Omega f(x) d\mu(x)$



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





