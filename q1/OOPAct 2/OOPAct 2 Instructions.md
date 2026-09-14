My OOP Seed System - Part II 
Bringing your Class to Life 
Learning Objective 
At the end of the activity you should be able to: 
1. Convert your existing UML class design into a working Python class. 
2. Distinguish between public and private attributes. 
3. Implement attributes and methods using appropriate Python syntax. 
4. Use __init__() to initialize objects. 
5. Instantiate multiple independent objects from one class. 
6. Use methods to safely modify the state of an object. 
7. Update your UML class diagram to show visibility modifiers. 
------------------------------------------------------------------------------------------------------------------>>>>>> Your Task You already designed your own class in My OOP Seed System - Understanding Classes and Objects. Do not create a new class for this activity. 
You will now take the class you designed in the previous activity and turn your blueprint into working Python code. 
Your previous work contained: 
● a class name 
● at least four properties 
● their data types 
● at least three methods 
● a basic UML class diagram. 
For this activity you will upgrade and implement that same design. 
----------------------------------------------------------------------------->>>>>> Step 1 - Review Your Previous Design Open your previous: classObjectUML.md 
Review your: 
● class name 
● four or more properties 
● methods 
● UML class diagram. 
Before coding, decide whether your original properties and methods still make sense. You may improve their names or descriptions, but you must keep the same overall class/context from the previous activity. 
Write a short revision note 
## Design Revision 
Changes from my previous design: 
- ... 
- …
If you made no changes: 
No major changes were needed from my original design. 
------------------------------------------------------------------------>>>>>> Step 2 - Decide what is Public and Private In UML: 
+ Public 
- Private 
A public member can be accessed normally outside the class, while a private attribute is intended to protect internal data.]Review your existing attributes. 
You must have: 
at least 2 public attributes 
at least 1 private attribute 
Choose a private attribute that makes sense to protect. 
Example only. Suppose a student previously designed: 
GameCharacter 
name 
level 
health 
experience 
A reasonable revision might be: 
+ name : string 
+ level : int 
- health : int 
- experience : int 
Do not copy this example. 
Complete this table:
Attribute 
Data Type 
Visibility 
Why Public/Private?




Public / Private






Public / Private






Public / Private






Public / Private





------------------------------------------------------------------------->>>>>> Step 3 - Update your UML Class Diagram Modify your previous UML diagram to include: 
● class name 
● attributes 
● data types 
● visibility symbols 
● methods 
● parameters where applicable. 
Use: 
+ = public 
- = private 
Your updated UML should follow this general form. 
+--------------------------------------------+ 
| ClassName | 
+--------------------------------------------+ 
| + publicAttribute : datatype | 
| + publicAttribute : datatype | 
| - privateAttribute : datatype | 
| - privateAttribute : datatype | 
+--------------------------------------------+ 
| + method() | 
| + method(parameter : datatype)| 
| + getSomething() | 
+--------------------------------------------+ 
------------------------------------------------------------------------------------>>>>>> Step 4 - Create the Python CLass Create a Python file: classImplementation.py 
Use your own class from the previous activity 
Your class must contain an __init__() method that initializes the attributes of every new object. 
General pattern: 
class YourClass: 
def __init__(self, value1, value2, value3): 
self.attribute1 = value1 
self.attribute2 = value2 
self.__private_attribute = value3 
Remember: 
self 
refers to the particular object currently being created or used.
For a private attribute, use two leading underscores: 
self.__attribute 
---------------------------------------------------------------------------------->>>>>> Step 5 - Implement Your Methods Implement at least three meaningful methods from your original design. 
Your methods must satisfy all of these requirements: 
At least one method receives a parameter. 
At least one method changes an attribute. 
At least one method reads or returns information about the object. 
At least one method must safely interact with a private attribute. 
For example, if you have: 
self.__status 
you might provide: 
def get_status(self): 
return self.__status 
or a method that changes it according to valid rules. 
Important 
Do not simply create methods such as: 
def method1(): 
pass 
Each method should perform a meaningful action related to your class. 
SG5 specifically demonstrates methods for changing object state, for example, take_damage(amount) changing one Hero object's HP and use() changing an equipment's private status. 
------------------------------------------------------------------------------------>>>>>>Step 6 - Instantiate Two Objects Now prove that your class is really a blueprint. 
Create at least two different objects from your class. 
General pattern: 
object1 = YourClass(...) 
object2 = YourClass(...) 
Use different values where appropriate. 
For example: 
Object 1 
name = ...
value = ... 
Object 2 
name = ... 
value = … 
Do not use the same values for everything. 
----------------------------------------------------------------------------------->>>>>> Step 7 - Change Only One Object Call one of your methods on Object 1 only. 
For example: 
object1.some_method(...) 
Then display the relevant values of: 
object1 
and: 
object2 
Your output should demonstrate that changing Object 1 does not automatically change Object 2. 
SG5 uses Arthur and Morgana to establish this idea: both come from the same Hero class, but damaging Arthur changes Arthur's HP while Morgana retains her own state. 
------------------------------------------------------------------------------------------->>>>>> Step 8 - Produce a Test Run Your program should clearly demonstrate: 
1. Object 1 initial state 
2. Object 2 initial state 
3. Method executed on Object 1 
4. Object 1 updated state 
5. Object 2 unchanged state 
You may format your output however you want,provided it is readable. 
Example structure only: 
--- BEFORE --- 
Object 1: ... 
Object 2: ... 
Performing action on Object 1... 
--- AFTER --- 
Object 1: ... 
Object 2: …
Take a screenshot showing the successful execution. 
Save it as: images/classTestRun.png 
--------------------------------------------------------------------------------->>>>>> Step 9 - Create an Object Diagram Create a simple object diagram showing the state of your two objects after Step 7. 
Example structure: 
YourClass 
+--------------------+ 
| class blueprint | 
+--------------------+ 
| 
------------------- 
| | 
v v 
object1 : YourClass object2 : YourClass 
+-------------------+ +-------------------+ 
| attr = value | | attr = value | 
| attr = value | | attr = value | 
| attr = value | | attr = value | 
+-------------------+ +--------------------+ 
The two object boxes should show their actual final values, not merely the data types. 
Save this as: images/objectDiagram.png 
------------------------------------------------------------------------------------------------>>>>>> Step 10 - Short Analysis Answer each question in 3 - 4 sentences in your OWN words. 
1. Why did you make your chosen attribute private? Explain what could go wrong if other parts of the program changed it directly. 
2. Which method changes the state of your object? Identify the attribute affected and describe what happens. 
3. How did your two objects demonstrate that instances are independent? Refer to your actual test output. 
4. What is the difference between your class diagram and your object diagram? Explain this using your own class. 
----------------------------------------------------------------------------------------------------->>>>>> GitHub Submission
Continue using the same CS3 Portfolio repository from the previous activity. Keeping the continuation beside the SG4 work rather than replacing it. 
Your folder could look like: 
q1/ 
├── classObjectUML.md 
├── classImplementation.py 
├── classAttributesMethods.md 
└── images/ 
├── classDiagram.png 
├── classDiagramSG5.png 
├── classTestRun.png 
└── objectDiagram.png 
Create: 
classAttributesMethods.md 
with the following structure: 
# Class Attributes and Methods 
## Previous Design 
Link to my previous activity: 
[classObjectUML.md](classObjectUML.md) 
## Design Revision 
Describe any changes made to your original class. 
## Visibility Decisions 
| Attribute | Data Type | Visibility | Reason | 
|---|---|---|---| 
| | | | | 
| | | | | 
| | | | | 
| | | | | 
## Updated UML Class Diagram 
![Class Diagram](images/classDiagramSG5.png) 
## Python Implementation
[View Python Source](classImplementation.py) 
## Test Run 
![Test Run](images/classTestRun.png) 
## Object Diagram 
![Object Diagram](images/objectDiagram.png) 
## Analysis 
### Why did you make your chosen attribute private? 
### Which method changes the state of your object? 
### How did your two objects demonstrate that instances are independent? ### What is the difference between your class diagram and your object diagram? 
Then update the main README.md so that it links to your new activity. 
----------------------------------------------------------------------------------------------------->>>>>> Scoring Rubrics
Criterion 
Points
Correct continuation of the original SG4 class
1
Appropriate public/private attribute decisions
2
Correct updated UML visibility notation 
2
Correct __init__() and initialization of attributes
2
Correct implementation of private attribute(s) using __ 
At least three meaningful working methods
2 
3



Method with parameter and 
state-changing behavior
2
Two correctly instantiated independent objects
2
Successful test demonstrating 
independent object states
1
Correct class diagram and object diagram 
2
Complete GitHub documentation and README update
1
Total 
20

