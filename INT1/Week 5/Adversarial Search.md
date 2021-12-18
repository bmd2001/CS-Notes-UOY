A #GameTree is a #tree that maps all the possible routes the #game can take.

![Game Tree Example](GameTree.png)

A #solution instead is a double tuple in this format $(P1, (P2_1, P2_2))$, where the P2 values are the best choices for P2 for any single decision that P1 will make.

There are two possible #strategies that we could take:
1) #MaxMin: try to maximise the worst case scenario #payoff. In the example before the move A2 follows the #MaxMin strategy, because the worst payoff is 3 that, compared to -2 in the other subtree, is way higher.
2) #MinMax: try to minimise the opponent's #payoff. In the example above, it would be the same move as before. In a [[Intro to Game Theory#^c3d12b|zero-sum game]], this means that were minimising our **loss**.

These two #strategies will be used in our [[MinMax Algorithm|MinMax Search Algorithm]] that can help us parse a #tree to find the best #move we can take.
[[Uni Work Checklist|]]