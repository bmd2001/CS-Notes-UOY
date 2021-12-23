The System Software is the main Software that allocates the #resources of a computer to the different programs.

The **Operating System** ( #OS ) instead, is the software that manages the #hardware and acts as an intermediary between user and computer.

This is the list of services of Operating Systems:

![[Operating Systems Services.png]]

A #system-call is a request (done at #user level) for a #kernel service (related to the hardware of the computer).

An example of a #system-call is when a printf statement in a C program is called. A #system-call is made to so that the computer can write what is needed to be printed back.

Code can be in one of these two modes:

1) #User mode (the code doesn't have direct access to the hardware)
2) #Kernel mode (the code has unrestricted access to the hardware)

Operating systems can also be of three different types:

1) #Open-Source (Linux)
2) #Closed-Source (Windows)
3) #Hybrid (macOS)

There are also 4 different types of #OS architecture:

1) #Monolithic
2) #Layered
3) #Micro-Kernel
4) #Hybrid 

## Monolithic

#UNIX #OS uses the #Monolithic approach: that means dividing the #OS into two blocks: 

1) System Programs
2) kernel

![[Monolithic.png|400]]

## Layered

The #Layered approach instead divides the #OS into multiple layers, each of them having gradually more access to the #hardware. Its structure is usually shown in a circle subdivided in different circular section.

*Example*:

![[Layered.png|400]]

## Micro kernel

Here, the #kernel is used as little as possible, so the components get to moved to user interface.

![[Micro Kernel.png|500]]

## Hybrid

The #hybrid approach is actually to use the positive aspects of all approaches into one. In fact, usually, #OSs are not a pure model.