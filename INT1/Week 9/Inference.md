We can now use inference and [[Substitution]] to eliminate #quantifiers. In fact we can translate the #existential #quantifier in this way:

$$\exists x \space\text{Crown}(x) \land \text{OnHead}(x, John)$$$$\text{Crown}(C1) \land \text{OnHead}(C1, John)$$

Instead, for the #universal #quantifier, we can substitute all the values that x can have.

In this way, we can translate our #KB in #PL terms if we need to.

#Unification returns the values of the terms, such as two sentences are equal:

$$\text{Unify}(\text{Knows}(John, x), \text{Knows}(y, Bill) = \{y/John, x/Bill\}$$

If the variables are the same, we can change one of them, so we can easily find a unification. This action is called **standardizing apart**.