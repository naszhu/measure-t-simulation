# first explore:
It took me some real efforts in thinking about this. Firstly, I figured the probelm we saw in last meeting, of why I had list 3 better than list 2 performance — Those are caused by a line of bug in strenghtening process that always fasely strengthens a mistaken trace.

  

Now, Ifixed the bug and got the a new prediction for initial test attached below followed by data for a comparison. A flat (or slightly descrease) of hit rate from list 2 to list 3 is shown. 

  

Now, let me explain, why though, the **expected list length effect is very small or close to none in current model** (from list 2 to list 3). (T**his explains in general why sometimes list length effect predicted by REM is very low).** 

1. Odds Phi follows log-normal distribution.
    
2. The current model simulation shows the mean of Phi (odds) in list 2 and 3 (given a target), is way way higher than criterion1. (for exmaple, E(Phi)=1e10 >>1)
    
3.  The variance of the odds is VERY big as well. As that I printed from the model, the variance could be even bigger than the mean of Phi.
    
4. Odds go lower from list 2 to list 3 when increase traces: Given target (only consider target test for now): The change of E(Phi) from list 2 to list 3 could be seen as changing from Lambda_a/N_a in list 2 to (Lambda_a+Lambda_b)/(N_a+N_b) in list 3. Lambda_a is a sum likelihood includes likelihood of the targeted item in trace given current test target and Lanbda_b will be the likelihood of a nontargeted item in trace given current test target. When expectation drops from list 2 to 3,  it means Lambda_a+Lambda_b)/(N_a+N_b) >  Lambda_a/N_a. It gives,  E(Phi) will decrease from list 2 to 3 when Lambda_b<(Lambda_a/N_a)*N_b. Because Lambda_a is that include the targeted item trace, this value will be about 10 times bigger than that lambda_b (targeted item trace likelihood is about 10 times bigger than non-targeted item trace likelihood). A change from Na to Nb is about 40 items to 60 items from list 2 to 3. Under this relationship and this model, E(Phi) necessarily go lower. 
    
5. The mean of odds (E(Phi)) go lower necessarilyfrom list 2 to list 3 shown in step 4, but Hit Rate P(Phi>1)  doesn't necessarily go lower in this distribution feature described in point 2 and 3
    
6. **Hit rate = P(Phi>1) = P(log Phi >0) = Phi_normal(mu/sigma)** => Hit rate depends on mu/sigma 
    

==> An abstract summary:, not rigorously mathmatically proved but I think it is the right trend: how P(Phi>1) change with decrease of E(Phi) could be dependent, and given the distribution, it could sometimes predict Hit rate to go lower, but other time, higher. 

  

I feel like this is how it goes and explains the flatness of Hit Rates in between-list predictions. Let me know -- or I can zoom to explain the above logic.

---
Hit rate = P(Phi>1) = P(log Phi >0) = Phi_normal(mu/sigma) 
The above is correct when Phi ~ lognormal (mu, sigma), but when log phi ~ normal (mu, sigma), another formula will be given 