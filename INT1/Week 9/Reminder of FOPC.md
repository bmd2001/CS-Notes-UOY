We can't use add in the #KB, if we use #Propositional #Logic, statements that were true for multiple squares on the board (like "There a breeze if and only if there's a pit in one of the adjacent squares") but about a specific square (listing all the positions of the breeze).
These are the differences:
$$
\begin{aligned}
B_{x, y} & \Longleftrightarrow\left(P_{x, y+1} \vee P_{x, y-1} \vee P_{x+1, y} \vee P_{x-1, y}\right) \\
B_{2,2} & \Longleftrightarrow\left(P_{2,3} \vee P_{2,1} \vee P_{3,2} \vee P_{1,2}\right)
\end{aligned}
$$

Because of this, the #KB has multiple rules that are repeated.

An #atomic #sentence, in #First-Order #Predicate #Logic,  is a sentence that can describe a fact about the world. In atomic sentence, there are two types of "symbols", that can relate to what #functions are in programming:

1) Predicate symbols (functions that "return" a #boolean: **Brother(Richard, John)** )
2) Function Symbols (functions that "return" an #object: **Father(Richard)** )

The #terms can be #variables (x) or #constants (Richard).

#Quantifiers used in THE1 (like $\exists x$ or $\forall x$) can be used to build our #KB.