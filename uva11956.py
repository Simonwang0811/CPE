
N = int(input())

for Case in range(N):
    m = list(input())
    point = 0
    data = []
    
    for i in range(100):
        data.append(0)
        
    for i in range(len(m)):
        if m[i] == '<':
            point -= 1
            if point == -1:
                point = 99
        elif m[i] == '>':
            point += 1
            if point == 100:
                point = 0
        elif m[i] == '+':
            data[point] += 1
            if data[point] == 256:
                data[point] = 0
        elif m[i] == '-':
            data[point] -= 1
            if data[point] == -1:
                data[point] = 255  
        else:
            pass

    hex_list = []
    for val in data:
        hex_str = "%02X" % val
        hex_list.append(hex_str)
        
    result_str = " ".join(hex_list)

    print(f"Case {Case+1}: {result_str}")