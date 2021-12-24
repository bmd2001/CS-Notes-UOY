# Scheduling

## Overview

The reason we try to schedule #processes is that we want to maximize the #CPU utilization. To do so, we can have two types of systems:

1) Concurrent (all the tasks are managed by one #CPU #core)
2) Parallel (tasks are split into different #cores)

Computers have a mixture of both.
Usually, all processes have a cycle of using the #CPU and then waiting for #I/O.

To know if adding cores to the #CPU will make the system gain better performance, this formula can help:

$$\frac{1}{S+\frac{1-S}{N}}$$

S stands for the serial/concurrent component as a percentage, and N is the number of cores.

<br>

## CPU Scheduler

When the #CPU is in an idle state, the #OS will schedule process depending on a number of metrics. To do so, it can do it with or without interrupting the task if this is exceeding its allocated time slot (respectively #Preemptive and #Non-Preemptive #Scheduling). When the #scheduler knows what the #CPU should be running, the #dispatcher comes in and gives control to the #CPU to start with the next #process in the #schedule. This #dispatcher  should be very fast, so that the #dispatch #latency is the minimum it can be.

<mark> Definition</mark>: 

*Burst Time* = The time that the process take to execute

<br>

## Scheduling Algorithms

<br>

### FCFS (First Comes First Scheduling)
![[FCFS.gif|500]]

<br>

### SJF (Shortest Job First Scheduling)

![[SJF.gif|500]]

<br>

### Shortest Remaining Time First (With Preemption)

![[SRTF.gif|600]]

<br>

### Round Robin

Quantum is the maximum period of time that the #CPU can work on a single process, until it has to go to the next one.

![[RR.gif|600]]

<br>

### Priority Scheduling

With #Priority #Scheduling, we could have a slight problem: processes with the highest #priority could be stuck in an idle state for a very long time. To prevent that from happening, we can use a technique called #aging: this means lowering the priority number every time a process has been in an idle state for too long.

![[PS.gif|500]]

<br>

### Priority Scheduling with Round Robin

![[PSRR.gif|600]]

<br>

## IPC (Inter-Process Communication)

#Processes can be working on their own, or they can cooperate with each other. To do so, there has to an #IPC between the processes. 
There are two models of #IPC:

1) Shared memory
2) Message passing

![[IPC.png|600]]

### Shared Memory

As the name says, in this model, different #processes share a part of their #memory in a fixed #memory #address. To do so, the #processes involved have to request this need to the #OS (since, by default, sharing #memory is not possible), so they can then handle the communication between themselves. Usually, #processes that have this #IPC follow a #producer-consumer metaphor, where a #process produces information that is consumed by another #process.

Since the information is share, there has to be some sort of [[Synchronization]] between all the #processes.

<br>

### Message Passing

This other model makes #processes communicate through #messages. The ability to do so is conveyed by the #OS, that takes control of every aspect of the #message exchange #system.