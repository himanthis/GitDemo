values = [1, 2, "rahul", 4, 5]
#list is a data types that allows multiple values and can be with different data types

print(values[0]) #1
print(values[-1]) #last index
print(values[1:3]) # 2 rahul
values.insert(3,"shetty")
print(values)
values.append("End")
print(values)
values[2] = "RAHUL"
print(values)
del values[0]
print(values)

#TUPLE- same as list data types but immutable
val = (1, 2, "rahul", 4.5)
print(val[1])
#val[2] = " RAHUL"  'tuple' object does not support item assignment
print(val)

#dictionary
dic = {"a":2, 4:"bcd", "c":"hello world"}
print(dic[4])
print(dic["c"])

# dynamic dictionary 
dict ={}
dict["firstname"]= "Himanthi"
dict["lastname"]="Siriwardane"
dict["gender"]= "Female"

print(dict)
print(dict["lastname"])







