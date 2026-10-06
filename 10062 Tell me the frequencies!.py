try:
    sw = 0
    while True:
                
        N = input()
        if sw == 0:
            sw = 1
        else:
            print()
            
        dic = {}

        for i in range(len(N)):
            count = N.count(N[i])
            if dic.get(count,-1) == -1:
                dic[count] = []
                dic[count].append(N[i])
            else:
                if dic[count].count(N[i]) == 0:
                    dic[count].append(N[i])


        #print('dic:',dic)
        key = list(dic.keys())
        key.sort()
        for i in key:
            value = dic[i]
            value.sort()
            value.reverse()
            for j in value:
                print(ord(j),i)
            

        
except Exception:
    pass
