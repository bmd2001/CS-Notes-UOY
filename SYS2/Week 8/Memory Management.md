Programs have to be stored in #memory (main memory and registers) and place in a #process for it to be run.

![[Components.png]]

Every process has a base address and a limit (the process uses the addresses between base and base + limit).

There are three types of times when the addresses are set:
1) Compile time: you tell the exact address of the memory
2) Load time: you set a temporary address that is translated at compile time
3) Execution time: you haven't used addresses in the code, so it can easily be moved to any address

![[Address Binding.png|200]]

#Logical #addresses are some numbers that are different from the ones that the computer uses (like the indices of a list).

The #MMU (Memory Management Unit) is the hardware piece that translate the logical addresses to the physical addresses.

The #memory can be partitioned statically, so all the #memory is divided at system generation time. The partitions are can be bigger than the actual process size.

###### 15-11-2021

---

The #memory can be partitioned dynamically, with partition of the size of the #process. 
There are three #strategies for the dynamic approach:

1) First fit: first partition
2) Best fit: smallest partition first
3) Worst fit: biggest partition first

You can also use #swapping: that means that a process can be swapped out of the #memory to a backing store. The only con is that there's always going to be a transfer time. This is a #technique use by #OS only if the computer is very low on free memory.

There's also the #paging technique: partition the memory and the processes in small parts (in the second case, they're called #pages) so we can allocate them anywhere in memory:

![[Paging.png]]

Every #process has a #page #table that stores the values of the #indices:

![[Page Tables.png]]

The #addresses are relative to the page, though, so they're #logical #addresses. The #MMU will have to translate these #addresses too.

![[Paging Adresses.png|500]]

We can also use #segmentation, a #technique where the pages are instead called #segments, and they can all have different sizes. To do so, the addresses will have to store the size of the segment too.

![[Segmentation Addresses.png]]

The #resident #set is the portion of a process that is stored in memory. Now that we have these new #techniques, we don't have to store every part of process in memory.

###### 16-11-2021

---