marks = []
average= 0
for i in range(6):
    sub_mark=int (input (f"{i+1} Enter  marks :"))
    marks.append(sub_mark)
for i in range (6):
    average+=marks[i]
    
average = average/6

if ( average >= 90):
    print("O")
elif ( average < 90 and  average >80):
    print("A+")
elif ( average < 80 and average >70):
    print("B+")
elif ( average < 70 and average > 60):
    print("B-")
elif ( average < 60 and average > 50):
    print("c")
else:
    print("Fail")