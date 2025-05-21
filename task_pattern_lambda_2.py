x=lambda a: "A " if a==1 else "A "*a+"\n"+x(a-1)
print(x(5))