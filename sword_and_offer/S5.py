S="We Are Happy"
i=0
count=0
while i<len(S):
    if S[i]==" ":
        count+=1
    i+=1
result=[]
for i in range(0,len(S)+2*count):
    result.append(" ")
p1=len(S)-1
p2=len(result)-1
while p1>=0:
    if S[p1]==" ":
        result[p2]="0"
        result[p2-1]="2"
        result[p2-2]="%"
        p2=p2-3
    else:
        result[p2]=S[p1]
        p2-=1
    p1-=1
print(result)