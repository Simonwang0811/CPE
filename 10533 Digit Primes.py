import sys
input = sys.stdin.readline
try:
    data = []
    m = []
    data.append(0)
    m.append(0)
    '''def Prime_number(num):
        if num == 2 or num == 3 :
            return True
        if num % 2 == 0 or num % 3 == 0:
            return False
        
        i = 5
        while i * i <= num:
            if num % i == 0 or num % (i + 2) == 0:
                return False
            i += 6  # 下一組
            
        return True'''


    '''def Prime_number(num):
        if num %2 == 0 or num %3 == 0:
            return 0
        6n (6n+1) 6n+2 6n+3 6n+4 (6n+5)
        n=0 1,5 
        n=1   7,11
        n=2     13,17
        n=3        19,23
        
        for i in range(5,int(num**0.5)+1):
            if num%i == 0:
                #print(num,0)
                return 0
        #print(num,1)
                
        return 1'''

    def digit_prime():
        global data,m
        for i in range(1,len(data)):
            #print(i,end = ' ')
            if data[i] == 1:   #prime number
                Sum = 0
                copy_i = i
                while copy_i > 0:
                    S = copy_i%10
                    Sum += S  #Sum i
                    copy_i = copy_i//10
                
                if data[Sum] == True:
                    m.append(m[-1]+1)
                else:
                    m.append(m[-1])
                '''num = str(i)
                if len(num) != 1:
                    Sum = 0
                    for j in range(len(num)):
                        Sum += int(num[j])
                    
                    if Sum <= len(data):
                        if data[Sum] == 1:
                            
                            m.append(m[-1]+1)
                            #print('test',i)
                        else:
                            m.append(m[-1])
                    else:
                        print('check01')
                else:
                    if data[i] == 1:
                        m.append(m[-1]+1)
                        #print(i)
                    else:
                        m.append(m[-1])'''
            else:
                m.append(m[-1])
            
        
    for i in range(1, 1000001):
        
        data.append(True)
    
        #data.append(Prime_number(i))
        #print(i,data[i])
    data[0] = False
    data[1] = False
    for i in range(2,int(1000000**0.5),1):
        if data[i] == True:
            j = 2
            while i*j < len(data):
                data[i*j] = False
                j += 1
    
    #print(data)
    #print('done')
    digit_prime()
    #print(m,len(m))
    
    while True:
        N = int(input())
        for case in range(N):
            s = list(map(int,input().split()))

            #print(len(data))
            '''c1 = 0
            c2 = 0

            count = 0
            sw = 0
            i=0
                
                
            while True:
                if m[i] <= s[1]:
                    if m[i] > s[0] and sw == 0:
                        sw = 1
                        c1 = count
                        count += 1
                    else:
                        count += 1
                else:
                    c2 = count
                    break
                i += 1'''

            print(m[s[1]]-m[s[0]-1])
except Exception :
    pass
