# Functions
<br>

## Computable Functions

We can use #TM to also #compute #functions, that from an input of a string, that is the [[Lecture 4 Turing Machines#^753f16|configuration]] of the tape at the start, will give the [[Lecture 4 Turing Machines#^753f16|configuration]] of the tape when the #TM reaches the $\mathrm{h_a}$.

```ad-warning
If the #TM doesn't reache the $\mathrm{h_a}$ , then the function is #undefined for that input.
```

We can write how the #function works in this way:

$$
f_{M}(x)=\left\{\begin{array}{cl}
y & \text { if } q_{0} \Delta x \vdash^{*}\mathrm{h_a}\Delta y \text{ for some } y \in \Sigma^* \\
\text { undefined } & \text { otherwise }
\end{array}\right.
$$

This #function could also take in more arguments:

$$
f_{M}\left(x_{1}, \ldots, x_{k}\right)=\left\{\begin{array}{cl}
y & \text { if } q_{0} \Delta x_{1} \Delta x_{2} \ldots \Delta x_{k} \vdash^{*} h_{\mathrm{a}} \Delta y 
 \text { for some } y \in \Sigma^{*} \\
\text { undefined } & \text { otherwise }
\end{array}\right.
$$

All the strings inputted in the #function will be seen as string divided by $\Delta$ symbols on the tape in the initial [[Lecture 4 Turing Machines#^753f16|configuration]].

A #function of the second form is #computable if there's a #TM that gives back the same output, has its #function written in the first way.

*Example*:

![[Computable FM.png|500]]

This #TM computes the #function:

$$  
f(x)=\{\begin{array}{cl}\text{if x\%2 then 1, else 0}
\end{array}$$
---
## Characteristic function of a language

A #characterisitc #function of a #language outputs two different string created from $\Sigma^*$ depending on if the input string is part of a #language or not.

$$
\chi_{L}(x)= \begin{cases}w_{1} & \text { if } x \in L, \\ w_{2} & \text { otherwise }\end{cases}
$$

```ad-abstract
title: Theorem 15
collapse: closed
*A language $L$ is decidable if and only if its characteristic function $\chi_{L}$ is computable.*
```

^b5343f

---

## Graphs

The #graph of a #function is a set defined in this way:

$$
\operatorname{Graph}(f)=\left\{(v,\ w) \in \Sigma^{*} \times \Sigma^{*} \mid f(v)=w\right\}
$$

This can be turned into a language with # as a #separator between the two strings:

$$
\operatorname{Graph}_{\#}(f)=\{v \# w \mid(v, w) \in \operatorname{Graph}(f)\}
$$

```ad-abstract
title: Theorem 16
collapse: closed
*A partial function $f:  \Sigma^\ast \to \Sigma^\ast$ is computable if and only if $\operatorname{Graph}_{\#}(f)$ is [[Lecture 6 Semidecidable Languages and Language Enumeration#^f34ccb|semidecidable]].*
```

^c1e886

```ad-abstract
title: Theorem 17
collapse: closed
*A total function $f:  \Sigma^\ast \to \Sigma^\ast$ is computable if and only if $\operatorname{Graph}_{\#}(f)$ is [[Lecture 7 Decidable Languages#^24c0d8|decidable]].*
```

^440173
