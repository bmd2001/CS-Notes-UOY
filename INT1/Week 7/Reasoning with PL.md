To #deduce facts about our world, we can use #entailment ($p\models q$) that means that if p is true, q can't be false. To do so, we have to check that the entailment between our #Knowledge #Base and the question we're asking is there. ^a31886

To do so, we have to have a #KB that is correct, so every statement is proven and true. These are the statements that our #KB knows and are verified by the rules of the [[Representing Knowledge in PL#^4dd056|game]].

$$
\begin{aligned}
&R_{1}: \neg P_{1,1} \\
&R_{2}: B_{1,1} \Longleftrightarrow\left(P_{1,2} \vee P_{2,1}\right) \\
&R_{3}: B_{2,1} \Longleftrightarrow\left(P_{1,1} \vee P_{2,2} \vee P_{3,1}\right) \\
&R_{4}: \neg B_{1,1} \\
&R_{5}: B_{2,1}
\end{aligned}
$$

Then, knowing this information, we can create truth tables to know more about the #world:

![[TruthTable.png]]

In this case, we can see that we have some #knowledge now of where the components of the #game are, but we're not sure of everything ($P_{2,2}, P_{3,1}$).

We can also use #inference, the technique of modifying Propositional Logic sentences to get meaningful information, like in this example:

![[Inference.png]]

To do so with a computer, it will have to apply [[Depth First Search]] for every possible combination, making it very slow.