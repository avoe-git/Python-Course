day = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
persons = int(input('Persons:'))
StartTime=0
while StartTime>0:
    for PersonCount in range(1,persons+1):
        CurrentPersonName = input('CurrentPersonName:')
        works = int(input('works:'))
        for WorkCount in range(1,works+1):
            StartTime=int(input('StartTime:'))
            FinishTime=int(input('FinishTime:'))
            CopyList = day.copy()

print(str(day)+'\n'+persons+'\n'+StartTime+'\n'+PersonCount+'\n'+WorkCount+'\n'+StartTime+'\n'+FinishTime)