# Create file 
# file = open("students.txt", "x")
# file.close()
# print("Students file created..")

# Open File 
# file = open("students.txt","r")
# print("File opened")
# file.close()

# Read file 
# file = open("students.txt","r")
# info = file.read()
# print(info)
# file.close()

# Read first line 
# file = open("students.txt","r")
# info = file.readline()
# print(info)
# file.close()

# Read each line 
# file = open("students.txt","r")
# info = file.readlines()
# print(info)
# file.close()

# Add text in same line
# file = open("students.txt","w")
# file.write("This is new line for Student 4")
# file.write("This is new line for Student 5")
# file.write("This is new line for Student 6")
# file.write("This is new line for Student 7")
# file.close()
# print("New text added in student file")

# Add test in multiple lines 
# file = open("students.txt","w")
# file.write("This is new line for Student 4 \n")
# file.write("This is new line for Student 5 \n")
# file.write("This is new line for Student 6 \n")
# file.write("This is new line for Student 7 \n")
# file.write("This is new line for Student 7 \n")
# file.close()
# print("New text added in student file")

# List add in file 
# students = ["Student 1 \n","Student 2 \n", "Student 3 \n", "Student 4 \n"]
# file = open("students.txt","w")
# file.writelines(students)
# file.close()
# print("New text added in student file")

# List add in file  with new line 
# students = ["Student 1 \n","Student 2 \n", "Student 3 \n", "Student 4 \n"]
# file = open("students.txt","a")
# file.writelines(students)
# file.close()
# print("New text added in student file")

# import os
# os.rename("students.txt", "students-renamed.txt")
# print("Renamed success")

# import os 
# os.remove("students-renamed.txt")
# print("Deleted successfully")

# import os
# file = os.path.exists("students.txt")
# if file:
#     print("File exisist")
# else:
#     print("No exist")    

# import os
# size = os.path.getsize("students.txt")
# print(size)

# import os
# os.makedirs("student")
# print("Directory created")

# import csv
# with open("students.csv","w", newline="") as file:
#     wr = csv.writer(file)
    
#     wr.writerow(["Name", "Age", "Address"])
#     wr.writerow(["St1", 11, "bbsr"])
#     wr.writerow(["St2", 22, "bbsr1"])
#     wr.writerow(["St3", 55, "ctc"])
    
# print("CSV file created")    

# import csv
# with open("students.csv","r") as file:
#         rd = csv.reader(file)
        
#         for i in rd:
#             print(i)
        

import json

student = {
    "name":"Student 1",
    "age":22,
    "address":"BBSR"
}

with open("students.json","w") as file:
    json.dump(student,file,indent=4)


import json
with open("students.json","r") as file:
    data = json.load(file)

print(data['name'])
    