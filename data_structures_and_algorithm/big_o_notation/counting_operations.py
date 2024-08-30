# big o(1)
student_list = ['khenso','lungi','vukosi','kim', 'zoe','tim', 'tom','ntsako','amu','karabo','teboho','tumi'] # O(1)

def randomFunction(students):
    first = students[0] #  O(1)
    total = 0 #O(1)
    new_list = [] # O(1)
    
    for student in students: 
        total += 1 # O(n)
        new_list.append(student) #O(n)
    
    print(new_list) #O(1)
    return total #O(1)

print(randomFunction(student_list))#O(n) => O(n)