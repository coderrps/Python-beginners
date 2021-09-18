#reading files
'''employee_file = open("employees.txt", "r")

print(employee_file.readable())
print(employee_file.readlines())
print(employee_file.read()) #to read the elements of the file
for employee in employee_file.readlines():
    print(employee)


employee_file.close() # closing the file'''

'''employee_file = open("employees.txt", "a")
employee_file.write("\nToby - Salesman") #add new line in the file
employee_file.close()'''

employee_file = open("index.html", "w") #creating a new file
employee_file.write("<p> This is my HTML file </p>") 
employee_file.close()