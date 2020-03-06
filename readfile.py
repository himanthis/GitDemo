file = open("test.txt")  # file path
# read all the content of file
#print(file.read(2))  # read n number of  characters

#print(file.readline())
#print(file.readline())

# print line by line using readline method

# line = file.readline()
# while line!="":
#     print(line)
#     line=file.readline()

# values=[abc,bvsdf,cat, dog,elephant]
for line in file.readlines():
    print(line)
file.close()
