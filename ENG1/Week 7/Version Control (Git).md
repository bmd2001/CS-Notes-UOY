They can help with collaboration on code, because rolling back to older, but working versions of code is very useful on a Software Engineering project. 
There have been versions of Version Control software from 1972. The most important ones now are Apache SVN and [[Version Control (Git)|Git]]

# Terms:
- #Repository: Where all the files are stored
- #Commit: Store a change to the #repository
- Commit N°: It's a version of the files
- #Branch: A path/directory where the #source #code of the #repository is the copied
- #Merge: Combine two paths
- #Conflict: Changes performed on the same files

# SVN

It's centralized (a single repository) and the repository has an ID that changes at every commit.

# Git

It's decentralized (multiple copies of the repository) and the ID of each copy is a 40 hex number. Every user has a local repository on their machine, and, when files have to be updated, they are updated on the global repository.