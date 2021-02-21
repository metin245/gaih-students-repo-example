
Student_Grade=[]
Student_Name=[]
Info={}
Midterm_All=[]
Final_All=[]
Homework_All=[]
ort=[]
ort_2=[]
ort_3=[]
info={}
sorted_avgDict={}
import math
for i in range(2):
    student = input("Öğrencinin Adını ve Soyadını Aralarında Boşluk Olacak Şekilde Giriniz")
    Student_Name.append(student)
    Final=list(map(float, input("Öğrencinin Midterm notunu,Final Notunu ve Homework Notunu aralarında"
                                " virgül olacak şekide giriniz Giriniz").split(',')))
    Final_All.append(Final)
info=dict(zip(Student_Name,Final_All))
print(info)
avgDict = {}
for k,v in info.items():
    # v is the list of grades for student k
    avgDict[k] = sum(v)/ float(len(v))

sorted_avgDict=dict(sorted(avgDict.items(),key=lambda item: item[1],reverse=True))
print(sorted_avgDict)
max_key = max(sorted_avgDict, key=sorted_avgDict.get)
print("congrulation",max_key,"you are the best grade")
