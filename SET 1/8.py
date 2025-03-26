List = [[2, 8, 10], [12, 45, 2], [4, 10, 1]]  
for i in range(len(List)-1):
    if List[i][0]>List[i+1][0]:
        List[i][0],List[i+1][0]=List[i+1][0],List[i][0]
print("Ascending",List) 


List = [[2, 8, 10], [12, 45, 2], [4, 10, 1]]  
for i in range(len(List)-1):
    if List[i][0]<List[i+1][0]:
        List[i][0],List[i+1][0]=List[i+1][0],List[i][0]
print("Descending",List)
