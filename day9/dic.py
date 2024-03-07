# programming_dictionary = {
#     "Bug": "An error in a program that prevents the program from running as expected.", 
#     "Function": "A piece of code that you can easily call over and over again."
# }

# programming_dictionary["Bug"]
# programming_dictionary["loop"]="hbkhjbkb j k o o oojjoioo i oi "
# print(programming_dictionary)

student_scores={
    "Harry" : 81,
    "Ron" : 78,
    "Hermione" : 99,
    "Draco" : 74,
    "Neville" : 62
}
for name in student_scores:
    if student_scores[name]>=91:
        student_scores[name]="Outstanding"
    elif student_scores[name]<91 and student_scores[name]>=81:
        student_scores[name]="Exceeds Expectations"
    elif student_scores[name]<81 and student_scores[name]>70:
        student_scores[name]="Acceptable"
    elif student_scores[name]<=70:
        student_scores[name]="you fail motherfucker"

print(student_scores)