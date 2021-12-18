# Lab Sheet

# Answers

1) These are the possible substitutions 
	1) $\theta = \{x/A\}$
	2) No substitution (the function is not the same)
	3) $\theta = \{x/y\}$ or $\theta = \{y/x\}$ (a term can also be substituted by another term)
	4) No substitution (x can't be taking two values)
	5) $\theta = \{\space y/f(x, A), \space z/B, \space w/B\}$
	6) No substitution (x can't be taking two values)

2) With this scenario
	1) This #KB can be described in this way:
		$$\text{Croaks}(f) \land \text{Eats}(f, Flies) \Rightarrow \text{Frog}(f)$$
		$$\text{Chirps}(c) \land \text{Sings}(c) \Rightarrow \text{Canary}(c)$$
		$$\forall c \space \text{Canary}(c) \Rightarrow \text{Yellow}(c)$$
		$$\forall f \space \text{Frog}(f) \Rightarrow \text{Green}(f)$$
		
	2) The statement is translated in this way: $\text{Croaks}(Fritz) \land \text{Eats}(Fritz, Flies) \Rightarrow \text{Green}(Fritz)$. The two proof are as follows:
		1) 
3) With this code, I implemented the statement above in python:
	1) 
		```python
		kb = createResolutionKB()



		flies = Constant('flies')

		frog = Variable('$frog')

		canary = Variable('$canary')

		Fritz = Constant('fritz')

		# define some functions...

		def Croaks(x):

		return(Atom('Croaks', x))



		def Eats(x, y):

		return(Atom('Eats', x, y))



		def Chirps(x):

		return(Atom('Chirps', x))



		def Sings(x):

		return(Atom('Sings', x))



		def Frog(x):

		return(Atom('Frog', x))



		def Canary(x):

		return(Atom('Canary', x))



		def Green(x):

		return(Atom('Green', x))



		def Yellow(x):

		return(Atom('Yellow', x))



		kb = createResolutionKB()



		tell_p(kb, Forall(frog, Implies(And(Croaks(frog), Eats(frog, flies)), Frog(frog))))



		tell_p(kb, Forall(canary, Implies(And(Chirps(canary), Sings(canary)), Canary(canary))))



		tell_p(kb, Forall(frog, Implies(Frog(frog), Green(frog))))



		tell_p(kb, Forall(canary, Implies(Canary(canary), Yellow(canary))))



		tell_p(kb, Croaks(Fritz))



		tell_p(kb, Eats(Fritz, flies))



		ask_p(kb, Green(Fritz))



		kb.dump()
		```
		
		The reply was:
		
		```bash
		1 Tell: Forall($frog,Implies(And(Croaks($frog),Eats($frog,flies)),Frog($frog)))

		>> I learned something.



		2 Tell: Forall($canary,Implies(And(Chirps($canary),Sings($canary)),Canary($canary)))

		>> I learned something.



		3 Tell: Forall($frog,Implies(Frog($frog),Green($frog)))

		>> I learned something.



		4 Tell: Forall($canary,Implies(Canary($canary),Yellow($canary)))

		>> I learned something.



		5 Tell: Croaks(fritz)

		>> I learned something.



		6 Tell: Eats(fritz,flies)

		>> I learned something.



		7 Ask: Green(fritz) ?

		>> Yes.

		==== Knowledge base [14 derivations] ===

		* Derivation(Or(Or(Frog($frog3),Not(Croaks($frog3))),Not(Eats($frog3,flies))), cost=0, permanent=True, derived=False)

		* Derivation(Or(Or(Canary($canary3),Not(Chirps($canary3))),Not(Sings($canary3))), cost=0, permanent=True, derived=False)

		* Derivation(Or(Green($frog6),Not(Frog($frog6))), cost=0, permanent=True, derived=False)

		- Derivation(Or(Or(Green($frog3),Not(Croaks($frog3))),Not(Eats($frog3,flies))), cost=1, permanent=True, derived=True)

		* Derivation(Or(Not(Canary($canary6)),Yellow($canary6)), cost=0, permanent=True, derived=False)

		- Derivation(Or(Or(Not(Chirps($canary3)),Not(Sings($canary3))),Yellow($canary3)), cost=1, permanent=True, derived=True)

		* Derivation(Croaks(fritz), cost=0, permanent=True, derived=False)

		- Derivation(Or(Frog(fritz),Not(Eats(fritz,flies))), cost=1, permanent=True, derived=True)

		- Derivation(Or(Green(fritz),Not(Eats(fritz,flies))), cost=2, permanent=True, derived=True)

		* Derivation(Eats(fritz,flies), cost=0, permanent=True, derived=False)

		- Derivation(Or(Frog(fritz),Not(Croaks(fritz))), cost=1, permanent=True, derived=True)

		- Derivation(Or(Green(fritz),Not(Croaks(fritz))), cost=2, permanent=True, derived=True)

		- Derivation(Green(fritz), cost=3, permanent=True, derived=True)

		- Derivation(Frog(fritz), cost=2, permanent=True, derived=True)
		```
	2) 
	```bash
		8      Ask:     Forall($frog,Eats($frog,flies)) ?
		>>      I dont know.
	```
	3) 
	```bash
		9 Ask: Exists($frog,Eats($frog,flies)) ?

		>>      Yes.
	```
	4) 

# Challenge

