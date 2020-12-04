
"""
This program is to display the number of grades of final exam
The program would display average grades 
Then find percentage of grades is greater than the average grades

"""

"""
   
 open text file
grades = infile input()
average = sum of grades / grades 
    if the % of grades > average
    num = 1
print number of grades to user 
print average grade 
print percentage of grades above average


"""

infile = open("final.txt", "r")
grades = [line.rstrip() for line in infile]
infile.close()
for i in range(len(grades)):
    grades[i] = int(grades[i])
average = sum(grades) / len(grades)
num = 0

for grade in grades: 
    if grade > average:
        num += 1

print("Number of grades:", len(grades))
print("Average grade:", average)
print("percentage of grades above average: {0:.2f}%" .format(100 * num / len(grades)))