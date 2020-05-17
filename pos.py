    print("POS CONVERSION")
    print("Enter variables:")
    v=list(input().split())
    n=len(v)
    print("Enter expression:")
    ne=list(input().split(")("))
    f=ne.pop(0)
    f=f[1:]
    ne.insert(0,f)
    f=ne.pop(len(ne)-1)
    f=f[:len(f)-1]
    ne.append(f)
    e=[]
    def pos(t,a):
        e.remove(t)
        nt=t+"+"+a
        e.append(nt)
        e.append(nt+"'")
        for j in v:
            if nt.find(j)==-1:
                pos(nt,j)
                pos(nt+"'",j)
                break
    for i in ne:
        s=i
        f=0
        e.append(i)
        for j in v:
            if s.find(j)==-1:
                pos(s,j)
                break
    ne=[]
    for i in e:
        if i not in ne:
            ne.append(i)
    f=ne.pop(0)
    f="("+f
    ne.insert(0,f)
    f=ne.pop(len(ne)-1)
    f=f+")"
    ne.append(f)
    print("Standard POS form:")
    print(*ne,sep=")(")
