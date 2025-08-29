def htcheck(l):
    rec=[]
    for i in range(len(l)):
        if l[i]==0:
            rec.append("Tail")
        elif l[i]==1:    
            rec.append("Head")
    return rec

