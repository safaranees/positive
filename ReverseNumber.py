number=int(input())
rev=0
while(number!=0):
    d=number%10
    rev=rev*10 +d
    number//=10
print(rev)
