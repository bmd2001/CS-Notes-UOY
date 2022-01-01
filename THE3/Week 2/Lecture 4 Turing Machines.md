# Turing Machines

In 1928, [David Hilbert](https://it.wikipedia.org/wiki/David_Hilbert) formulated the "Decision Problem": is there an #algorithm that can determine if a formula is universally valid or not.
[Alan Turing](https://it.wikipedia.org/wiki/Alan_Turing) negatively answered this question, using #Turing #Machines.

<br>

## Turing machines in detail

A #Turing #Machine is a 5-tuple $\left(Q,\ \Sigma, \ \Gamma,\ q_{0}, \ \delta\right)$, where:

1) $Q$ is the finite set of states (with $(\mathrm{h}_{\mathrm{a}},\ \mathrm{h}_{\mathrm{r}})$ being the halting accepting and rejecting states)
2) $\Sigma$ is the #input #alphabet
3) $\Gamma$ is the tape #alaphabet, so $\Sigma \subseteq \Gamma - \{\Delta\}$
4) $q_{0}$ is the initial state
5) $\delta:\left(Q-\left\{\mathrm{h}_{\mathrm{a}}, \ \mathrm{h}_{\mathrm{r}}\right\}\right) \times \Gamma \rightarrow Q \times \Gamma \times\{\mathrm{L}, \ \mathrm{R}, \ \mathrm{S}\}$ is the transition function

A Turing machine can move and overwrite things on the tape.

A #configuration is a string that specifies the state the tape is in. ^753f16

*Example*:

![[Configuration.png]]

The #configuration of this state is $\Delta \mathrm{acbb} q \mathrm{ac}$.

A #transition is described with this symbol: $\dashv$.


This is how an accepted #language is defined:

$$\mathrm{L}(M)=\left\{w \in \Sigma^{*} \mid q_{0} \Delta w \vdash^{*} u \mathrm{~h}_{\mathrm{a}} v\right. \ \text{ for some} \ \left.u, v \in \Gamma^{*}\right\}$$

The #language is the form to generalize the accepted strings.

A string is accepted if it reaches the halting state $\mathrm{~h}_{\mathrm{a}}$

*Example*:

**Turing Machine as an automata**:

![[Simple Turing Machine.png]]

It's accepted #language is:

$$\mathrm{L}(M)=\{a,\ b\}^{*}\{aa\}\Sigma^{*}$$