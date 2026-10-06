case = int(input())

for t in range(case):
    blank = input()
        
    m, n = list(map(int, input().split()))
    
    data = []
    for i in range(m):
        c = list(input())
        for j in range(len(c)):
            c[j] = c[j].lower()
        data.append(c)

    k = int(input())

    #方向
    move_r = [-1, -1, -1, 0, 0, 1, 1, 1] 
    move_c = [-1, 0, 1, -1, 1, -1, 0, 1]
    
    for w in range(k):
        word = list(input().lower())  # 單字轉小寫

        found = False
        for i in range(m):
            if found == True:
                break
            for j in range(n):
                if found == True:
                    break
                if data[i][j] == word[0]:
                    for d in range(8):
                        match = True  
                    
                        for step in range(len(word)):
                            r = i + move_r[d] * step
                            c = j + move_c[d] * step
                        
                            if r < 0 or r >= m or c < 0 or c >= n or data[r][c] != word[step]:
                                match = False
                                break
                        
                       
                        if match == True:
                            print(f"{i + 1} {j + 1}")
                            found = True
                            break 
                            
    if t < case - 1:
        print()
'''for i in range(m):
    o = ''.join(data[i])
    print(o)'''
