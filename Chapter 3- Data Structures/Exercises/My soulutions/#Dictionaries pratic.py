#Dictionaries pratic
student={'name':'Joana','age': '23' , 'course' : 'Business'}
print(student['name'])
print(student['age'])
print (student ['course'])
# THERE TWO METHEDO TWO DELETE IN DICTIONARIES  pop and Del
age=student.pop('age')
print(student)
print(age)
# second method of delete

student={'name':'Joana','age': '23' , 'course' : 'Business'}
del  student['age']
print(student)
# how many key are in dictionaries we use 'Len'

student={'name':'Joana','age': '23' , 'course' : 'Business'}
print(len(student))
# if you want to see key

student={'name':'Joana','age': '23' , 'course' : 'Business'}
print(student.keys())
# if you would like to see values
print(student.values())
# if you want see both keys and 
student={'name':'Joana','age': '23' , 'course' : 'Business'}
print (student.items())
# if you want  dont want to you ANY METHOD
student={'name':'Joana','age': '23' , 'course' : 'Business'}
for key in student:
  print (key)
  #PRINT BOTH 
student={'name':'Joana','age': '23' , 'course' : 'Business'}
for key, value in student.items():
  print(key,value)


