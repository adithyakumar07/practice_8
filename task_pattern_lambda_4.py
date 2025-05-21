x=64
m=lambda y:[" ".join([chr(x+i)+" " for j in range (i)]) 
	for i in range(1,5)]
for k in m(x):
	print(k)