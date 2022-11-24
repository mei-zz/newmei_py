a = input()
up_count, low_count = 0, 0
for i in a:
    if i.islower():
        low_count += 1
    elif i.isupper():
        up_count += 1
print("UPPER CASE:"+str(up_count))
print("LOWER CASE："+str(low_count))