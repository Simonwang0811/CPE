N = int(input())
sw = 0
for i in range(N):
	if sw==0:
		sw=1
	else:
		print()
	blank=input()
	M=int(input())
	
	data=[]
	for i in range(M):
		temp=list(map(int,input().split()))
		data.append(temp)
	total=[]
	carry=0
	for i in range(M-1,-1,-1):
		count=data[i][0]+data[i][1]+carry
		
		carry=int(count/10)
		count=count%10
		
		total.append(count)
		
		if i==0 and carry!=0:
			total.append(carry)
	total.reverse()
	total = list(map(str,total))
	print(''.join(total))
		
	



