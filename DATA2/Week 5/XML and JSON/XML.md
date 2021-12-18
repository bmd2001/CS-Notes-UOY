# What is #XML?

#XML stand for *Extensible Markup Language*
The #markup part of the acronym means that the code uses #tags to enclose information in them, like in #HTML:

```xml
<student>Tim May</student>
```

It can be understood by **every** programming language.
The #extensible part of the acronym instead means that the tags can be easily changed in three ways:

1) They're defined by the #user 
2) Their functionality are also defined by the #user
3) Their functionality is also extendable for the application requirements

#XML is also a language because, if we're using two applications that are exchanging data with each other and they work with different languages, they'll use #XML to convert the data easily. 
**Every comunicator between two applications, in fact, is called a programming #language.**

# Why do we use #XML ?

- To store and arrange the data.
- To describe the data. 
- To maintain text based database. 
- To transport the data from one application to another. 
- To simplify the creation of #HTML documents for large websites.


```xml
<?xml version = “1.0” encoding = “UTF-8”?>
<student_information>
	<name>Alan Smith</name>
	<course>Artificial Intelligence</course>
	<id>607545</id>
	<address>46 Warley Rd Newcastle</address>
</student_information>
````

# How to use #XML 

Basic concepts are like #HTML .
You can use a #browser or a text editor to easily write a #xml file.
#Attributes are the #classes or #ids that you would find in an #HTML file, but in this case you can name them in whatever way you want.
The difference between #attributes and #text in #xml is that #attributes are in the #tag, #text is between the #tags.
```xml
<test attribute = "attribute_value">This is the text, not an attribute</test>
````
#Comments are also like in #html:
```xml
<!--This is a comment-->
````
There are a few characters that can't be typed directly in xml, so we need to use some other character combinations:

| Characters | Replacement |
| ---------- | ----------- |
| >          | ``&gt;``    |
| <          | ``&lt;``    |
| &          | ``&amp;``   |
| '          | ``&apos;``  |
| "          | ``&quot;``  |

# What is a #XML #DTD file?

#DTD files can be used to define a #structure of a #xml file, so that you can declare all of the #tags and their #attributes.
Example of #dtd file:

```dtd
<!ELEMENT York_University (department+)>
<!ELEMENT department (location+, num_of_student+)>
<!ELEMENT location (#PCDATA)>
<!ELEMENT num_of_student (#PCDATA)>
<!ATTLIST department name CDATA #REQUIRED>
```

**N.B. See [[Lab 9 XML#^53d42b|week 5's practical]] to see what the #syntax means.**
This is a #external #private #dtd, but #dtd declarations can be done directly in the #xml file ( #internally ), using the following command:

```xml
<!DOCTYPE York_University[
<!ELEMENT York_University (department+)>
<!ELEMENT department (location+, num_of_student+)>
<!ELEMENT location (#PCDATA)>
<!ELEMENT num_of_student (#PCDATA)>
<!ATTLIST department name CDATA #REQUIRED>
]>
```

[[Uni Work Checklist|]]