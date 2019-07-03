n=input()
t=list(n)
per=[]
l=[]
c=1
for i in range(0,len(n)-3):
    per.append(n[i:i+4])
for i in range(1,len(n)):
    l.append(n[i-1:i+1])
for i in range(len(l)):
    for j in range(i+1,len(l)):
        x=l[i]+l[j]
        if int(l[i])>=10 and int(l[i])<=26 and int(l[j])>=10 and int(l[j])<=26:
            if x in per:
                c+=1
for i in l:
    if int(i)>=10 and int(i)<=26:
        c+=1
print(c)
