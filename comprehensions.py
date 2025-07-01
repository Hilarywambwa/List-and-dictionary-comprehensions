#List comprehension
scores = [45, 78, 88, 56, 90, 62, 33, 99, 70, 50]
# Creates a list of scores above 60
Above_60 = [score for score in scores if score>60]
print(Above_60)

# Creates a list of 'Pass' and fail based on a score threshold of 50. The condition comes before the for loop.
passed = ['Pass' if score >= 50 else 'Fail' for score in scores]
print(passed)



#Dictionary comprehension
students = ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve']
marks = [82, 48, 79, 65, 91]
# Creates a dictionary to assign each key(students) to a value(marks). We use zip function since we have two inputs
pair = {k:v for (k,v) in zip(students,marks)}
print(pair)

#Create list to store students who scored above 70. We use a condition.
Above_70 = {k:v for (k,v) in zip(students,marks) if v>70}
print(Above_70)

#A dictionary that maps students to pass/fail based on a threshold. Condition comes before for loop
passed1 = {k:'Pass' if v >= 50 else 'Fail' for (k,v) in zip(students,marks)}
print(passed1)

#A dictionary comprehension that maps each word to its length
#The split() function is used to split sentence to words
sentence = "Data science is fun and insightful"
word_lengths = {word: len(word) for word in sentence.split()}
print(word_lengths)
