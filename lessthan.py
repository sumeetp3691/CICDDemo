a=[1,2,3,4,5,6,7,8,9,0]
x=[]
y=[]
for l in a :
    if l < 5:
        x.append(l)
        x.sort()
print(x)

m=eval(input("Enter a number between 0 to 9: "))
for n in a :
    if n < m :
        y.append(n)
        y.sort()
print(y)