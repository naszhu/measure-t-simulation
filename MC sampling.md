- n Monte Carlo sampling you almost always start by drawing
    
    u  ∼  Uniform(0,1)
    
    sometimes called the **unit-uniform random variable** or **standard uniform variate**.
    
 it’s literally a single draw from the continuous distribution that puts equal mass on every sub-interval of $0,1$$0,1$$0,1$.
    
- Once you have u, you use it to pick one of your discrete outcomes by seeing **which slice of $0,1$$0,1$$0,1$** it falls into (slices sized by your weights).


e.g.,: [[Sampling]]: 

Partition $0,1$$0,1$$0,1$ into nnn intervals of length pip_ipi​:

![[Pasted image 20250619204411.png]]
  
  

Draw u∼Uniform(0,1).


Find the unique interval into which u falls.

  
  ![[Pasted image 20250619204429.png]]