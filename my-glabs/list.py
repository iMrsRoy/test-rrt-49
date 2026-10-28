students = ['Roy', 'Reem', 'Renida', 'Ruth']
print(students)

# # Solution Template (For Learners)**
print(students)
# # 1. Add Frank to the end

print(students.append("Frank"))

# # 2. Add Grace to the front
print(students.insert(0,"Grace"))

# # 3. Replace Charlie with Chuck

students.append("Charlie")
print(students)
students[-1]="Chuck"

print(students)

# # 4. Remove the person at index 3 (Check the list after previous steps!)
removed = students.remove("Ruth")
print(removed)

# # 5. Print final results
print(students)


