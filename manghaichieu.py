a = [[1,2,3],[4,5]]
row = len(a)
for i in range (0, row):
    col = len(a[i])
    for j in range(0,col):
        print("Hang",i+1,"Cot",j+1,":",a[i][j])