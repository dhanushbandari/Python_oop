def check_key(my_dict,key):
    if key in my_dict:
        return "Key is present in the dictionary"
    else:
        return "Key is not present in the dictionary"
    
my_dict={"name":"Alice","age":30,"city":"New York"}
print(check_key(my_dict,"name"))            
print(check_key(my_dict,"country"))


dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

dict1.update(dict2)
print(dict1)

dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

merged = {**dict1, **dict2}
print(merged)

student = {"name": "John", "age": 20, "grade": "A"}

for key, value in student.items():
    print(key, ":", value)