# Processes

## Overview

A #process is a #program that is being executed, and it's #dynamic, so it's location varies in memory based on the need of the #OS. Since #programs can be executed multiple times, they can have multiple #processes at the same time.

A #process has multiple section:

1) The code's text
2) Data (variables)
3) #Heap (for storing operations)
4) Stack (for temporary variable or returned values)

In the #OS, processes are represented by a #PCB (Process/Task Control Block). The #PCBs store:

1) Process #state (new, ready, running, waiting, executed/terminated)
2) Program Counter
3) CPU Register and scheduling info
4) Memory organization data
5) #Accounting (the record-keeping and tracking of the system's activity)
6) #I/O Status

*Example*:

![[Process Parts.png|500]]

## Process Creation

When creating a #process, the #OS will create a new #pid (process ID) for it and add it to a #process table/tree. The #child #process will have all the data copied into it, apart from any shared memory. Its state will also be a **ready** state, and the #parent #process will store its child #pid.

*Example*:

![[Process Tree.png|500]]

## Process Deletion

When a #process terminates, it warns the #OS that it should be deleted, and it also will return a value (usually an integer) to the #parent #process that was waiting in the meantime. When it's deleted, the #process' resources will be re-allocated in the memory by the #OS too. 
A #parent #process could also abort a #child #process for multiple reasons:

1) #Child has too many resources allocated to it
2) The #child's task is no longer required
3) The parent needs to exit, but it can't do that if its children are still operating

---

# Threads

## Overview

A #Thread is the unit of #CPU the #process uses. Every #thread has a #TCB, that stores the same data as it's #parent #process, but it also stores it's #thread #priority. The thread keeps track of some data of the parent process too. They're usually implemented using #Thread #Libraries, such as:

1) POSIX Pthreads
2) Windows
3) Java

Threads can be at the #user level or at the #kernel level.

*Example*:

![[Process Execution Flow.png|500]]

![[User and Kernel Threads.png|500]]
<br>

## Single and Multi-threaded processes

![[Single and Multi-threaded processes.png|500]]

