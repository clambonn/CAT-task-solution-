#1 
# True , false 
#2
#a compiler translates the entire code and stores the compiled version for faster later execution, while an interpreter translates the code line by line and does not keep the translation, requiring it to run every time the program is executed.
#3
#it is a way to extract a part of a list, string, or any iterable, for example:
s = "Hello World"

print(s[0:5])   
print(s[6:])    
print(s[:5])    
#4
#shallow copy Copies object but not nested objects and Deep copy Copies everything including nested objects 
#it breaks code when modifying nested structures affects the original
#5
#map Applies function to all items
#filter Filters items based on condition
#List comprehensions More readable, Pythonic syntax 
#Preferable: List comprehensions for readability; map/filter for functional programming style 
#6
# B
#7 
#raise Throws an exception to stop program execution,Used when an error occurs
#assert Tests if a condition is True, raises "AssertionError" if False and Used for debugging and testing assumptions
#Can be disabled with -O flag in production
#Returns special values (like -1, None, False) to indicate errors, doesn't stop execution
#it shouldn't be used for Input validation from users,Handling expected errors, Production error handling
#8 
# Core Principles
#Encapsulation: Bundle data and methods; control access 
#Inheritance: Child classes inherit from parent
#Polymorphism: Same interface, different implementations
#Abstraction: Hide complexity, show only essentials
#sort Modifies original list
#sorted makes New sorted list