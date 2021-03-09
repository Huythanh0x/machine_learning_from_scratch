import numpy as np
given_number = input().split()
given_number = [int(number) for number in given_number]
number_of_student = given_number[0]
number_of_exam = given_number[1]
row = given_number[2]
column = given_number[3]

def nearest_position(np_student,row,column):
    stt = np_student[row-1][column-1]
    nearest_student = np.where(np_student == stt)
    if row = nearest_student[0][0] + 1:
        print(nearest_student[0][1] + 1,nearest_student[1][1] + 1)
    else:
        print(nearest_student[0][0] + 1,nearest_student[1][0] + 1)


seq_exam = 1
list_student = []
for _ in range(number_of_student):
    if seq_exam > number_of_exam:
        seq_exam = 1
    list_student.append(seq_exam)
    seq_exam += 1
np_student = np.array(list_student)
np_student = np_student.reshape(-1,2)
print(np_student)
nearest_position(np_student,row,column)
