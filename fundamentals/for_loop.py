A = [0,1,2,3,4,5] # List
B = (0,1,2,3,4,5) # Tuple
C = {0,1,2,3,4,5} # Set
D = 'Kim' # String
E = {
    'name': 'Kim', 
    'age': 22
    } # Dictionary only iterate keys

for x,y in E.items():
    print(x + ' ' , y)