student = {"Alex": 91, "Bob": 86, "Nathan": 45, "John": 92, "Joshua": 79}
print(student)

sum = 0

for i in student:
    sum += student[i]
print(sum)
average  = sum / len(student)
print (f"The average mark is {average}")

maximum = max(student.values())
print ("The maximum score is",maximum)
minimum = min(student.values())
print("The minimum score is",minimum)

max_key = max(student,key = student.get)
print("The person with lowest marks is",max_key)
min_key = min(student,key = student.get)
print("The person with lowest marks is",min_key)




