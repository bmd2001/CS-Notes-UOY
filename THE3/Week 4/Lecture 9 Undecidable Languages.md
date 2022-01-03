# SA AND NSA

A #language is #Self-accepting if the encoded #Turing #machine is a string is a string accepted by the #Turing #machine itself. We can write this like:

$$
\mathrm{SA}=\{\mathrm{e}(M) \mid M \text { is a TM and e }(M) \in \mathrm{L}(M)\}
$$

^5b1f55

A #non-self-accepting language, instead, consists of all the encodings that are not accepted by their #TM and all the string with 0 and 1 that are not encodings of a #TM.
This, instead, is written like this:

$$
\begin{aligned}
\mathrm{NSA}=&\{\mathrm{e}(M) \mid M \text { is a TM and e }(M) \notin \mathrm{L}(M)\} \\
& \cup\left\{w \in\{0,1\}^{*} \mid w \neq \mathrm{e}(M) \text { for every TM } M\right\}
\end{aligned}
$$

```ad-abstract
title: Theorem 10
collapse: closed
NSA *is not [[Lecture 6 Semidecidable Languages and Language Enumeration#^f34ccb|semidecidable]]*
```

^0e46cf

```ad-abstract
title: Theorem 11
collapse: closed
SA *is not [[Lecture 7 Decidable Languages#^24c0d8|decidable]]*
```

^18bea8

```ad-abstract
title: Theorem 12
collapse: closed
SA *is [[Lecture 6 Semidecidable Languages and Language Enumeration#^f34ccb|semidecidable]]*
```

^cd5a1e

---

# Universal Turing Machines

A #Universal #TM takes as an input a #TM and a string $\mathrm{w}$ and it will accept them if the #TM accepts the string, it won't if the #TM doesn't accept the string.

We call this an #interpreter.