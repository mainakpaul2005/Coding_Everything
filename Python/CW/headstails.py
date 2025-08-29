import random
import itertools
coin = {
    'heads':0,
    'tails':0
}
ch=list(coin.keys())
for i in range(10):
    x=random.choice(ch)
    coin[x]=coin[x]+1
print("No of heads : ",coin['heads'])
print("No of tails : ",coin['tails'])    