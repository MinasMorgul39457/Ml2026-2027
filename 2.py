from math import dist as r
f=open("задание 2.txt")
q=[]
for s in f:
    s=s.replace(",",".")
    a,b=[float(i) for i in s.split()]
    q+=[[a,b]]
k1,k2=[],[]
for t in q:
    x,y=t
    if x<22.5:
        k1+=[t]
    else:
        k2+=[t]
def c(k):
    rt=[]
    for t in k:
        s=sum([r(t,i) for i in k])
        rt+=[[s,t]]
    return min(rt)[1]
w1=c(k1)
w2=c(k2)
print(w1,w2)
print((w1[0]+w2[0])/2*1000,(w1[1]+w2[1])/2*1000)
