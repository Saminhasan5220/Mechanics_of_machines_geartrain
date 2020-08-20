N = [20,22,25,30,32,34,35,40,50,55,60,64]

for i in range(len(N)):
	N4 = N[i]
	for	j in range(len(N)):
		N3 = N[j]
		for k in range(len(N)):
			N5 = N[k]
			if (N3 != N4) and (N4 != N5) and (N5!=N3):
				product = N4/(N3*N5)
				if product == 0.025:
					#print("N4=",N4,",","N3=",N3,"and","N5=",N5)
					print(N4,N3,N5)
		
	