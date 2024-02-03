file=open('game.txt')
data=file.read().split('\n')
data.pop(0)
datanew=[]
for i in data:
    s=i.split('$')
    datanew.append(s)
datanew=sorted(datanew,key=lambda x: x[1])
while True:
    charname=input('Введите имя персонажа: ')
    if charname=='game':
        break
    c=0
    left=0
    right=len(datanew)-1
    while abs(left-right)>1:
        mid=(left+right)//2
        if datanew[mid][1]<charname:
            left=mid
        elif datanew[mid][1]>charname:
            right=mid
        else:
            break
    for i in range(max(0,mid-4),min(len(datanew),mid+5)):
        if datanew[i][1]==charname:
            print(datanew[i][0])
            c+=1
        if c==5:
            break

    if c==0:
        print('Этого персонажа не существует')