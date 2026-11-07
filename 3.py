f=open("задание 3.txt")
q=[]
for s in f:
    s=s.replace(",",".")
    a,b=[float(i) for i in s.split()]
    q+=[[a,b]]
k1,k2,k3=[],[],[]
for t in q:
    x,y=t
    if x<-10:
        k1+=[t]
    if -10<=x<=15:
        k2+=[t]
    if x>15:
        k3+=[t]
def r(a,b):
    x1,y1=a
    x2,y2=b
    return abs(x1-x2)+abs(y1-y2)
def c(k):
    rt=[]
    for t in k:
        s=sum([r(t,i) for i in k])
        rt+=[[s,t]]
    return min(rt)[1]
w1=c(k1)
w2=c(k2)
w3=c(k3)
print(w1,w2,w3)
print((w1[0]+w2[0]+w3[0])/3*1000,(w1[1]+w2[1]+w2[1])/3*1000)
