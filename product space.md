[[outer product]]  
[[Space]]
is also [[function space]]
乘积是面积 画xy轴cover所有xy轴区域，x×y 是所有连线的点的数量 连续值为面积
### Product space
Given two sets $A$ and $B$:

$$
A \times B = \{(a,b) \mid a\in A, b\in B\}
$$

Each element $(a,b)$ can be viewed as a **function**  
$$
f:\{1,2\}\to A\cup B, \quad f(1)=a,\ f(2)=b.
$$

Hence:  
- The *pair (a,b)* is one *function* that selects one value from each set.  
- The whole Cartesian product $A×B$ is then the *set of all such 2-point functions*.  

So yes: **product space = function space from an index set to component sets.**

---

## 2. Generalization

For any family of sets $\{X_i\}_{i\in I}$:  
$$
\prod_{i\in I} X_i = \{f : I \to \bigcup_{i\in I} X_i \mid f(i)\in X_i\ \forall i\}
$$

This is the **general product definition in set theory**,  
and it *is* exactly a **function space** over index set $I$.  

- Domain of functions → index set $I$ (labels of coordinates)  
- Codomain → union of all $X_i$  
- Constraint → each coordinate must land in the corresponding component $X_i$

So when $I=\{1,2\}$, this reduces to your intuition:  
each “line” (pair) is a function assigning coordinate 1 → some A-value, coordinate 2 → some B-value.  

### spatial view 
![[Pasted image 20251014124658.png]]
### Set theory view
![[Pasted image 20251014124709.png]]
- Elements are **pairs** $(x,y)$.

- The dimensions are **glued together**; each element carries one coordinate from each domain.

- If $X$ and $Y$ are vector spaces, the *tensor product* $X\otimes Y$ or the *Cartesian product* $X\times Y$ creates a **joint coordinate system**.

- Dimension = $\dim(X)\times\dim(Y)$.

- Typical operation: joint similarity or distance

  

$$

d((x_1,y_1),(x_2,y_2)) = d_X(x_1,x_2) + d_Y(y_1,y_2).

$$

  

**Cognitive meaning:**

Context and content are *fused*: every memory trace is stored as one point $(c_i,f_i)$ in a joint coordinate system.


[[sum space]]