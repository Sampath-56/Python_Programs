# Python program to show to randomise elements of a list  
  
# Importing the random module  
import random  
list = ["Python", "Interview", "Questions", "Randomise", "List"]  
print("Original list: ", list)  
random.shuffle(list)  
print("After randomising the list: ", list)  

#Output: Original list:  ['Python', 'Interview', 'Questions', 'Randomise', 'List']
#After randomising the list:  ['Interview', 'Questions', 'Python', 'Randomise', 'List']