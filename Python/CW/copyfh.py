with open("Delhi.txt") as F:
    with open("abc.txt",'w') as F1:
        for i in F:
            F1.write(i.replace('a' or 'A',''))    
F1.close
F.close        