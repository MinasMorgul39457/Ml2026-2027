f=open("задание 4.txt")
q=[]
for s in f:
    s=s.replace(",",".")
    a,b=[float(i) for i in s.split()]
    q+=[[a,b]]
k1,k2=[],[]
for t in q:
    x,y=t
    if y>=6 or (-2<=x<=2 and y>=4):
        k1+=[t]
    else:
        k2+=[t]
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
print(w1,w2)
print((w1[0]+w2[0])/2*1000,(w1[1]+w2[1])/2*1000)
