try:
    while True:
        
        s1 = list(input())
        s2 = list(input())
        s1.insert(0,'0')
        s2.insert(0,'0')
        data = []
        for i in range(len(s1)):
            n = []
            for j in range(len(s2)):
                n.append(0)
            data.append(n)
        #print(data)

        for i in range(1,len(s1)):
            for j in range(1,len(s2)):
                if s1[i] == s2[j]:
                    data[i][j] = data[i-1][j-1]+1
                else:
                    data[i][j] = max(data[i-1][j],data[i][j-1])
                    
        print(max(data[-1]))
        
except Exception:
    pass
