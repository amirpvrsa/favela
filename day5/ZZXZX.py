student_heiights = input().split()
for n in range(0,len(student_heiights)):
    student_heiights[n]=int(student_heiights[n])
    total_height += student_heiights[n]
    
print(f"tota heigh = {total_height}")