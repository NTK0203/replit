N,M = map(int,input().split())
number = []
max=0
for i in range(N):
    number = list(map(int,input().split()))
    number.sort()
    if(number[0]>max):
        max=number[0]
print(max)