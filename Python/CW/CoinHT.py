import random
ch=0
ct=0
def coinht():
    return random.choice([1,0])
for i in range(10):
    if coinht()==0:
        ch=ch+1
    else:
        ct=ct+1
print(ct)
print(ch)        