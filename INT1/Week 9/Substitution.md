We can now use #quantifiers when we #tell something to the #KB. When doing so, though, we have to change the #ask action because, instead of returning a #boolean, we would like to have the #object returned.

A #substitution can be defined in this way:

If there's a formula $e = Brother(x, y)$, a #substitution is a set of values that x and y can have in one case, like $\theta = \{x/Richard, y/John\}$. This will give us this equation here:
$$\theta (e) = Brother(Richard, John)$$

$\theta (e)$ is called an instance of $e$. $e$ is called #ground if and only if there aren't any free variable and it's instance is called a #ground #instance.