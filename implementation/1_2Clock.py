N = int(input())
hour = 0
min = 0
sec = 0
count=0
for hour in range(N+1):
    for min in range(60):
        for sec in range(60):
            if(hour%10==3):
                count+=1
                continue
            elif(min%10==3 or min//10==3):
                count+=1
                continue
            elif(sec%10==3 or sec//10==3):
                count+=1
                continue
print(count)