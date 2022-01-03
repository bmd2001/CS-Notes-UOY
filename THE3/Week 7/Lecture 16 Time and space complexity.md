# Time and space complexity
<br>

## Time

#Time #complexity is the function $\tau_M(n)$ that outputs the maximum number of #transitions of a string of length $n$ on the #TM $M$.

```ad-warning
We're only considering #TM that #halt on every #input.
```

---
## Space

#Time #complexity is the function $\mathrm{S}_M(n)$ that outputs the maximum number of tape squares that the #TM $M$ can visit with #input $n$

```ad-warning
For [[Lecture 5 Variations on Turing Machines#Multitape Turing Machines|Multitape TM]] the #space #complexity is the maximum for every single tape, so a series of equations that differ only by the constant value.
```

```ad-warning
This formula is always true:
$$\mathrm{S}_M(n)\leq \tau_M(n) + 1$$

```
---
## Growth rate of functions

Suppose we have two #functions ($f$ and $g$) and two integers ($c$ and $\mathrm{n_0}$). $f \in O(\mathrm{n})$ only if, for every value of the two integers, this is always true:

$$f(\mathrm{n}) \leq c \bullet \ g(\mathrm{n}) \ \ \text{for all } \mathrm{n\geq n_0}$$

##### Big-O Hierarchy
<br>

| Ordinal Number | Order                              | Name                             |
|:--------------:| ---------------------------------- | -------------------------------- |
|       1        | $\mathrm{O(1)}$                    | constant                         |
|       2        | $\mathrm{O(log_a}(n))$             | logarithmic ($\mathrm{a} > 1$)   |
|       3        | $\mathrm{O(}n)$                    | linear                           |
|       4        | $\mathrm{O(}n\ \mathrm{log_a(}n))$ | $n\ \mathrm{log}\ n$             |
|       5        | $\mathrm{O(}n^2)$                  | quadratic                        |
|       6        | $\mathrm{O(}n^3)$                  | cubic                            |
|       7        | $\mathrm{O(}n^r)$                  | polynomial ($\mathrm{r} \geq 4$) |
|       8        | $\mathrm{O(}b^n)$                  | exponential ($\mathrm{b} > 1$)   |
|       9        | $\mathrm{O(}n!)$                   | factorial                        |

---
## Properties of time complexity

```ad-abstract
title: Theorem 20
collapse: closed
*For every k-tape #TM $\mathrm{M}$ there is a #TM $\mathrm{M^′}$ such that: $$L(\mathrm{M}') = L(\mathrm{M}) \ \land \ \tau_{\mathrm{M^′}} \in O(\tau_{\mathrm{M}}^2)$$*
```

^30677e

```ad-abstract
title: Theorem 21
collapse: closed
*Let $f : \mathbb{N} \to \mathbb{N}$ be a total computable function. Then there is a decidable language $L$ such that for every #TM $\mathrm{M}$ accepting $L$, $\tau_{\mathrm{M}}$ is not bounded by $f$.*
```

^e92ff3

```ad-abstract
title: Theorem 22
collapse: closed
*There is a decidable language $L$ such that for every #TM $\mathrm{M}$ accepting $L$, there is a #TM $\mathrm{M^′}$ such that:
$$L(\mathrm{M^′}) = L(\mathrm{M}) \ \land \ \tau_{\mathrm{M^′}}  \in \mathrm{O(log_2(\tau_{\mathrm{M}}))}$$*
```

^d0abe5

