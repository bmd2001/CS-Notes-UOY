[[XML|]][[XML and Python|]]
1) **We have a root ‘cars’ with two child elements – ‘car’. For each child there is a sub-child element for make, model, colour, and mileage. Content for the first child: For make it is bmw; for model it is 6 series; for colour it is blue; and for mileage it is mileage<10000. Similarly, content for the second child: for make it is merc, for model it is CLA, for colour it is grey; for mileage it is mileage<15000.**
	<br/><br/>
	*Answer:*

	```xml
		 <?xml version="1.0" ?> 
		<!-- The following information is about cars
		  --> 
		<cars>
			<car>
			  <make>bmw</make> 
			  <model>6 series</model> 
			  <colour>blue</colour> 
			  <mileage>miliage%It10000</mileage> 
			</car>
			<car>
			  <make>merc</make> 
			  <model>CLA</model> 
			  <colour>grey</colour> 
			  <mileage>mileage%It15000</mileage> 
			</car>
		</cars>
	```
	<br/><br/>

2) **Refer to the following xml elements:**

	```xml
	<?xml version = "1.0" encoding = "UTF-8"?>
	<York_University>  
	  <department name ="CS">
		<location>East Campus</location>
		<num_of_student>2000</num_of_student>
	  </department>
	  <department name =“PE”>
		<location>West Campus</location>
		<num_of_student>1000</num_of_student>
	  </department>
	</York_University>
	```


	**If you are asked to go back and create an external (Private) Document Type Definition (DTD) for the above XML elements, how would you proceed?**
		<br/><br/>
	*Answer:*
	
	The .dtd file is like this:
	
	```dtd
	<!ELEMENT York_University (department+)>
	<!ELEMENT department (location+, num_of_student+)>
	<!ELEMENT location (#PCDATA)>
	<!ELEMENT num_of_student (#PCDATA)>
	<!ATTLIST department name CDATA #REQUIRED>
	```
	
	And in the .xml this line is added on the top:
	
	```xml
	<!DOCTYPE York_University SYSTEM "H:\Desktop\York_University.dtd">
	```
	<br/><br/> ^53d42b
3) **Write an XML file for the following XML elements in python. Name your XMF file: xml2.**

	```xml
	<York_University>  
	  <department name ="CS">
		<location>East Campus</location>
		<num_of_student>2000</num_of_student>
	  </department>
	  <department name = “PE”>
		<location>West Campus</location>
		<num_of_student>1000</num_of_student>
	  </department>
	</York_University>
	```
	<br/><br/>
	*Answer:*
	
	The content of the notebook file is:
	
	```python
	import xml.etree.ElementTree as xmldoc
	root = xmldoc.Element("York_University")
	department1 = xmldoc.Element("department")
	location1 = xmldoc.Element("location")
	num_of_student1 = xmldoc.Element("num_of_student")
	location1.text = "East Campus"
	num_of_student1.text = "2000"
	department1.set("name", "CS")
	department2 = xmldoc.Element("department")
	location2 = xmldoc.Element("location")
	num_of_student2 = xmldoc.Element("num_of_student")
	location2.text = "West Campus"
	num_of_student2.text = "1000"
	department2.set("name", "PE")
	department1.append(location1)
	department1.append(num_of_student1)
	root.append(department1)
	department2.append(location2)
	department2.append(num_of_student2)
	root.append(department2)
	tree= xmldoc.ElementTree(root)
	tree.write("/Users/bre.xit/Desktop/Uni Documents/Second Year/DATA2/xml2.xml")
	```
	<br/><br/> ^98ead2
4) **We are now going to read an xml file (xmldoc), created earlier in Exercise 10.3, 1. We can read a file using the root.**

	```python
	import xml.etree.ElementTree as xml
	tree=xml.ElementTree(file='xmldoc.xml')
	root=tree.getroot()
	tagforroot=root.tag
	print(tagforroot)
	# The output was: student #
	for child_element in root:
    	print(child_element.tag)
	# The output was:
	# name Alan Smith
	# id 607545
	```
	<br/><br/>
5) **You are now going to read an xml file (xml2), created earlier in Exercise 10.3, 2.**<br/><br/>
	1. Show the code to read and display the root:
		
		```python
		tree = xml.ElementTree(file = "/Users/bre.xit/Desktop/Uni Documents/Second 	Year/DATA2/xml2.xml")
		root = tree.getroot()
		print(root.tag)
		````
		<br/><br/>
	2. Show the code to read and display the attribute name and value for each child:
		
		```python
		for department in root:
    		print(department.attrib)
		```
		<br/><br/>
	3. Show the code to read and display the attribute value for each child:
		Knowing the attribute name from before, we can use this method:
		
		```python
		for department in root:
    		print(department.get("name"))
		```
		</br></br>
	4. Show the code to read and display the sub-child elements along with their content. You should get a result like this:

		```python
		for department in root:
    		for child in department:
        		print("%s: %s"%(child.tag, child.text))
		````