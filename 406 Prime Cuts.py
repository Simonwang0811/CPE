try:
    
    data = []
    for i in range(1001):
        data.append(True)

    data[0] = False
    def prime_number():
        for i in range(2,int(1000**0.5),1):
            if data[i] == True:
                j=2
                while i*j < len(data):
                    
                    data[i*j] = False
                    j += 1
    prime_number()
    while True:
                
        N,C = list(map(int,input().split()))
        print(f'{N} {C}: ',end = '')
        prime = []
        for i in range(1,N+1):
            if data[i] == True:
                prime.append(i)

        #print(prime)


        ans = []
        if len(prime)%2 == 0: #even number
            C = 2*C
            left = (len(prime)-1)//2
            right = left+ 1
            ans.append(prime[left])
            ans.append(prime[right])
            C -= 2
            d = 0
            while C > 0 and len(ans) < len(prime):
                d += 1
                #print(left-d,right+d)
                ans.append(prime[left-d])
                ans.append(prime[right+d])
                C -= 2
        else: #odd number
            C = 2*C-1
            mid = int((len(prime)-1)/2)
            ans.append(prime[mid])
            C -= 1
            d = 0
            while C > 0 and len(ans) < len(prime):
                d += 1
                ans.append(prime[mid+d])
                ans.append(prime[mid-d])
                C -= 2
        ans.sort()

        ans = list(map(str,ans))
        print(' '.join(ans))
        print()
except Exception:
    pass







