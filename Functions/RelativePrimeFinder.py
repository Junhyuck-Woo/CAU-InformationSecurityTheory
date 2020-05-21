a = 1
b = 33
a_list = []

for a in range(b):
    count = 0
    for i in range(2, b):
        if (a%i==0) and (b%i==0):
            count = count + 1
            break
    if count==0:
        a_list.append(a)


print(a_list)
