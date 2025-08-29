import count as C1, Check as C2
def main(l1,l2):
    count=C1.htrec()
    rec=C2.htcheck(count)
    for i in range(len(rec)):
       if rec[i]=="Head":
        l1.append(rec[i])
       elif rec[i]=="Tail":
        l2.append(rec[i])
    