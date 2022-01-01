# Variations on Turing Machines
<br>

## Non-Deterministic

*Example*:

![[Non-Deterministic Turing Machine.png|500]]

Here the language accepted is:

$$\mathrm{L}(M)=\Sigma^{*}\{abc,\ cab\}\Sigma^{*}$$

```ad-abstract
title: Theorem 1
collapse: closed
*For every Non-Deterministic Turing Machine $N$ there exist a Deterministic Turing Machine $D$ such that* $\mathrm{L}(N) = \mathrm{L}(D)$
```

---

## Linear-Bounded Automaton

It's defined as a #Turing #Machine, but the initial [[Lecture 4 Turing Machines#^753f16|configuration]] is as follows:

$$q_0 \langle \mathrm{w} \rangle$$

The $\langle \rangle$ are the extremes where the tape head can't go further. These extremes aren't overwritable.

```ad-abstract
title: Theorem 2
collapse: closed
*A language L is is accepted by some linear-bounded automaton if and only if L is context-sensitive.*
```

---

## Multitape Turing Machines

It's a normal #Turing #Machine but with multiple tapes instead of one.

The only thing that changes from a normal one is the transition function:

$$\delta:\left(Q-\left\{\mathrm{h}_{\mathrm{a}},\  \mathrm{h}_{\mathrm{r}}\right\}\right) \times \Gamma^{\mathrm{n}} \rightarrow Q \times \Gamma^{\mathrm{n}} \times\{\mathrm{L}, \mathrm{R}, \mathrm{S}\}^{\mathrm{n}}$$

A configuration, instead, is only a tuple of string for the state of each tape.

```ad-abstract
title: Theorem 3
collapse: closed
*For every multitape Turing machine N there exists a Turing machine M such that <br> $\mathrm{L}$(N) = $\mathrm{L}$(M).*
```

---

## Chomsky Hierarchy

| Type | Grammars/ Languages          | Grammar productions                                                                                                         | Machines                                                |
|:---- |:---------------------------- |:--------------------------------------------------------------------------------------------------------------------------- |:------------------------------------------------------- |
| 0    | *Unrestricted semidecidable* | $\alpha \to \beta$<br>$[\alpha \in(\mathrm{V} \cup \Sigma)^{+},$<br>$\beta \in (\mathrm{V}\cup \Sigma)^{*}]$                | *Turing machine* <br>(deterministic or <br> nondeterministic)    |
| **1**    | ***Context-sensitive***          | **$\alpha \to \beta$<br>$[\alpha , \beta \in(\mathrm{V} \cup \Sigma)^{+},$<br>$\mid \alpha \mid \ \leq \ \mid \beta \mid \ ]$** | ***Linear-bounded automaton***                           |
| 2    | *Context-free*               | $\mathrm{A} \to \beta$<br>$[\mathrm{A}\in \mathrm{V},\ \beta \in (V\cup\Sigma)^{*}]$                                        | *Pushdown automaton*                                    |
| 3    | *Regular*                    | $\mathrm{A} \to \mathrm{aB},\ \mathrm{A}\to \lambda$<br>$[\mathrm{A,\ B \in \ V, \ a \in \Sigma}]$                                                                    | *Finite automaton* <br>(deterministic or <br> nondeterministic) |
