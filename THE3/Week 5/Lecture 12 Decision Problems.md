# Decision Problems

<br>

## Definition

A #decision #problem is a set of question that have 'yes' or 'no' as answers. The questions are #instances of the #problem. The #yes-instances and #no-instances are sets that contain all the inputs that gave output yes or no for the specific question.

*Example*:

![[Decision Problem.png|500]]

---
## Encoding

| Symbol                                                | Meaning                 |
| ----------------------------------------------------- | ----------------------- |
| $I$                                                   | Instance                |
| $P$                                                   | Problem                 |
| $\mathrm{Y}(P)$                                       | Encoded yes-instances   |
| $\mathrm{N}(P)$                                       | Encoded no-instances    |
| $\mathrm{E}(P) = \mathrm{Y}(P)\ \cup \ \mathrm{N}(P)$ | All Encodeded instances

All the #instances can be encoded, only if the encoding follows certain rules:

1) $\mathrm{Y}(P)\ \cap \ \mathrm{N}(P) = \emptyset$
2) $\mathrm{E}(P)$ is #decidable
3) If we know that $w$ is an encoding of the encoding #algorithm, then there's an #instance $I$ that accepts it ( $\text{enc}(I) = w$ ).

---

## Decidable and semidecidable problems

$P$ is #decidable if $\mathrm{Y}(P)$ is, otherwise it's #undecidable.
$P$ is #semidecidable if $\mathrm{Y}(P)$ is.

The complement of a problem ( $\overline{\rm P}$ ) is obtained by swapping the #yes-instances with the #no-instances.

```ad-abstract
title: Theorem 18
collapse: closed
*If a decision problem $P$ is [[Lecture 7 Decidable Languages#^24c0d8|decidable]], then its complement $\overline{\rm P}$ is also [[Lecture 7 Decidable Languages#^24c0d8|decidable]].*
```

^51790f

The #SAP (self-accepting #problem) is the problem where we ask ourselves if an encoded #TM is accepted by itself. But we can find that:
$$
\mathrm{SAP}=\{\mathrm{e}(M) \mid M \text { is a TM and e }(M) \in \mathrm{L}(M)\} = \mathrm{SA}
$$

(You can see that the equation is the same [[Lecture 9 Undecidable Languages#^5b1f55|here]])

```ad-abstract
title: Theorem 19
collapse: closed
*The self-accepting problem is undecidable but semidecidable*
```

^174b95
