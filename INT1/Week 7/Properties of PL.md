There are other three #properties that can be useful in PL:

1) #Equivalence
2) #Validity
3) #Satisfiability
</br>

### Equivalence

Two sentences are equivalent if this rule applies:

$$
p \equiv q \Longleftrightarrow(p \vDash q) \wedge(q \vDash p)
$$

$\vDash$ is the symbol of [[Reasoning with PL#^a31886|entailment]].
</br>

### Validity

The R propositions used in our #game are #valid only if they're always true, regardless of how the cells in the #game are arranged. These can always be true if you could say that they're the #rules of the #game. A #tautology is slightly different: this is a proposition that is always true, regardless of the model used (if we are in a #game or not). If you add a symbol to #tautology, it doesn't change the result of the #tautology.
</br>

### Satisfiability

Here, we're trying to find if a proposition is true in at least one model. It can become a difficult problem to solve, and in fact it was the first discovered #NP-complete #problem (https://www.britannica.com/science/NP-complete-problem) and it's called [[SAT Solving]]