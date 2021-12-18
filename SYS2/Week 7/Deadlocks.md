A #deadlock is a permanent blocking of a set of #processes. A #set of #private are #deadlocked if every #process is blocked because they're waiting for another blocked #process.

A #system (like a computer) as multiple #resources.

There are four reasons for #deadlocks to happen:

![[DeadlockReasons.png]]
![[DeadlockPossibility.png]]

To handle #deadlocks there three #strategies:
 1) prevention
 2) avoidance
 3) detection

We can use a #resource #allocation #graph, that tells us the actions the #processes can do:

![[AllocationGraphs.png]]
</br>
## Deadlock Prevention

1) Mutual Exclusion: not required for #shareable #resources (read-only files)
2) Hold and Wait: make the process send a #request that specifies the resources needed. It can create #starvation.
3) No Preemption: 
4) Circular Wait:

Usually invalidating the circular waiting condition is the most used #strategy.
It can be done with assigning an #ID and make the #resources be only required in order.

```c
/* thread_one runs in this function */
void *do_work_one(void *param)
{
pthread_mutex lock(&first mutex);
pthread mutex lock(&second mutex);
/**
* Do some work
*/
pthread mutex-unlock(&second mutex);
pthread mutex-unlock(&first mutex);
pthread_exit(0);
}
/* thread_two runs in this function */
void *do_work_two(void *param)
{
pthread mutex lock(&second mutex);
pthread mutex.lock(&first mutex);
/**
* Do some work
*/
pthread mutex-unlock(&first mutex);
pthread_mutex-unlock(&second mutex);
pthread_exit(0);
}
```
In this example, only the first function will work because it follows that #strategy.
</br>
## Deadlock Avoidence

To avoid #deadlocks, the #resources have to be allocated carefully: to do so, the #processes have to declare the maximum number of #resources. After that, an #algorithm will examine this data to #allocate the #resources correctly.

The #avoidance #strategies have to avoid the computer to be in an #unsafe state, becuase in an #unsafe state there's a possibility for a #deadlock.

###### 08-11-2021

---

## Avoidence #Algorithms

There are two different types:

1) Single instance of resource type $\Rightarrow$ #Resource-allocation #graph
2) Multiple instances of resource type $\Rightarrow$ #Banker's #algorithm 
</br>

### Resource-allocation graph

![[ResourceAllocation.png|500]]

T1 can't request a resource R2 because it's being used by T2.
</br>

### Banker's algorithm

There are 4 data structures used for the #Banker's #algorithm (n = number or processes, m = number of resource types, i = index of processes, j = index of resources):

1) #Available: vector of lenght m, that gives the number of instances of a resource type
2) #Max: matrix[i, j] that gives max number that a process will request for a specific resource type
3) #Allocation: matrix[i,j] that gives allocated instances of a resource type
4) #Need: matrix[i, j] that gives the difference between #Max and #Allocation

This is a #Banker's #algorithm example:

![[Banker's Algorithm Example.png]]

![[Need table 1.png]]

To make a process get the resources, the process' row in the #Need matrix has to have every value that is less or equal to the correspondent value in the #Available #vector.
After that, the process will you use all the resources and return the resources back, so the #Available #vector will be modified with the sum of the requested resources and the already allocated ones.

###### 09-11-2021

---

# Deadlock Detection

To detect #deadlocks, we can use some graphs where the #nodes are the #processes and the #resources and the #vertices are directed from a process to a resource that is being requested by the process. 

![[Graphs.png]]



###### 15-11-2021
 
