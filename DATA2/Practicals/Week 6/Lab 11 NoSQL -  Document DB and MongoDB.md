# Lab Sheet

![[Lab 11 NoSQL - Document DB and MongoDB.pdf]]

# Answers

1) 
```bash
test> show dbs

**admin** 8.19 kB

**config** 12.3 kB

**local** 8.19 kB
```
2) 
```bash
test> use data2

switched to db data2
```
3) 
```bash
data2> db.createCollection("info")

{ ok: 1 }
```
4) 
```bash
data2> show collections

**info**
```
5)      
```bash
data2> db.info.insertOne({"_id":101, "name":"JS", "age":23, "course":"Computer Science"})

{ acknowledged: true, insertedId: 101 }
```
6) 
```bash
data2> db.info.insertMany([{"_id":102, "name": "SG", "age":19, "course": "Software Engineering"},{"_id":103, "name": "AS", "age":21, "course": "Artificial Intelligence"}])

{ acknowledged: true, insertedIds: { '0': 102, '1': 103 } }
```
7) 
```bash
data2> db.info.find()

[

	{ _id: 101, name: 'JS', age: 23, course: 'Computer Science' },

	{ _id: 102, name: 'SG', age: 19, course: 'Software Engineering' },

	{ _id: 103, name: 'AS', age: 21, course: 'Artificial Intelligence' }

]
```
8)	
```bash
data2> db.info.find({course:{$eq:"Computer Science"}})

[ { _id: 101, name: 'JS', age: 23, course: 'Computer Science' } ]
```
9) 
```bash
data2> db.info.find({age:{$gt:20}})

[

 { _id: 101, name: 'JS', age: 23, course: 'Computer Science' },

 { _id: 103, name: 'AS', age: 21, course: 'Artificial Intelligence' }

]
```
10) 
```bash
data2> db.info.find({course:{$nin:["Computer Science", "Artificial Intelligence"]}})

[ { _id: 102, name: 'SG', age: 19, course: 'Software Engineering' } ]
```
11) 
```bash
data2> db.info.find({$and:[{age:{$exists:true}},{age:{$ne:25}}]})

[

 { _id: 101, name: 'JS', age: 23, course: 'Computer Science' },

 { _id: 102, name: 'SG', age: 19, course: 'Software Engineering' },

 { _id: 103, name: 'AS', age: 21, course: 'Artificial Intelligence' }

]
```
12) 
```bash
data2> db.info.find({name:{$eq:"JS"}}, {course:1})

[ { _id: 101, course: 'Computer Science' } ]

data2> db.info.find({name:{$eq:"JS"}}, {course:1, _id:0})

[ { course: 'Computer Science' } ]
```
13)       
```bash
data2> db.info.find({course:{$eq:"Artificial Intelligence"}}).count()

1
```
14) 
```bash
data2> db.info.find().sort({age:-1})

[

 { _id: 101, name: 'JS', age: 23, course: 'Computer Science' },

 { _id: 103, name: 'AS', age: 21, course: 'Artificial Intelligence' },

 { _id: 102, name: 'SG', age: 19, course: 'Software Engineering' }

]
```
15) 
```bash
data2> db.info.find().limit(2)

[

 { _id: 101, name: 'JS', age: 23, course: 'Computer Science' },

 { _id: 102, name: 'SG', age: 19, course: 'Software Engineering' }

]
```
16) 
```bash      
data2> use HCI

switched to db HCI

HCI> use data2

switched to db data2

data2> db

data2
```
17) 
```bash
data2> db

data2

data2> use HCI

switched to db HCI

HCI> db

HCI

HCI> db.dropDatabase()

{ ok: 1, dropped: 'HCI' }

HCI> show dbs

**admin** 41 kB

**config** 111 kB

**data2** 73.7 kB

**local** 41 kB
```

[[NoSQL|]][[Document DB|]]