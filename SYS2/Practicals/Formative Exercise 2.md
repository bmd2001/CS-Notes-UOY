# Lab Sheet

![[SYS2_Exercise_2(1).pdf]]

# Answers

1) The answer is D because all the possible schedules are the permutations of the n processes, and the formula for permutations is $n!$.
2) 
	1) The four Gantt charts are:
		1) FCFS:
		
			![[Exercise 2 FCFS Scheduling.png]] 
		2) SJF:
		
			![[Exercise 2 SJF Scheduling.png]]
		3) Non-Preemptive (highest number in the priority table comes first):

			![[Exercise 2 Non-Preemptive Scheduling.png]]
			
		4) RR (Quantum = 2):

			![[Exeercise 2 RR.png]]
	2) The turnaround times are these:
		1) (5, 8, 9, 16, 20)
		2) (13, 4, 1, 20 , 8)
		3) (5, 20 , 13, 12, 17)
		4) (17, 12, 5, 20, 16)
	3) The waiting times are:
		1) (0, 5, 8, 9, 16)
		2) (8, 1, 0, 13, 4)
		3) (0, 17, 12, 5, 13)
		4) (12, 9, 4, 13, 12)
	4) The average waiting times are:
		(7.6, 5.2, 9.4, 10)
		The Algorithm with the smallest average waiting time is SJF.
1) From this table:

	|     |  Allocation  |     Max      |  Available   |
	|:---:|:------------:|:------------:|:------------:|
	|     | (A, B, C, D) | (A, B, C, D) | (A, B, C, D) |
	| T0  | (3, 1, 4, 1) | (6, 4, 7, 3) | (2, 2, 2, 4) |
	| T1  | (2, 1, 0, 2) | (4, 2, 3, 2) |              |
	| T2  | (2, 4, 1, 3) | (2, 5, 3, 3) |              |
	| T3  | (4, 1, 1, 0) | (6, 3, 3, 2) |              |
	| T4  | (2, 2, 2, 1) | (5, 6, 7, 5) |              |

	The answers are:
	1)
		$$T_2 \Rightarrow A = (2, 6, 3, 7)$$
		$$T_1 \Rightarrow A = (4, 7, 3, 9)$$
		$$T_0 \Rightarrow A = (7, 8, 7, 10)$$
		$$T_3 \Rightarrow A = (11, 9, 8, 10)$$
		$$T_4 \Rightarrow A = (13, 11, 10, 11)$$
	2) It can't because the allocation of T4 is too low for a request of (2, 2, 2, 4) and no thread can use the resources any more: $Allocation + Request \neq Max \Rightarrow (2, 2, 2, 1) + (2, 2, 2, 4) \neq (5, 6, 7, 5) \Rightarrow (4, 4, 4, 5) \neq (5, 6, 7, 5)$
	3) It can, since there's a safe sequence that the OS can choose from: it still the same as the first part but $T_2$ will request for a second time $(0, 0, 1, 0)$.
	4) It can, since there's a safe sequence that the OS can choose from, like freeing $T_3$ or restart with $T_2$.

[[Deadlocks|]]