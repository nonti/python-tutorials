a = {
    "name": "John Doe",
    "age": 30,
    "city": "New York"
}

for k in a:
    print("Prints only keys \n ",k)
    
for k,v in a.items():
    print(k + " ", v)
    
for key, value in a.items():
    print(f"This prints key and value: \n{key}: {value}")