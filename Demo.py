num=5
star=1
for line in range(1,num+1):
    for st in range(star):
        print('*',end=' ')
    print()
    if line<num//2+1:
        star+=1
    else:
        star-=1
