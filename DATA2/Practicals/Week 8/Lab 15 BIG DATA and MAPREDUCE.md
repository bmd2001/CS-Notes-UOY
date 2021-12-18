# Lab Sheet

# Answers

1) 

```bash
[cloudera@quickastart ~]$ cat lab15.txt | python data2mapper.py
apple	1
banana	1
pear	1
plum	1
plum	1
pear	1
apple	1
banana	1
pear	1
```

2) 
```bash
[cloudera@quickastart ~]$ cat lab15.txt | python data2mapper.py | sort | python data2reducer.py
apple	1
apple	2
apple	2
banana	1
banana	2
banana	2
pear	1
pear	2
pear	3
pear	3
plum 	1
plum 	2
```

[[Big Data and its Challenges|]][[Dealing with Big Data|]]