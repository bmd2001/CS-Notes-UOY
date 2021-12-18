# Lab Sheet

# Answers

1)  $$
(a \Leftrightarrow b) \wedge(\neg b \vee \neg a)
$$
$$ ((a \Rightarrow b) \land (b \Rightarrow a)) \wedge(\neg b \vee \neg a)$$
$$ ((\neg a \lor b) \land (\neg b \lor a)) \wedge(\neg b \vee \neg a)$$
$$ (\neg a \lor b) \land ((\neg b \lor a) \wedge(\neg b \vee \neg a))$$
$$ (\neg a \lor b) \land (\neg b \lor (a \land \neg a))$$
$$ (\neg a \lor b) \land (\neg b) $$
$$ (\neg a \land \neg b) \lor (b \land \neg b) $$
$$ (\neg a \land \neg b) $$
2) </br>

![[DPLL.png]]

3)
 ```txt
(lab8.in)

~A ~B
~A B
A ~B
```

```bash
H:\Desktop\INT1\SAT\simple-sat-master\src>python sat.py -v --input tests/Lab8/lab8.in
Trying A = 0
Trying B = 0
Found satisfying assignment #1:
~A ~B
```

4)
This is the passed text file with the minimum colors possible (3):

![[colors input.rtf]]

After a few recursions, this is the output and it gives one of the possible solutions:

```bash 
H:\Desktop\INT1\SAT\simple-sat-master\src>python sat.py -v --input tests/Lab8/colors.in
Found satisfying assignment #1:
~R1 ~B1 G1 ~R2 B2 ~G2 ~R3 B3 ~G3 ~R4 B4 ~G4 ~R5 ~B5 G5 ~R6 ~B6 G6 ~R7 B7 ~G7 R8 ~B8 ~G8 ~R9 B9 ~G9 ~R10 ~B10 G10
```
The last line is translated with: 

$$(G, B, B, B, G, G, B, R, B, G)$$

![[colored_graph.png]]

These are all the other possible option for coloring the graph (168, where the first one is the one provided above):

![[colors ouput.rtf]]

