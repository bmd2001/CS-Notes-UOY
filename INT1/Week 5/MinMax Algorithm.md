It's easier to apply it on #Zero-Sum #games. The two #players are called #Max and #Min. #Plyes are the #half-turns, so in this example this is a 2 #ply tree (because, to complete a #game's turn, both the #players have to take an action).

The #MinMax #algorithm works thanks to #recursion: in fact, we need to reach our #terminal-nodes (the #leaves) and compute the #min and #max values.

![MinMax Tree](MinMax.png)

The numbers at the #nodes of the #tree are the actions taken by the two #players, where #Min tries to take the minimum value and #Max the maximum value. 

The #MinMax #algorithm is not very efficient if implemented naively with more complex #games like chess.

To guide our #search, we need some sort of [[Informed search and heuristics|heuristic]] called #Evaluation #Function. They affect the quality of our solution way more than a normal #heuristic.

The factors that make good an #evaluation #function are:

1) It agrees with the #payoff #function at the #terminal-nodes 
2) Not complex to compute
3) It reflects the chances of winning accurately

The #pseudocode of this #algorithm will be written like this:

```{r, tidy=FALSE, eval=FALSE, highlight=FALSE }
FUNCTION MinimaxDecision {
	For each a in Actions do {
		VALUE[a] MinimaxValue (Apply(a, InitialState))
	}
	return a with maximum Value [a]
}
FUNCTION MinimaxValue (state) {
	If TerminalTest (state) then return Utility (state)
	else if Max is to move in state then
	return the highest MinimaxValue of Successors (state)
	else return the lowest MinimaxValue of Successors (state)
}
```