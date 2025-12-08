# **TVA assumes that each object has its own _independent attentional weight_**

and that these weights are **scalars**, not functions over a space.

### TVA assumption:

Each object xxx has a weight:

wx=ηxπxw_x = \eta_x \pi_xwx​=ηx​πx​

No feature space is modeled.  
Objects do _not_ occupy regions in a representational space.  
Weights simply add:

∑wz=w1+w2+…\sum w_z = w_1 + w_2 + \dots∑wz​=w1​+w2​+…

This implicitly assumes:

> **Object representations are non-overlapping, independent units.**

---

# 🌐 **2. Your model introduces a different assumption:

Objects occupy measurable _regions_ in a representational space**

Objects are no longer independent scalars; they are **sets** in feature space:

Ex⊂ΩRE_x \subset \Omega_REx​⊂ΩR​

with a measure:

ν(Ex)\nu(E_x)ν(Ex​)

Once objects have spatial extent in representational space, the following becomes _inevitable_:

ν(E1∪E2)=ν(E1)+ν(E2)−ν(E1∩E2)\nu(E_1 \cup E_2) = \nu(E_1) + \nu(E_2) - \nu(E_1 \cap E_2)ν(E1​∪E2​)=ν(E1​)+ν(E2​)−ν(E1​∩E2​)

Thus:

> **Sub-additivity is not an assumption; it is a _mathematical consequence_ of treating objects as overlapping sets rather than independent scalars.**

This is the single, fundamental shift that makes your new prediction possible.

---

Your internal operations are:

$$wx=∫Exπ(ω)dμw_x = \int_{E_x} \pi(\omega)d\mu wx​=∫Ex​​π(ω)dμ$$

and

$$vx=C⋅wxν(∪Ez)v_x = C \cdot \frac{w_x}{\nu(\cup E_z)}vx​=C⋅ν(∪Ez​)wx$$​​