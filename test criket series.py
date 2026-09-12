test1={}
print('Enter test one Player Name & runs')
for i in  range(11):
    print('EnterPlayer Name:',i+1)
    p=input()
    r=int(input('Runs:'))
    test1.update({p:r})
test2={}
print('Enter test two Player Name & runs')
for i in  range(11):
    print('Enter Player Name:',(i+1))
    p=input()
    r=int(input('Runs:'))
    test2.update({p:r})    
print('__________________________________________')
print('Test 1: Players\t :  Runs')
print('__________________________________________')
for k,v in test1.items():
    print(k,'\t\t',v)
print('__________________________________________')
print('Test 2:Players\t :  Runs')
print('__________________________________________')
for k,v in test2.items():
    print(k,'\t\t',v)
def Max_Score(test1,test2):
    Series={}
    Series.update(test1)
    for k in test2.keys(): #Any  player is one test played is also worked this logic
        v=Series.get(k,-1)
        if v!=-1:
            Series.update({k:v+test2[k]})
        else:
            Series.update({k:test2[k]})
    print('__________________________________________')
    print('This Series Total Runs test1,test1')
    print('Players \t :  Runs')
    print('__________________________________________')
    for k,v in Series.items():
        print(k,'\t\t',v)
    Sort_dict=sorted(Series.items(),key= lambda k: k[1], reverse=True)
    player_runs=Sort_dict[0]
    player,runs=tuple(player_runs)
    return player,runs
    
    
player,runs=Max_Score(test1,test2)
print('__________________________________________')
print('Top player:',player, end='\t\t')
print('Runs:',runs)
print('__________________________________________')
print('Player type:\t',type(player),',' 'Runs Type:',type(runs))
