student_list1 = ['kim', 'zoe','tim', 'tom']

student_list2 = ['khenso','lungi','vukosi','ntsako','amu','karabo','teboho','tumi']

def chcekStudent(student_lis1):
    for student in student_list1:
        if student == 'tumi': # complexity is worse case scenario because it iterate through the loop
            print('available')

chcekStudent(student_list1)