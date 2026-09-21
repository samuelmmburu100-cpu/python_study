fruits={'mang','oranges','apple','lemon','grapes'}

print(fruits)
print(type(fruits))

print(fruits[2])
print (fruits[-2])

print(fruits[1:2])
print(fruits[2:5])

fruits[2]='banana'
print(fruits)

fruits.append('straberries')
fruits.append('watermelon')
print(fruits)

fruits.insert(1,"Tomatoes")
print(fruits)

fruits.remove("oranges")
fruits.pop(0)
fruits.clear()


days={'monday','tuesday','wensday','thursday','friday','saturday','sunday'}
print(days[0])
print(days[-2])

print(days[1:5])

print(days[1:5])

days[3]

days.append("january")

days.insert(2,"december")

print(days)

days.remove("friday")

removed_day=days.pop()

del days[1]

days.clear()

print(days)