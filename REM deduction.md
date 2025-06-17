## Deduction of original REM
[[REM]]
[[Original REM deduction]]
[[Explain - Why not M but n]]
[[REM temp save 1]]


: [[Law of Total Probability]], [[Bayes Rule]]



[[Deduction version 1]]
[[deduction version 2]]




$$
\begin{align}
\frac{P(O|D)}{P(N|D)} &= \frac{P(D|O)}{P(D|N)}\\
&= \frac{\sum_{j=1}^m{P(D|Sj)P(Sj)}}{P(D|N)} \\
&=\frac{1}{n}\frac{\sum_{j=1}^m{P(D|Sj)}}{P(D|N)} \\
&= \frac{1}{n}\sum_{j=1}^m\frac{{P(D|Sj)}}{P(D|Nj)} \\
&=\frac{1}{n}\sum_{j=1}^M\frac{{P(D_j|Sj)\ \Pi_{i\neq j}^MP(Di|N_i) }}{x\left[{P(D_j|Sj)\ \Pi_{i\neq j}^MP(Di|N_i) } \right] + (1-x) \Pi_{i=j}^MP(Di|N_i)   }\\
&=\frac{1}{n} \sum_{j=1}^M \frac{{P(D_j|S_j)/ P(Dj|Nj) }}{x\left[{P(D_j|Sj)\ / \ P(D_j|N_j) } \right] + (1-x)  }\\
&=\frac{1}{n}\sum_{j=1}^M
\end{align} 
$$
$$
\frac{P(O \mid D)}{P(N \mid D)} = \frac{P(D \mid O)}{P(D \mid N)} 
$$