import Cointoss as c
ch,ct=0,0
lst=['T','H']
for i in range(10):
    if c.coinht()==1:
        print(lst[c.coinht()])
        ch=ch+1
    else:
        print(lst[c.coinht()])
        ct=ct+1 
print("No of heads : ",ch)
print("No of tails : ",ct)           