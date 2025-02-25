# file = open("test.txt","a")
# # file.write("10")
# for i in range(1,11):
#     file.write(f"\n{i}") 
# file.close

# file = open("test.txt", "r")
# a = file.read(3)
# b = file.readline()
# print(a,b, sep="--")
# file.close

# file = open("test.txt","r")
# a=[]
# n = int(file.readline())
# for i in range(0,n):
#     tmp= int (file.readline())
#     a.append(tmp)
# print(a)
# file.close  

# file = open("test.txt","r")
# a = []
# data = str(file.readlines()).split()
# for i in data:
#     tmp= i
#     a.append(tmp)
# print(a)


file = open("test.txt", "r")
a= []

for i in file:
    data = i.split()
    temp_row = []
    for j in data:
        tmp = int(j)
        temp_row.append(tmp)
    a.append(temp_row)
print(a)
file.close()