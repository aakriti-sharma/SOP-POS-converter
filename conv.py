
def sop(t,a,v,e):
        e.remove(t)
        nt=t+a
        e.append(nt)
        e.append(nt+"'")
        for j in v:
            if nt.find(j)==-1:
                sop(nt,j,v,e)
                sop(nt+"'",j,v,e)
                break

def sopcon(ne,v):
    n=len(ne)
    e=[]
    for i in ne:
        s=i
        e.append(i)
        for j in v:
            if s.find(j)==-1:
                sop(s,j,v,e)
                break
    print("Standard SOP form: ")
    ne=[]
    for i in e:
        if i not in ne:
            ne.append(i)
    print(*ne,sep=" + ")
    return ne

def soppos():
    v=list(input("Enter variables:").split())
    e=list(input("Enter SOP expression:").split("+"))
    t=["0000","0001","0010","0011","0100","0101","0110","0111","1000","1001","1010","1011","1100","1101","1110","1111"]
    e=sopcon(e,v)
    f=[]
    for i in e:
        s=""
        for j in v:
            ix=i.find(j)
            if ix!=len(i)-1:
                if i[ix+1]=="'":
                    s=s+"0"
                else:
                    s=s+"1"
            else:
                s=s+"1"
        f.append(s)
    for i in f:
        t.remove(i)
    f=[]
    for k in t:
        i=""
        for j in k:
            if j=="0":
                i=i+"' "
            else:
                i=i+" "
        f.append("("+v[0]+i[0]+"+"+v[1]+i[1]+"+"+v[2]+i[2]+"+"+v[3]+i[3]+")")
    print("POS expression:");
    print(*f,sep="")

def pos(t,a,v,e):
        e.remove(t)
        nt=t+"+"+a
        e.append(nt)
        e.append(nt+"'")
        for j in v:
            if nt.find(j)==-1:
                pos(nt,j,v,e)
                pos(nt+"'",j,v,e)
                break

def poscon(ne,v):
    n=len(ne)
    e=[]
    for i in ne:
        s=i
        f=0
        e.append(i)
        for j in v:
            if s.find(j)==-1:
                pos(s,j,v,e)
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
    return ne   
    
def possop():
    v=list(input("Enter variables:").split())
    e=list(input("Enter POS expression:").split(")("))
    t=["0000","0001","0010","0011","0100","0101","0110","0111","1000","1001","1010","1011","1100","1101","1110","1111"]
    p=e.pop(0)
    p=p[1:]
    e.insert(0,p)
    p=e.pop(len(e)-1)
    p=p[:len(p)-1]
    e.append(p)
    e=poscon(e,v)
    f=[]
    for i in e:
        s=""
        for j in v:
            ix=i.find(j)
            if ix!=len(i)-1:
                if i[ix+1]=="'":
                    s=s+"1"
                else:
                    s=s+"0"
            else:
                s=s+"0"
        f.append(s)
    for i in f:
        t.remove(i)
    f=[]
    for k in t:
        i=""
        for j in k:
            if j=="0":
                i=i+" "
            else:
                i=i+"' "
        f.append(v[0]+i[0]+v[1]+i[1]+v[2]+i[2]+v[3]+i[3])
    print("SOP expression:");
    print(*f,sep=" + ")
o=input("OPTIONS\n1:SOP to POS\n2:POS to SOP\nEnter your choice:")
if o=="1":
    soppos()
else:
    possop()
