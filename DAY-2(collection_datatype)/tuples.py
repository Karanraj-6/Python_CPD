#tuples =collection which is ordered,allows duplicates and unchangeble used to group together related data


student= ("A",1,"B")

print(student.count("A"))
print(student.index("B"))


# *immutable so we need to convert into list first to chage that values
student = list(student)
student.append("C")
student = tuple(student)
print(student)
