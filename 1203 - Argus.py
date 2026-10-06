data_keys = []
data_values = []
data_add = []
data = []
n = input().split()
n.pop(0)

while True:
    n[0] = int(n[0])
    n[1] = int(n[1])
    data.append(n)
    n = input().split()
    if n[0] == '#':
        break
    else:
        n.pop(0)
    

data.sort()

for i in range(len(data)):
    m = data[i]
    data_keys.append(m[0])
    data_values.append(int(m[1]))
    
    
data_add = list(data_values)
#print(data_keys,data_values)
#print(min(data_values))
num = int(input())
while num != 0:
    num -= 1
    minium = min(data_values)
    p = data_values.index(minium)
    print(data_keys[p])
    data_values[p] += data_add[p]
    #print(data_keys,data_values)
    

