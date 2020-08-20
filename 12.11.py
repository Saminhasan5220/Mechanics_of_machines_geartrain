P=[1, 1.25, 1.5, 1.75,2,2.5,3,3.5,4,6,8,10,12,14,16,18,20,24,28,32,36,40,44,48,52,56]
N2=20
N3=30
rat=1/8
fact=rat*N3/N2
for i in range(len(P)):
    Pd2=P[i];
    for j in range(len(P)):
        Pd4=P[j]
        for k in range(15, 201):
            N4=k
            N5=N4/fact
            N4T=(N2+N3)/(1+1/fact)*(Pd4/Pd2)
            if abs(N4T-N4)<0.1 and N5.is_integer():#fix(N5)==N5:
                #print("N4=", N4,",","N5=",N5,",","Pd2=",Pd2,",","Pd4=",Pd4)
                print( N4,N5,Pd2,Pd4)