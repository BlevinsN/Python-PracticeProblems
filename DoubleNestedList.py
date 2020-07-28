AllRecords = []
for _ in range(int(raw_input())):
    name = raw_input()
    score = float(raw_input())
    NewRecord = [name, score]
    AllRecords.append(NewRecord)
AllRecords.sort(key = lambda x: x[0])
AllRecords.sort(key = lambda x: x[1])
index = 0
Lowest = AllRecords[0][1]
while AllRecords[index][1] == Lowest:
    index+=1
Lowest = AllRecords[index][1]
while AllRecords[index][1] == Lowest:
        print(AllRecords[index][0])
        index+=1
