x=4
m=lambda a:[" ".join([chr(65+j)+" " for j in range (i+1)]) 
	for i in range(x)]
for k in m(x):
	print(k)