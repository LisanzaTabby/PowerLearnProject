import pandas as pd
#import matplotlib as plt
import matplotlib.pyplot as plt

# creating a dataframe= which is a whole table
# A dataframe is a 2D data structure which is like a 2D array or a table with rows and columns
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [24, 50, 22],
    'Score': [85, 90, 95]
}
df = pd.DataFrame(data)
print(df)
# Series- is like a column in a table 
a = [1,7,2]
myint= pd.Series(a)
print(myint)

# Labels = follows indexing labelling with the 1st value being index[0]
print(myint[1])
# creating customized labels
b = [2, 3, 4, 5]

my_int2 = pd.Series(b, index = ["w","x","y","z"])
print(my_int2)

# Loading file into a DataFrame
#df = pd.read_csv('synthetic_credit_consumers.csv')
#print(df.to_string()) # to prinmt the entire dataframe
#print(df. head(10))# to display the first 10 rows)
#print(df.info())

# Practice (Create a DataFrame with 3 students: name, age, and grade. Add a column called “Passed” where grade > 50 = True. 
# Filter and display only students who passed.)
student_data = {
    'Name': ['student1', 'student2', 'student3'],
    'Age': [20, 21, 22],
    'Grade': [60, 40, 75]
}
student_df = pd.DataFrame(student_data, index=[1,2,3])

# Adding the passed column
student_df['Passed'] = student_df['Grade'] > 50

# Filter and display only studentys who passed
passed_students = student_df[student_df['Passed']]

print("All Students: ")
print(student_df)
print("\nStudents who passed:")
print(passed_students)

# plot using pandas + Matplotlib
plt.plot(student_df['Name'], student_df['Grade'], marker='o')
plt.title("Students Performance")
plt.xlabel("Students")
plt.ylabel("Grade")
plt.grid(True)
plt.show()