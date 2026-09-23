# =>stores multiple properties in kye-value pairs key:(value)
# enclosed with {curly braces}
# keys are always strings but values can be of any type
# keys are unique
# class 'dict'

"students1"={
    "name:" "alex",
    "age:" "20",
    "admn:" "tech2323",
    "city:" "Nairobi",
}

print("student1")
print(type("student1"))

# display values
print("student1"['name'])
print("student1"['city'])

# display adm
print("student1"['tech2323'])

# adding and updating

# adding
"student1"['Gender']='Male'
print("student1")

# add a new key email with a value
print("student1"['email'])='value'

# updating
"student1"['age']=30
print("student1")

# update name with a diff name
print(type('student1'))gg