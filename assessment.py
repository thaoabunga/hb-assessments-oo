"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.

   1. Abstraction - Creates efficiencies by hiding details that are not required.
   2. Encapsulation - Allows for modularity, keeps everything in one place.
   3. Polymorphism - Enhances interchangeability of components, different things can be done within one interface.

2. What is a class? A class can be thought of as guidelines for creating objects. They are often referred to as a type of thing
like a string or file and are written in UpperCamelCase.  
They cannot have empty bodies, a pass statement or doc strings are used so that the bodies aren't empty. Classes are also an attribute of that class.


3. What is an instance attribute? An instance attribute is an instance on the object. They occur within specific instances of a class.

4. What is a method? A method is like a function defined on a class. They must always have at least one parameter, self.
They can also refer to attirbutes and can call other methods which is polymorhpic in nature.

5. What is an instance in object orientation? An instance is a memory reference, it only has a memory address of an object in it.

6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.

   The class attribute is shared by all instances, whereas, the instance attribute is specific to that instance. 
   Class attributes are handy when storing constants, defining default values, and tracking data across all instances of a given class.
   An instance attribute would be useful when using data attributes and methods.
"""


# Parts 2 through 5:
# Create your classes and class methods

class Student(object):
	"""Student contact information"""

	student_info = {}
	student_info['first_name'] = first_name
	student_info['last_name'] = last_name
	student_info['address'] = address

	def ___init__(self, first_name, last_name, address):
		self.first_name = first_name
		self.last_name = last_name
		self.address = address

class Question(object):
	"""Prep questions"""
	def ___init___(self, question, correct_answer):
		self.question = question
		self.correct_answer = correct_answer

class Exam(Question):
	"""Exam questions"""
	def ___init___(self, name)
		self.name = name
		

	def add_question(self, question, correct_answer):

