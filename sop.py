print("SOP CONVERSION")
print("Enter variables:")
v=list(input().split())
n=len(v)
print("Enter expression:")
ne=list(input().split("+"))
e=[]
def sop(t,a):
    e.remove(t)
    nt=t+a
    e.append(nt)
    e.append(nt+"'")
    for j in v:
        if nt.find(j)==-1:
            sop(nt,j)
            sop(nt+"'",j)
            break
for i in ne:
    s=i
    e.append(i)
    for j in v:
        if s.find(j)==-1:
            sop(s,j)
            break
print("Standard SOP form: ")
ne=[]
for i in e:
    if i not in ne:
        ne.append(i)
print(*ne,sep=" + ")
