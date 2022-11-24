all=[]
for i in range(4):
    name,age,score = input().split(",")
    all.append([name,age,score])
    if(name>all[i][0]):
        all.insert(i)
        all[i]=[name,age,score]
# print(all)
# print("Tom">all[0][0])
for i in range(len(all)):   # 0-3
    if(all[i][0]<all[i+1][0]):
        all[i+1]=all[i]