# Synchronization
<br>

## Overview

Before we start, we have to state a few definitions:

1) #Concurrency (the ability to make progress on multiple processes at the same time)
2) #Mutual #exclusion (MUTEX: it's a lock that makes sure that two processes don't use the same variable at the same time, causing the result of the program changing based on who got access to the variable first)
3) #Race #condition (occurs is when #MUTEX has to be enabled because of the reason written in the point before)
4) #Critical #section (it's the process' segment of code that can trigger a #race #condition, so no other process should be in it's #crititcal #section when another one is)

```clike
do {
	/* entry section */
		critical section
	/* exit section */
		remainder section
} while(true);
```

### Solutions Requirements for Critical Sections Problems

1) [[Synchronization#Requirements for Mutual Exclusion|MUTEX]]
2) Progress (if there aren't any processes in their #critical #section, the selection of the next process to enter the #crititcal #section cannot be postponed)
3) #Bounded #Waiting (there has to be a maximum number of times other processes enter their critical section when another one as requested to do the same, but its request hasn't been granted yet)

#Peterson's #Algorithm is a way to solve a #Critical #Section problem, even though it's not meant to be used on newer machines. This is how it works:

```c
boolean flag[2];
int turn;

void P0(){

	while(true){
		flag[0] = true;
		turn = 1;
		while(flag[1] && turn == 1){
			/* do nothing*/
		};
		/* critical section */
		flag[0] = false;
		/* remainder section */
		
	}
}

void P1(){

	while(true){
		flag[1] = true;
		turn = 0;
		while(flag[0] && turn == 0){
			/* do nothing */
		};
		/* critical section */
		flag[1] = false;
		/* remainder section */
		
	}
}

void main(){
	flag[0] = false;
	flag[1] = false;
	parbegin(PO, P1);
}
```
<br>

### Requirements for Mutual Exclusion

1) Only one #process can access their #critical #section at a time
2) A halting #process in their #non-critical #section can't affect other #processes
3) No [[Deadlocks]] or #Starvation 
4) #Bounded #Waiting 
5) No assumptions about processes' speeds
6) A #process stays in its #critical section for a limited amount of time