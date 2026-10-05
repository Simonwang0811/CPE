try:
	data ={'A':'A','B':'','C':'','D':'', 'E':'3', 'F':'', 'G':'' ,'H':'H', 'I':'I', 'J':'L', 'K':'', 'L':'J', 'M':'M', 'N':'', 'O':'O', 'P':'', 'Q':'', 'R':'', 'S':'2', 'T':'T', 'U':'U', 'V':'V', 'W':'W', 'X':'X', 'Y':'Y', 'Z':'5','1':'1','2':'S','3':'E','4':'','5':'Z','6':'','7':'','8':'8' ,'9':'' }
	out_sw = 0
	while True:
		if out_sw == 0:
			out_sw = 1
		else:
			print()
		N = list(input())
		s_sw=0
		for i in range(len(N)):
			temp=len(N)-i-1
			
			g=data.get(N[i],-1)
			if g==-1 or data[N[i]]=='' or data[N[i]] != N[temp]:
				s_sw = 1
				break
					
		#print(s_sw)
		
		
		p_sw=0
		
		for i in range(0,int(len(N)/2),1):
			temp = len(N)-1-i
			if N[i] != N[temp]:
				p_sw = 1
				break
		
		#print(p_sw)
		
		
		if p_sw==1 and s_sw==1:
			print(''.join(N),' -- ','is not a palindrome.',sep='')
			
		elif p_sw==0 and s_sw==1:
			print(''.join(N),' -- ','is a regular palindrome.',sep='')
		elif p_sw==1 and s_sw==0:
			print(''.join(N),' -- ','is a mirrored string.',sep='')
		else:
			print(''.join(N),' -- ','is a mirrored palindrome.',sep='')
		
	
except Exception :
	pass


