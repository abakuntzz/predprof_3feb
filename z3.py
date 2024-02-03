file=open('game.txt')
data=file.read().split('\n')
data.pop(0)
datanew=[]
for i in data:
    s=i.split('$')
    datanew.append(s)
while True:
    charname=input('Введите имя персонажа: ')
    if charname=='game':
        break
    c=0
    games=[]
    print('Персонаж встречается в играх:')
    for i in datanew:
        if c==5:
            break
        if i[1]==charname and i[0] not in games:
            print(i[0])
            games.append(i[0])
            c+=1
    if c==0:
        print('Этого персонажа не существует')