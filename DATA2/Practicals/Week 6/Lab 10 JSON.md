# Lab Sheet
![[Lab 10 JSON.pdf]]

# Answers

1) 
 
 ![[Exercise 1 answers.json]]
 
 2)
 
  	```jupyter
	import json
	with open("/Users/bre.xit/Desktop/Uni Documents/Second Year/CS 2021/2022/DATA2/Practicals/Week 6/ex1.json") as jsonfile:
    	ex1 = json.load(jsonfile)
	print(ex1)
	print("\n")
	print(ex1["lecturer"])
	print("\n")
	print(ex1["lecturer"][0])
	print("\n")
	print(ex1["lecturer"][1]["room"])
	print("\n")
	print([student["name"] for student in ex1["student"]])
	```

3) 
	```jupyter
	ex1["rank"] = 19
	print(ex1)
	for student in ex1["student"]:
    	del student["age"]
	print(ex1["student"])
	```

4) 
	```jupyter
	with open("/Users/bre.xit/Desktop/Uni Documents/Second Year/CS 2021/2022/DATA2/Practicals/Week 6/ex1new.json", "w") as newfile:
    	json.dump(ex1, newfile)
	```
	
5)
	 ```jupyter
	 a = """{
	"store": "Tesco Express",
	"id": "T12588",
	"location": "Clifton Moore",
	"payment methods": {
	"method1": "cash",
	"method2": "debit card",
	"method3": "credit card",
	"method4": "cheque",
	"method5": "tesco vouchers"
	},
	"cash machine": null,
	"24 hours": false
	}"""
	b = json.loads(a)
	print(b)
	print("\n")
	print(b["store"])
	```

6)
	 ```jupyter
	 c = json.dumps(b)
	 print(c)
	 with open("/Users/bre.xit/Desktop/Uni Documents/Second Year/CS 2021/2022/DATA2/Practicals/Week 6/jsontopython.json", "w") as file:
    	json.dump(c, file)
	```

[[JSON|]]
	 
	