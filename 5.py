f=open("задание 5.txt")
q=[]
for s in f:
    s=s.replace(",",".")
    a,b=[float(i) for i in s.split()]
    q+=[[a,b]]
k1,k2,k3=[],[],[]
for t in q:
    x,y=t
    if x<=0 and y<=3.5:
        k1+=[t]
    elif (y<=7.1 and x>=2) or (y<=4.3 and 0<=x<2):
        k2+=[t]
    else:
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
print((w1[0]+w2[0]+w3[0])/3*1000,(w1[1]+w2[1]+w3[1])/3*1000)
