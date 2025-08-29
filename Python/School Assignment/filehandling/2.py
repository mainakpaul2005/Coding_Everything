def readLine():
    f=open("Delhi.txt",'r')
    l=f.readlines()
    for i in l:
        if i[0]=='D' or i[0]=='M':
           print(i)
    f.close()
readLine()           